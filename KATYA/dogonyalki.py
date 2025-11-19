import pgzrun
import random

WIDTH = 800
HEIGHT = 600

G = (30, 120, 30)
W = (255, 255, 255)
lan=(255,255,0)
he = Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
ta = Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
fan = Rect(random.randint(0, WIDTH-10),random.randint(0, HEIGHT-10),10,10)
x=0
y=0
t=0
l=0
cuo=1
score=0
ssore=0
def draw():
    screen.fill(G)
    screen.draw.filled_rect(he, W)
    screen.draw.filled_rect(ta, lan)
    screen.draw.filled_rect(fan, W)
    screen.draw.text("1 СЃС‡С‘С‚: "+str(score),center=(WIDTH//2-100,10),color=W)
    screen.draw.text("2 СЃС‡С‘С‚: " + str(ssore), center=(WIDTH // 2+100, 10), color=lan)
def update():
    global x, y, score,t, l, ssore
    if he.colliderect(fan):
        fan.x=random.randint(0,WIDTH-10)
        fan.y =random.randint(0,HEIGHT-10)
        score+=1
    if ta.colliderect(fan):
        fan.x=random.randint(0,WIDTH-10)
        fan.y =random.randint(0,HEIGHT-10)
        ssore+=1

    if keyboard.w:
        y -= cuo
    if keyboard.a:
        x -= cuo
    if keyboard.s:
        y += cuo
    if keyboard.d:
        x += cuo
    if he.top <=0:
        he.y = HEIGHT - he.height - 3
    if he.left <= 0:
        he.x = WIDTH - he.width - 3
    if he.right >= WIDTH:
        he.x = 0
    if he.bottom >= HEIGHT:
        he.y = 0
    he.x+=x
    he.y += y
    x=x*0.9
    y=y*0.9

    if keyboard.up:
        l -= cuo
    if keyboard.left:
        t -= cuo
    if keyboard.right:
        t += cuo
    if keyboard.down:
        l += cuo
    if ta.top <=0:
        ta.y = HEIGHT - ta.height - 3
    if ta.left <= 0:
        ta.x = WIDTH - ta.width - 3
    if ta.right >= WIDTH:
        ta.x = 0
    if ta.bottom >= HEIGHT:
        ta.y = 0

    t = t * 0.9
    l = l * 0.9
    ta.x+=t
    ta.y+=l


pgzrun.go()
