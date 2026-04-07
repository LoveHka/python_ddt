import socket
import threading
import json
import os
import random

HOST = "0.0.0.0"
PORT = 7000
USERS_FILE = "users.json"

clients = {}  # conn -> user object
users_db = {}
lock = threading.Lock()


class User:
    def __init__(self, username, addr):
        self.username = username
        self.addr = addr
        self.exp = 0
        self.money = 0

        # --- game state ---
        self.in_game = False
        self.secret_number = None
        self.attempts_left = 0

    def to_dict(self):
        return {
            "username": self.username,
            "exp": self.exp,
            "money": self.money
        }


# ---------- Persistence ----------
def load_users():
    global users_db
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            users_db = json.load(f)
    else:
        users_db = {}


def save_users():
    with lock:
        with open(USERS_FILE, "w") as f:
            json.dump(users_db, f, indent=4)


# ---------- Auth ----------
def register(username, password):
    if username in users_db:
        return False, "exists"

    users_db[username] = {
        "password": password,
        "exp": 0,
        "money": 0
    }
    save_users()
    return True, "ok"


def login(username, password):
    if username not in users_db:
        return False, "not_found"

    if users_db[username]["password"] != password:
        return False, "wrong_pass"

    return True, "ok"

# --------- BROADCAST --------

def broadcast(message):
    print(message)

    dead_clients = []
    for conn in clients:
        try:
            conn.sendall((message + "\n").encode())
        except:
            dead_clients.append(conn)

    #for conn in dead_clients:
        #if conn in clients:
            #del clients[conn]
# ------ TO_CLIENT -------

def send_to_client(conn, message):
    try:
        conn.sendall((message + "\n").encode())
    except:
        if conn in clients:
            del clients[conn]
        conn.close()

# ----- from one to one -------


# ---------- Game Random ----------
def start_game(user):
    user.in_game = True
    user.secret_number = random.randint(0, 20)
    user.attempts_left = 5

    broadcast(f"[GAME] {user.username}, у тебя 5 попытки. Я загадал число от 0 до 20")


def handle_guess(user, conn, message):
    try:
        guess = int(message)
    except ValueError:
        send_to_client(conn, f"[GAME] {user.username}, введи число")
        return

    user.attempts_left -= 1

    if guess == user.secret_number:
        reward_m = 10
        reward_e = 2
        users_db[user.username]["money"] += reward_m
        users_db[user.username]["exp"] += reward_e
        save_users()

        broadcast(f"[GAME] {user.username} угадал число {user.secret_number} и получил {reward_m}$ и {reward_e} exp")
        user.in_game = False
        return

    if user.attempts_left <= 0:
        send_to_client(conn,f"[GAME] {user.username} проиграл. Было число: {user.secret_number}")
        user.in_game = False
        return

    if guess < user.secret_number:
        hint = "больше"
    else:
        hint = "меньше"

    send_to_client(conn,f"[GAME] {user.username}, неверно. Подсказка: {hint}. Осталось попыток: {user.attempts_left}")


# --- CSASINO
# ---------- Casino Game ----------
def handle_casino(user, message):
    parts = message.split()

    if len(parts) < 2:
        broadcast(f"[CASINO] {user.username}, используй: CASINO <ставка>")
        return

    try:
        bet = int(parts[1])
    except ValueError:
        broadcast(f"[CASINO] {user.username}, ставка должна быть числом")
        return

    if bet <= 0:
        broadcast(f"[CASINO] {user.username}, ставка должна быть больше 0")
        return

    current_money = users_db.get(user.username, {}).get("money", 0)

    if current_money <= 0:
        broadcast(f"[CASINO] {user.username}, у тебя нет денег для игры")
        return

    if bet > current_money:
        broadcast(f"[CASINO] {user.username}, недостаточно денег. Баланс: {current_money}$")
        return

    broadcast(f"[CASINO] {user.username} ставит {bet}$... Крутим рулетку 🎰")

    roll = random.randint(1, 100)

    if roll <= 50:
        users_db[user.username]["money"] -= bet
        save_users()
        broadcast(f"[CASINO] ❌ Не повезло... шарик уходит мимо. Ты теряешь {bet}$")

    elif roll <= 85:
        users_db[user.username]["money"] += bet
        save_users()
        broadcast(f"[CASINO] ✅ Удача на твоей стороне! Ставка сыграла")
        broadcast(f"[CASINO] ➕ Ты выигрываешь {bet}$")

    else:
        users_db[user.username]["money"] += bet * 2
        save_users()
        broadcast(f"[CASINO] 🔥 ДЖЕКПОТ!!! Невероятное везение!")
        broadcast(f"[CASINO] 💎 Ты получаешь {bet * 2}$ сверху")

    broadcast(f"[CASINO] 💰 Текущий баланс: {users_db[user.username]['money']}$")


# ---------- Client Handler ----------
def handle_client(conn, addr):
    broadcast(f"[+] Подключился клиент: {addr}\n Пиши REGISTER <логин> <пароль>\n Или LOGIN <логин> <пароль>")
    send_to_client(conn, f"[+] Подключился клиент: {addr}\n Пиши REGISTER <логин> <пароль>\n Или LOGIN <логин> <пароль>")
    user = None

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode().strip()

            # --- AUTH ---
            if user is None:
                parts = message.split()
                if len(parts) < 3:
                    continue

                command, username, password = parts[0], parts[1], parts[2]

                if command.upper() == "REGISTER":
                    ok, _ = register(username, password)
                    if ok:
                        user = User(username, addr)
                        clients[conn] = user
                        broadcast(f"[REG] Новый пользователь: {username}")

                elif command.upper() == "LOGIN":
                    ok, _ = login(username, password)

                    if ok:
                        user = User(username, addr)
                        clients[conn] = user
                        broadcast(f"[LOGIN] {username} вошел ({addr})")

                continue

            # --- AFTER LOGIN ---
            if message.upper() == "LIST":
                user_list = [u.username for u in clients.values()]
                broadcast("[ONLINE] \n > "+ '\n > '.join(user_list))
                continue

            # --- START GAME ---
            if message.upper() == "GAME":
                if not user.in_game:
                    start_game(user)
                else:
                    broadcast(f"[GAME] {user.username}, ты уже в игре")
                continue

            # --- GAME PROCESS ---
            if user.in_game:
                handle_guess(user, conn, message)
                continue
            # --- CASINO ---
            if message.upper().startswith("CASINO"):
                handle_casino(user, message)
                continue
            # --- STATS ----
            if message.upper() == "STATS":
                data = users_db.get(user.username, {})
                exp = data.get("exp", 0)
                money = data.get("money", 0)

                broadcast(f"""[STATS] {user.username}
 > EXP: {exp}
 > MONEY: {money}""")
                continue

            # Основной вывод на экран ("большой экран")
            broadcast(f"[{user.username}] {message}")

    except ConnectionResetError:
        broadcast(f"[-] Клиент отключился (ошибка): {addr}")

    finally:
        if conn in clients:
            broadcast(f"[-] Отключен: {clients[conn].username}")
            del clients[conn]
        else:
            broadcast(f"[-] Отключен: {addr}")

        conn.close()


# ---------- Server ----------
def start_server():
    load_users()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[*] Сервер запущен на {HOST}:{PORT}")
    print("[*] Все сообщения будут выводиться на экран\n")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()


start_server()
