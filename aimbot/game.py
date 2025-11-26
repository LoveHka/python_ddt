import pgzrun   # Импорт бибилиотеки с играми
import random   # Импорт библиотеки случайных чисел
import time     # Импорт библиотеки времени

WIDTH = 600     # Ширина экрана
HEIGHT = 500    # Высота экрана

WHITE = (255, 255, 255)     # Цвета
BLACK = (0, 0, 0)           # ( Красный, Зелёный, Синий )

score = 0   # Счёт
start_time = time.time()
timer = start_time

def on_mouse_down(pos):     # Если щёлкнули мышкой
    pass

def draw():     # Функция для рисования
    screen.fill(WHITE)
    screen.draw.text("Счёт: " + str(score), (10, 10), color=BLACK)
    screen.draw.text("Время: " + str(int(60 - timer)) + " секунд", (10, 35), color=BLACK)

def update():   # Функция для обновления данных
    global start_time, score, timer
    timer = time.time() - start_time

pgzrun.go()
