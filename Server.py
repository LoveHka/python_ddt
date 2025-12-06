import pgzrun
import socket

WIDTH, HEIGHT = 300, 200
sock = socket.socket()
sock.bind(('0.0.0.0', 12345))
sock.listen(1)
sock.setblocking(False)
client = None

def update():
    global client
    if not client:
        try:
            client, _ = sock.accept()
            client.setblocking(False)
        except: pass

    if not client: return
    try:
        if keyboard.w: client.send(b'W')
        if keyboard.a: client.send(b'A')
        if keyboard.s: client.send(b'S')
        if keyboard.d: client.send(b'D')
    except: pass

def draw():
    screen.clear()
    screen.draw.text("Нажимай WASD", (50, 80), fontsize=40)

pgzrun.go()
