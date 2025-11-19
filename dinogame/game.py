import pgzrun
import random

WIDTH=800
HEIGHT=600

BLACK=(0,0,0)
WHITE=(255,255,255)

floor=400 # расстояние от потолка до пола
game_speed=5 # Скорость игры
dino_height = 40 # Высота динозавтрика

def draw():
    screen.fill(WHITE)
    screen.draw.line(  (0,400),  (WIDTH,400), BLACK  )

def update():
    pass
pgzrun.go()
