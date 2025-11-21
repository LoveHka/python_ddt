import pgzrun
import random

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)  # Цвета
WHITE = (255, 255, 255)

dino = Actor("dino1.png", pos=(WIDTH // 2, HEIGHT // 2))  # Создали динозавра
animation_timer = 0

def draw():
    screen.fill(WHITE)  # Заполняем фон экрана белым цветом
    dino.draw()


def update():
    global animation_timer
    animation_timer += 1
    if animation_timer > 10:
        if dino.image == "dino1.png":
            dino.image = "dino2.png"
        else:
            dino.image = "dino1.png"
        animation_timer = 0
    if keyboard.w:
        dino.y -= 3
    if keyboard.s:
        dino.y += 3
    if keyboard.a:
        dino.x -= 3
    if keyboard.d:
        dino.x += 3


pgzrun.go()
