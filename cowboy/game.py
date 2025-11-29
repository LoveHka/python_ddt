import pgzrun   # Импорт бибилиотеки с играми
import random   # Импорт библиотеки случайных чисел

WIDTH = 800     # Ширина экрана
HEIGHT = 600    # Высота экрана

WHITE = (255,255,255) # Добавляем цвета
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0 ,0)

hero = Rect(WIDTH // 2, HEIGHT // 2, 20, 40) # Создаём персонажа ( стоит в центре, размер 20 х 40 пикселей )

bullets = [] # Пустой список для пуль
b_speed = 10 # Скорость пуль

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

def update():   # Функция для обновления данных
    pass

pgzrun.go()

