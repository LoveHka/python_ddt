import socket

status = input("Вы будете сервер(s) или клиент(c) ?\n>")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

if status == "s":
    sock.bind(("0.0.0.0", port))
    sock.listen()
    print("Сервер ждёт подключения...")
    conn, addr = sock.accept()
else:
    ip = input("Введите IP адрес сервера!\n>")
    sock.connect((ip, port))

def sendmsg(msg):
    if status == "s":
        conn.send(msg.encode())
    else:
        sock.send(msg.encode())

def recvmsg():
    if status == "s":
        return conn.recv(1024).decode()
    else:
        return sock.recv(1024).decode()

print("Соединение успешно!")

