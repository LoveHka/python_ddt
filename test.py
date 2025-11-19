import pgzrun

WIDTH = 800
HEIGHT = 600

GREEN = (30, 120, 30)
WHITE = (255, 255, 255)
hero = Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
speed = 5
def draw():
    screen.fill(GREEN)
    screen.draw.filled_rect(hero, WHITE)

def update():
    if keyboard.w and hero.top > 0:
        hero.y -= speed
    if keyboard.a and hero.left > 0:
        hero.x -= speed
    if keyboard.s and hero.bottom < HEIGHT:
        hero.y += speed
    if keyboard.d and hero.right < WIDTH:
        hero.x += speed


pgzrun.go()
