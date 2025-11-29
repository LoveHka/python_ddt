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
    bullets.append(
        [  ]
    )

def draw():     # Функция для рисования 
    screen.fill(GREEN)
    screen.draw.filled_rect(hero, BLACK)

def update():   # Функция для обновления данных
    pass

pgzrun.go()

