import pgzrun
import random

WIDTH=800
HEIGHT=600

BLACK=(0,0,0) #Цвета
WHITE=(255,255,255)

floor=400 # расстояние от потолка до пола
game_speed=5 # Скорость игры
dino_height = 40 # Высота динозавтрика

dino = Rect(100, floor - dino_height, 20, dino_height)
jump = 5 # СИла прыжка
gravi = 0.2 # Сила гравитации
dino_speed = 0 # Скорость динозаврика
can_jump = True # Может ли динозавр прыгнуть сейчас?

kaktus = [] # Добавляем препятствия
for i in range(4): 
    kaktus.append(Rect(WIDTH + random.randint(400*i, 400*(i+1)), floor - 30, 10, 30 )) # Добавляем прямоугольник в конец списка

game_over = False # Переменная для проигрыша
def draw():
    screen.fill(WHITE) # Рисуем фон экрана
    screen.draw.line(  (0,400),  (WIDTH,400), BLACK  ) # Рисуем линию - пол
    screen.draw.filled_rect(dino, BLACK) # Рисуем динозавра
    for k in kaktus:# Рисуем все каактусы
        screen.draw.filled_rect(k, BLACK)
    if game_over:
        screen.draw.text("Game Over", center = (WIDTH // 2, HEIGHT // 3), color = BLACK, fontsize = 60)
        screen.draw.text("press R", center=(WIDTH // 2, HEIGHT // 3+30), color=BLACK, fontsize=30)

def update():
    global game_speed, dino_speed, can_jump, game_over, kaktus # Добавляем переменные снаружи в функци
    if game_over: # Если игра закончена, то
        if keyboard.r: # Если нажата клавиша R, то начинаем игру с начала
            game_over = False
            kaktus = []  # Добавляем препятствия
            for i in range(4):
                kaktus.append(Rect(WIDTH + random.randint(400 * i, 400 * (i + 1)), floor - 30, 10, 30))
            dino_speed = 0  # Скорость динозаврика
            can_jump = True  # Может ли динозавр прыгнуть сейчас?
            dino.y = floor - dino_height  # Cтавим ровно на пол
        return # Пропускаем игровой цикл ( всё, что ниже)

    for k in kaktus: # Выполянем команды для каждого кактуса
        k.x -= game_speed # Двигаем кактус влево
        if k.right < 0: # если кактус уехал за экран, телепортируем в начало
            k.x = WIDTH + random.randint(0, 800) # делаем вид, что кактусы появляются в случайный момент
        if k.colliderect(dino): # При столкновении кактуса с динозавром,
            game_over = True

    if dino.bottom < floor: # Если дино в воздухе
        can_jump = False # Прыгать не может
        dino_speed += gravi # Гравитация тянет вниз
    else: # иначе, если на полу
        dino.y = floor - dino_height # Cтавим ровно на пол
        dino_speed = 0 # Скорость равна нулю
        can_jump = True # Снова можем прыгать

    if (keyboard.up or keyboard.w or keyboard.space) and can_jump:
        # если нажата одна из трёх кнопок 
        # И мы можем прыгать, то прыгаем
        dino_speed -= jump 

    dino.y += dino_speed # изменяем координату динозавра, прибавляем к ней скорость



pgzrun.go() # Команда для открытия окна и старта игры
