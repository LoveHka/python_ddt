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

def on_key_down(key):
    if not client: return
    try:
        if key == keys.W: client.send(b'W')
        if key == keys.A: client.send(b'A')
        if key == keys.S: client.send(b'S')
        if key == keys.D: client.send(b'D')
    except: pass

def draw():
    screen.clear()
    screen.draw.text("Нажимай WASD", (50, 80), fontsize=40)

pgzrun.go()
