import pgzrun
import time

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

hero = Rect(100, 100, 20, 40)

cooldown = 0.5 # Это время перезарядки
last_attack = 0 # Когда была последняя атака?

berries = [] # Пока что пусто. Тут будут лежать ягоды
berrie_speed = 10
# Функция принимает от нас позицию мышки
def attack(mouse_pos): # Это наша собственная функция для атаки.
    global last_attack # Узнаём, КОГДА была последняя атака
        if last_attack - time.time() > cooldown: # Если прошло достаточно времени
            last_attack = time.time() # Обновляем таймер
            dx = mouse_pos[0] - hero.x
            dy = mouse_pos[1] - hero.y
            distance = (dx^2 + dy^2)^0.5
            speed_x = berrie_speed * (dx / distance)
            speed_y = berrie_speed * (dy / distance)
            berries.append(
                [ Rect(hero.x, hero.y, 10, 10), speed_x, speed_y ]
            )


def draw():
    screen.fill(WHITE)
    screen.draw.filled_rect(hero, BLACK)
def update():




pgzrun.go()
