import pgzrun   # Импорт бибилиотеки с играми
import random   # Импорт библиотеки случайных чисел
import time     # Импорт библиотеки времени

WIDTH = 800     # Ширина экрана
HEIGHT = 600    # Высота экрана

WHITE = (255, 255, 255)     # Цвета
BLACK = (0, 0, 0)           # ( Красный, Зелёный, Синий )

score = 0
max_time = 10 # Время на игру в секундах
start_time = time.time() # Запоминаем, когда начали игру !
timer = 0
game_over = True

size = 30 # Размер цели
target = Rect(WIDTH // 2, HEIGHT // 2, size, size)

def on_mouse_down(pos):     # Если щёлкнули мышкой
    global score
    if target.collidepoint(pos) and not game_over:
        score += 1
        target.x = random.randint(0, WIDTH - size)
        target.y = random.randint(0, HEIGHT - size)

def draw():     # Функция для рисования
    screen.fill(WHITE)
    if not game_over:
        screen.draw.text(f"Счёт: {score}", (10, 10), color=BLACK)
        screen.draw.text(f"Время: {int(timer)} секунд", (10, 30), color=BLACK)
        screen.draw.filled_circle((target.x + size // 2, target.y + size // 2), size // 2, BLACK)
    else:
        screen.draw.text(f"Вы набрали {score} очков!", center=(WIDTH//2, HEIGHT//2-50), fontsize=60, color=BLACK)
        screen.draw.text(f"Скорость реакции: {(max_time / score) if score > 0 else 'Вы ничего не нажали'}", center=(WIDTH // 2 - 50, HEIGHT // 2), color=BLACK)

def update():   # Функция для обновления данных
    global timer, score, start_time, game_over
    timer = time.time() - start_time
    if timer > max_time: # Если время закончилось, то game over
        game_over = True
    if game_over: # Если игра закончена
        if keyboard.space: # Если нажата клавиша space
            score = 0 # Обновляем счёт
            start_time = time.time() # Обновляем время начала игры
            game_over = False



pgzrun.go()

