import pgzrun

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0) # Цвета
WHITE = (255, 255, 255)

dino = Rect(60, HEIGHT // 2, 20, 20)

def draw():
    screen.fill(WHITE)
    screen.draw.filled_rect(dino, BLACK)
    screen.draw.line((0, HEIGHT // 2 + dino.height),(WIDTH, HEIGHT // 2 + dino.height), BLACK)

def update():
    pass

pgzrun.go()
