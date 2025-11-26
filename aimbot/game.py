import pgzrun   # Импорт бибилиотеки с играми
import random   # Импорт библиотеки случайных чисел
import time     # Импорт библиотеки времени

WIDTH = 600     # Ширина экрана
HEIGHT = 500    # Высота экрана

WHITE = (255, 255, 255)     # Цвета
BLACK = (0, 0, 0)           # ( Красный, Зелёный, Синий )

score = 0   # Счёт
start_time = time.time() # Когда началась игра
timer = start_time # Сколько прошло времени
max_time = 30   # Максимум времени
game_over = False    # Конец игры  ( кончилась или нет )
size = 30    # Размер мишени
target = Rect(WIDTH // 2, HEIGHT // 2, size, size)  # Создаём мишень

def on_mouse_down(pos):     # Если щёлкнули мышкой
    global score
    if target.collidepoint(pos): # Если мышка была на мишени
        target.x = random.randint(0, WIDTH - size)
        target.y = random.randint(0, HEIGHT - size)
        score += 1

def draw():     # Функция для рисования
    screen.fill(WHITE) #Заполняем экран белым цветом
    if not game_over: # Если игра не закончилась то будет выполняться это условие:
        screen.draw.filled_circle((target.x + size//2, target.y + size//2), size//2, BLACK) # Рисуем мишень
        screen.draw.text("Счёт: " + str(score), (10, 10), color=BLACK) # Выводим на экран текст "Счет"
        screen.draw.text("Время: " + str(int(max_time - timer)) + " секунд", (10, 35), color=BLACK)  # Выводим на экран текст "Время"
    else: # Иначе
        screen.draw.text("Вы набрали " + str(score) + " очков!", center=(WIDTH // 2, HEIGHT // 2),fontsize=60, color = BLACK)
        # Выводим на экран текст, о том сколько вы набрали очков
def update():   # Функция для обновления данных
    global start_time, score, timer, game_over
    timer = time.time() - start_time # Сколько времени с начала игры
    if timer > max_time: # Пока таймер не перевесит максимальное время
        game_over = True # Игра окончена


pgzrun.go()

