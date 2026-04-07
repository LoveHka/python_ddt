import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket()
client.connect((HOST, PORT))

print("Подключено к серверу. Пиши сообщения:")

while True:
    msg = input("> ")
    client.send(msg.encode())
