import pgzrun
import socket
import threading

SERVER = "192.168.0.155"
PORT = 12345

WIDTH = 800
HEIGHT = 600

players = {}
players_lock = threading.Lock()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((SERVER, PORT))

def send_move(directrion):
    client.send(directrion.encode())

def recive_loop():
    while True:
        data = client.recv(1024)
        msg = data.decode().strip()

        new_players = {}

        if msg:
            parts = msg.split(";")
            for p in parts:
                if not p:
                    continue
                try:
                    ip, x, y = p.split(":")
                    new_players[ip] = (int(x), int(y))
                except:
                    pass

            with players_lock:
                players.clear()
                players.update(new_players)

threading.Thread(target=recive_loop, daemon=True).start()

def update():

    if keyboard.w:
        send_move("up")
    if keyboard.a:
        send_move("left")
    if keyboard.s:
        send_move("down")
    if keyboard.d:
        send_move("right")

def draw():
    screen.fill((20,20,20))

    with players_lock:
        current_players = dict(players)

        # center_x = WIDTH // 2
        # center_y = HEIGHT // 2
        if not current_players:
            screen.draw.text("No players!", (20,20), fontsize=40, color="white")
            return

        for ip, (x, y) in current_players.items():
            rect = Rect(x - 10, y -10, 20, 20)
            screen.draw.filled_rect(rect, "deepskyblue")
            screen.draw.rect(rect, "white")

pgzrun.go()
