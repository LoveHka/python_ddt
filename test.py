import pgzrun

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0) # Цвета
WHITE = (255, 255, 255)

dino = Rect(60, HEIGHT // 2, 20, 40) # Создали динозавра
dino_speed = 0 # СКорость динозавтра
jump = 5 # Сила прыжка
gravi = 0.2 # Сила гравитации
can_jump = True # Можно прыгать
def draw():
    screen.fill(WHITE) # Заполняем фон экрана белым цветом
    screen.draw.filled_rect(dino, BLACK) # Рисуем динозавтрика - квадратик
    screen.draw.line((0, HEIGHT // 2 + 40), (WIDTH, HEIGHT // 2 + 40), BLACK)

def update():
    global dino_speed, can_jump
    
    if keyboard.down:
        dino.height = 20
    else:
        dino.height = 40

    if dino.bottom < HEIGHT // 2 + dino.height:
        dino_speed += gravi # Если мы в воздухе, добавляем гравитацию к скорости
        can_jump = False # Не можем прыгнуть, когда мы уже в воздухе!!!
    else: # Если мы падаем на или под линию, то возвращаем ровно в начальную позицию
        dino.y = HEIGHT // 2 + 40 - dino.height
        dino_speed = 0
        can_jump = True
    if keyboard.up and can_jump:
        dino_speed -= jump


    dino.y += dino_speed
pgzrun.go()
