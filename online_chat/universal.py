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
    for variant in win: # Для каждого победного варианта
        for pos in variant: # ПРоверяем каждую позицию
            if field[pos] != flag:  # Если в поле на победной позиции нет нашего маркера
                iswin=False         # Мы пока не победили
                break               # Сразу переходим к другой позиции
            iswin = True            # Сюда мы попадем только, если позиции победные
        if iswin == True:
            return True
    return False

def show_field(field):
    print("*"*20)
    print(field[0], "|", field[1], "|",field[2], "\t0 | 1 | 2")
    print("-"*9, "\t","-"*9)
    print(field[3], "|", field[4], "|", field[5], "\t3 | 4 | 5")
    print("-"*9, "\t","-"*9)
    print(field[6], "|", field[7], "|", field[8], "\t6 | 7 | 8")
    print("*" * 20)

c=1
if status != "s":
    c=2


while True:
    # Создаём поле для игры
    field = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    show_field(field)
    print("Поле создано")
    end_game= False # Флаг окончания игры

    opponent_flag = "O"
    my_flag = "X"
    if status != "s":
        opponent_flag = "X"
        my_flag = "O"

    c += 1
    if c % 2 == 0:
        while True:

            turn = input("Ваш ход:\n>")
            if field[int(turn)] == " ":
                field[int(turn)] = my_flag
                break
            else:
                print("Сюда нельзя сходить!")
        sendmsg(turn)
        show_field(field)

    while not end_game:

        print("Ждём соперника...")
        turn = recvmsg()
        field[int(turn)] = opponent_flag
        show_field(field)
        if " " not in field:
            print("Ничья!")
            end_game = True
            break
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





