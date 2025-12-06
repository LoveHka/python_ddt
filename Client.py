import pgzrun
import socket

WIDTH, HEIGHT = 800, 600

sock = socket.socket()
sock.setblocking(False)

# connect_ex сразу возвращает код ошибки вместо исключения
result = sock.connect_ex(('192.168.1.100', 12345))  # ЗАМЕНИ IP!

# result == 0 - сразу подключились
# result == 10035 или 115 - подключаемся в фоне (Windows/Linux)
connected = (result == 0)

x, y = 400, 300

def update():
    global x, y, connected
    
    if not connected:
        # Проверяем, установилось ли подключение
        try:
            sock.send(b'')
            connected = True
        except:
            return
    
    if connected:
        try:
            cmd = sock.recv(1)
            if cmd == b'W': y -= 5
            if cmd == b'A': x -= 5
            if cmd == b'S': y += 5
            if cmd == b'D': x += 5
        except BlockingIOError:
            pass

def draw():
    screen.clear()
    screen.draw.filled_rect(Rect((x, y), (50, 50)), 'red')
    screen.draw.text(f"Квадрат: {x},{y}" if connected else "Подключаемся...", 
                    (20, 20))

pgzrun.go()
