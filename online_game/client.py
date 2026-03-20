import pgzrun
import socket

WIDTH = 600
HEIGHT = 400

server = ("192.168.3.75", 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setblocking(False)


x = 300
y = 200

speed = 3

players = {}

def update():
    global x, y

    if keyboard.left:
        x -= speed
    if keyboard.right:
        x += speed
    if keyboard.up:
        y -= speed
    if keyboard.down:
        y += speed

    msg = f"{x},{y}"
    sock.sendto(msg.encode(), server)


    try:
        data, _ = sock.recvfrom(1024)
        parse_state(data.decode())
    except:
        pass

def parse_state(state):

    players.clear()

    parts = state.split(";")

    for part in parts:
        if part:
            pid, px, py = part.split(":")
            players[int(pid)] = (int(px), int(py))

def draw():

    screen.clear()

    for pid, (px, py) in players.items():

        screen.draw.filled_rect(Rect((px, py), (30, 30)), "white")

        screen.draw.text(str(pid), (px, py), color="black")

pgzrun.go()
