
import pgzrun   # Импорт бибилиотеки с играми
import random   # Импорт библиотеки случайных чисел

WIDTH = 800     # Ширина экрана
HEIGHT = 600    # Высота экрана

WHITE = (255,255,255) # Добавляем цвета
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0 ,0)

hero = Rect(WIDTH // 2, HEIGHT // 2, 20, 20) # Создаём персонажа ( стоит в центре, размер 20 х 40 пикселей )
h_speed = 0

bullets = [] # Пустой список для пуль
b_speed = 10 # Скорость пуль

enemies = [] # Пустой список для врагов
e_speed = 2 # Скорость врагов
max_en = 5
chanse = 10

game_over = False
score=0 # добавили счёт

def on_mouse_down(pos):     # Если щёлкнули мышкой
    # Математика для расчёта скорости пули
    dx = pos[0] - hero.x                    # Разница координат х мышки и героя
    dy = pos[1] - hero.y                     # Разница координат y мышки и героя
    distance = (dx**2 + dy**2)**0.5             # Расстояние между мышкой и героем
    speed_x = b_speed * ( dx / (distance + 0.00001) )       # умножкаем модуль скорости на синус
    speed_y = b_speed * ( dy / (distance + 0.00001) )       # умножаем модуль скорости на косинус

    bullets.append(
        [ Rect(hero.x + hero.width //2 - 2, hero.y + hero.height//2 - 2, 5, 5), speed_x, speed_y ] # Добавляем пулю
    )

def draw():     # Функция для рисования
    if not game_over:
        screen.fill(GREEN) # Заполняем экран
        screen.draw.filled_rect(hero, BLACK) # Рисуем персонажа
        for b in bullets:
            screen.draw.filled_rect(b[0], RED) # Рисуем каждую пульку красным цветом
        for e in enemies:
            screen.draw.filled_rect(e, RED) # Рисуем каждого врага красным цветом
    else:
        screen.fill(BLACK) # Заполняем экран
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), color=RED, fontsize=100)

def update():   # Функция для обновления данных
    global game_over
    if game_over:
        return

    if random.randint(0, 600) < chanse and len(enemies) < max_en: # Спавн врагов
        if random.choice([True,False]):
            ex = random.randint(0, WIDTH)
            ey = random.choice([-100, HEIGHT + 100])
        else:
            ex = random.choice([-100, WIDTH + 100])
            ey = random.randint(0, HEIGHT)
        enemies.append(
            Rect(ex, ey, 20, 20)
        )

    for e in enemies: # Перемещение врагов
        dx =  hero.x - e.x   # Разница координат х мышки и героя
        dy =  hero.y - e.y   # Разница координат y мышки и героя
        distance = (dx ** 2 + dy ** 2) ** 0.5  # Расстояние между мышкой и героем

        speed_x = e_speed * (dx / (distance + 0.00001))  # умножкаем модуль скорости на синус
        speed_y = e_speed * (dy / (distance + 0.00001))  # умножаем модуль скорости на косинус
        e.x += speed_x
        e.y += speed_y
        for b in bullets:  # Проверяем столкновения врагов и пулек
            if e.colliderect(b[0]):
                bullets.remove(b)
                enemies.remove(e)

        if e.colliderect(hero): # Столкновение с героем и конец игры
            game_over = True

    if keyboard.w and hero.top > 0:
        hero.y -= h_speed
    if keyboard.s and hero.bottom < HEIGHT:
        hero.y -= h_speed
    if keyboard.a and hero.left > 0:
        hero.x -= h_speed
    if keyboard.d and hero.right < WIDTH:
        hero.x += h_speed


    for b in bullets:  # Перемещает пули
        b[0].x += b[1]
        b[0].y += b[2]

pgzrun.go()
