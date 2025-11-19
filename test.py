import pgzrun
import random
WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0) # Цвета
WHITE = (255, 255, 255)

dino = Rect(60, HEIGHT // 2, 20, 40) # Создали динозавра
dino_speed = 0 # СКорость динозавтра
jump = 5 # Сила прыжка
gravi = 0.2 # Сила гравитации
can_jump = True # Можно прыгать

cactus = []
for i in range(3): # Cоздали
    cactus.append(Rect(WIDTH + random.randint(400*i, 400*(i + 1)), HEIGHT // 2 + 10, 5, 30))
cact_speed = 5
def draw():
    screen.fill(WHITE) # Заполняем фон экрана белым цветом
    screen.draw.filled_rect(dino, BLACK) # Рисуем динозавтрика - квадратик
    screen.draw.line((0, HEIGHT // 2 + 40), (WIDTH, HEIGHT // 2 + 40), BLACK)
    for i in cactus:
        screen.draw.filled_rect(i, BLACK)

def update():
    global dino_speed, can_jump, cactus

    for i in cactus:
        if i.x < -20:
            i.x = WIDTH + random.randint(200, 800)
        i.x -= cact_speed

    if keyboard.down: # Если нажата стрелка вниз, динозавтр пригибается
        dino.height = 20
    else:
        dino.height = 40 # Иначе опять распрямляется

    if dino.bottom < HEIGHT // 2 + dino.height:
        dino_speed += gravi # Если мы в воздухе, добавляем гравитацию к скорости
        can_jump = False # Не можем прыгнуть, когда мы уже в воздухе!!!
    else: # Если мы падаем на или под линию, то возвращаем ровно в начальную позицию
        dino.y = HEIGHT // 2 + 40 - dino.height # ставим динозавтрика на пол
        dino_speed = 0 # Дино перестаёт двигаться
        can_jump = True # Теперь мы можем прыгать снова
    if keyboard.up and can_jump:
        dino_speed -= jump # Если можем прыгать и нажата кнопка вверх, то прыгаем


    dino.y += dino_speed
pgzrun.go()
