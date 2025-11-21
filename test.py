import pgzrun
import random
WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0) # Цвета
WHITE = (255, 255, 255)

dino = Actor("dino.png", pos = (WIDTH // 2, HEIGHT // 2)) # Создали динозавра

def draw():
    screen.fill(WHITE) # Заполняем фон экрана белым цветом
    dino.draw()
    
def update():
    if keyboard.w:
        dino.y -= 3
    if keyboard.s:
        dino.y += 3
    if keyboard.a:
        dino.x -= 3
    if keyboard.d:
        dino.x += 3
pgzrun.go()
