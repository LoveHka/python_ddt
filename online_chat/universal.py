import socket
import random

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

msg = ""
if status != "s":
    msg = input(">")
    sendmsg(msg)
    msg = ""
    


while True:
    print("Ждём сообщения...")
    print(recvmsg())
    msg = ""
    while msg == "":
        msg = input(">")
        sendmsg(msg)


