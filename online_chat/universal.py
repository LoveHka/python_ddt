import socket

status = input("Вы будете сервер(s) или клиент(c) ?\n>")

# подключение:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
# БЛОК ПОДКЛЮЧЕНИЯ В ЗАВИСИМОСТИ ОТ СТАТУСА
if status == "s":
    sock.bind(("0.0.0.0", port))
    sock.listen()   # ЕСЛИ СЕРВЕР, ТО ЖДЁМ ПОДКЛЮЧЕНИЯ
    print("Сервер ждёт подключения...")
    conn, addr = sock.accept()
else:
    ip = input("Введите IP адрес сервера!\n>")
    sock.connect((ip, port)) # ЕСЛИ НЕ СЕРВЕР, ТО ПОДКЛЮЧАЕМСЯ

# Функция для отправки сообщения
def sendmsg(msg):
    if status == "s":
        conn.send(msg.encode())
    else:
        sock.send(msg.encode())

# Функция для приёма сообщения
def recvmsg():
    if status == "s":
        return conn.recv(1024).decode()
    else:
        return sock.recv(1024).decode()

print("Соединение успешно!")
# Список выйгрышных вариантов
win = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
# Функция для проверки, что вариант выйгрышный
def is_win(field, flag):
    iswin = False # Предположим, что проигрышный
    for variant in win:
        for pos in variant:
            if field[pos] != flag:
                iswin=False
                break
            iswin = True
        if iswin == True:
            return True
    return False

def show_field(field):
    print(field[0], "|", field[1], "|",field[2])
    print("-"*9)
    print(field[3], "|", field[4], "|", field[5])
    print("-"*9)
    print(field[6], "|", field[7], "|", field[8])

while True:
    # Создаём поле для игры
    field = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    show_field(field)

    end_game= False

    opponent_flag = "O"
    my_flag = "X"
    if status != "s":
        opponent_flag = "X"
        my_flag = "O"
    if status != "s":
        while True:
            turn = input("Ваш ход:\n>")
            if field[int(turn)] == " ":
                field[int(turn)] = my_flag
                break
            else:
                print("Сюда нельзя сходить!")
        sendmsg(turn)
        show_field(field)

    while True:
        print("Ждём соперника...")
        turn = recvmsg()
        field[int(turn)] = opponent_flag
        show_field(field)
        if is_win(field, opponent_flag):
            print("Победил соперник!!!")
            end_game = True
        else:
            while True:
                turn = input("Ваш ход:\n>")
                if field[int(turn)] == " ":
                    field[int(turn)] = my_flag
                    break
                else:
                    print("Сюда нельзя сходить!")
            if is_win(field, my_flag):
                print("Вы победили!!!")
                end_game = True
            show_field(field)
            sendmsg(turn)



