import pgzrun
import socket

WIDTH, HEIGHT = 800, 600
sock = socket.socket()
sock.setblocking(False)

# Поменяй этот IP на IP первого компьютера!
sock.connect(('192.168.1.100', 12345))

x, y = 400, 300  # позиция квадрата

def update():
    global x, y
    try:
        cmd = sock.recv(1)  # читаем 1 байт
        if cmd == b'W': y -= 5
        if cmd == b'A': x -= 5
        if cmd == b'S': y += 5
        if cmd == b'D': x += 5
    except: pass  # ничего не пришло - ок

def draw():
    screen.clear()
    screen.draw.filled_rect(Rect((x, y), (50, 50)), 'red')
    screen.draw.text(f"Квадрат: {x},{y}", (20, 20))

pgzrun.go()
