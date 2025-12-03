import pgzrun
import time
import random

WIDTH = 800
HEIGHT = 400
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)

hero = Rect(WIDTH // 2, HEIGHT - 80, 20, 40)
speed = 5

cooldown = 0.2 # Это время перезарядки
last_attack = 0 # Когда была последняя атака?

berries = [] # Пока что пусто. Тут будут лежать ягоды
berrie_speed = 15 # СКорость начальная ягод наших, падаваны мои
gravy = 0.4 # Гравитация


baskets = [] # Список для корзин
max_baskets = 4 #  Переменная для максиального количества корзин
b_w = 40 # Ширина корзинки
for i in range(max_baskets): # Заполняем список с корзинками
    baskets.append( # Добавляем в конец списка прямоугольник
        Rect(random.randint(0, WIDTH - b_w), random.randint(100, WIDTH - 300) ,b_w, 3)
    )

# Функция принимает от нас позицию мышки
def attack(mouse_pos): # Это наша собственная функция для атаки.
    global last_attack # Узнаём, КОГДА была последняя атака
    if time.time() - last_attack > cooldown: # Если прошло достаточно времени
        last_attack = time.time() # Обновляем таймер
        dx = mouse_pos[0] - hero.x # Разница по оси икс
        dy = mouse_pos[1] - hero.y # По оси игрек
        distance = (dx**2 + dy**2)**0.5 # Расстояние между мышкой и героем
        speed_x = berrie_speed * (dx / distance) # Скорость по оси икс
        speed_y = berrie_speed * (dy / distance) # Скорость по оси игрек
        berries.append(
            [ Rect(hero.x, hero.y, 10, 10), speed_x, speed_y ]
            # Теперь у нас есть ягодки :
            # be[0] - Сам прямоугольник
            # be[1] - Горизонтальная скорость
            # be[2] - Вертикальная скорость
        )

def on_mouse_down(pos): # При нажатии мышки
    attack(pos) # Пробуем запустить нашу ягодку

def draw():
    screen.fill(WHITE)
    screen.draw.filled_rect(hero, BLACK)
    for be in berries: # Рисуем ягодки
        screen.draw.filled_rect(be[0], RED)
    for b in baskets:
        screen.draw.filled_rect(b ,ORANGE)

def update():


    for be in berries: # Для каждой ягодки мы
        be[2] += gravy # Действуем на нёё гравитацией
        be[0].x += be[1] # Изменяем координаты в соответствии со скоростью
        be[0].y += be[2]

        if be[0].top > HEIGHT: # Если ягодка скрылась под полом
            berries.remove(be) # Удаляем ягодку из нашего списка ( что бы она не падала бесконечно )




    if keyboard.a and hero.left  > 0:
        hero.x -= speed
    if keyboard.d and hero.right  < WIDTH:
        hero.x += speed


pgzrun.go()
