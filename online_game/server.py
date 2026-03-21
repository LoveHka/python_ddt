import socket

HOST = "0.0.0.0"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
server.setblocking(False)

players = {}

while True:
    while True:
        try:
            data, addr = server.recvfrom(1024)
        except:
            break

        msg = data.decode()

        if addr not in players:
            players[addr] = [100, 100]

        x, y = players[addr]

        if msg == "up":
            y -= 1
        elif msg == "down":
            y += 1
        elif msg == "right":
            x += 1
        elif msg == "left":
            x -= 1

        players[addr] = [x, y]

        state_parts = []
        for addr, (x, y) in players.items():
            ip, port = addr
            state_parts.append(f"{ip}:{x}:{y}")

        state = ";".join(state_parts)

        for addr in players:
            server.sendto(state.encode(), addr)
