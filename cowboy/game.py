import pgzrun   # Импорт бибилиотеки с играми
import random   # Импорт библиотеки случайных чисел

WIDTH = 800     # Ширина экрана
HEIGHT = 600    # Высота экрана

WHITE = (255,255,255) # Добавляем цвета
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0 ,0)

hero = Rect(WIDTH // 2, HEIGHT // 2, 20, 40) # Создаём персонажа ( стоит в центре, размер 20 х 40 пикселей )
h_speed = 0

bullets = [] # Пустой список для пуль
b_speed = 10 # Скорость пуль

enemies = [] # Пустой список для врагов
e_speed = 2 # Скорость врагов
chanse = 10

def on_mouse_down(pos):     # Если щёлкнули мышкой
    # Математика для расчёта скорости пули
    dx = pos[0] - hero.x                    # Разница координат х мышки и героя
    dy = pos[1] - hero.y                     # Разница координат y мышки и героя
    distance = (dx**2 + dy**2)**0.5             # Расстояние между мышкой и героем
    speed_x = b_speed * ( dx / distance )       # умножкаем модуль скорости на синус
    speed_y = b_speed * ( dy / distance )       # умножаем модуль скорости на косинус

    bullets.append(
        [ Rect(hero.x, hero.y, 5, 5), speed_x, speed_y ] # Добавляем пулю
    )

def draw():     # Функция для рисования 
    screen.fill(GREEN)
    screen.draw.filled_rect(hero, BLACK)
    for b in bullets:
        screen.draw.filled_rect(b[0], RED) # Рисуем каждую пульку красным цветом
    for e in enemies:
        screen.draw.filled_rect(e, RED) # Рисуем каждого врага красным цветом

def update():   # Функция для обновления данных

    if random.randint(0, 600) < chanse:
        enemies.append(
            Rect(random.choice([-100, WIDTH + 100]), random.choice([-100, HEIGHT + 100]), 20, 20)
        )

    for e in enemies:
        dx =  hero.x - e.x   # Разница координат х мышки и героя
        dy =  hero.y - e.y   # Разница координат y мышки и героя
        distance = (dx ** 2 + dy ** 2) ** 0.5  # Расстояние между мышкой и героем
        speed_x = e_speed * (dx / distance)  # умножкаем модуль скорости на синус
        speed_y = e_speed * (dy / distance)  # умножаем модуль скорости на косинус
        e.x += speed_x
        e.y += speed_y
        for b in bullets:  # Проверяем столкновения
            if e.colliderect(b[0]):
                bullets.remove(b)
                enemies.remove(e)

    for b in bullets:
        b[0].x += b[1]
        b[0].y += b[2]

pgzrun.go()

