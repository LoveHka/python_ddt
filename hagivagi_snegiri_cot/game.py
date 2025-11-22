import pgzrun
import random
WIDTH = 800 # Размеры Экрана
HEIGHT = 600
WHITE = (255,255,255) # Цвета игры
BLACK = (0, 0, 0)
floor = 400 # Высота пола
game_speed=5 # СКорость игры
dino = Actor("hero1.png") # Актёр динозавр
dino.pos = (100, floor - dino.height // 2) # Ставим динозавра прямо на пол
frame=  0

# Добавляем гравитацию и прыжки!
can_jump = True # Если стоит на земле, то можно прыгать
gravity = 0.5 # Гравитация
jump = 10 # Сила прыжка
dino_speed = 0 # Скорость динозавтрика
def draw():
    screen.fill(WHITE)  # Делаем фон белым
    dino.draw()         # Рисуем динозавра
    screen.draw.line((0, floor), (WIDTH, floor), color=BLACK)
    # ^^^^ Рисуем линию (точка 1) (точка 2) и цвет  ^^^^
def update():
    global frame, can_jump, dino_speed

    if dino.bottom < floor: # Если мы в воздухе
        can_jump = False # Запрещаем прыгать
        dino_speed += gravity # Ускоряем вниз
    else: # Если мы на земле (или под землёй)
        dino.y = floor - dino.height // 2 # Устанавливаем ровно на пол
        dino_speed = 0 # Не продолжаем падать под пол!!!
        can_jump = True # Зато можем прыгать снова

    if (keyboard.space or keyboard.w or keyboard.up) and can_jump:
        dino_speed -= jump

    dino.y += dino_speed


    # Анимация:
    frame += 1
    if frame > 10:
        if dino.image == "hero1.png":
            dino.image = "hero2.png"
        else:
            dino.image = "hero1.png"
        frame = 0

pgzrun.go()
