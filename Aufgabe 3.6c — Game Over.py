import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "750, 150"

import pgzrun
import time


def draw():
    wasser.draw()
    schiff.draw()
    insel1.draw()
    insel2.draw()
    screen.draw.text("Leben: " + str(schiff.leben), left=20, top=20, fontsize=40)
    if schiff.leben > 0:
        herz3.draw()
    if schiff.leben > 1:
        herz2.draw()
    if schiff.leben > 2:
        herz1.draw()
    if schiff.leben < 1:
        screen.draw.text("Game Over", left=100 , top=384 , fontsize=50)    
        screen.draw.text(
            "Press SPACE to start", center=(WIDTH / 2, HEIGHT / 2 + 60), fontsize=30
        )

def bewege_schiff():
    if keyboard.left:
        schiff.x = schiff.x - 10
    if keyboard.right:
        schiff.x = schiff.x + 10
    if keyboard.up:
        schiff.y = schiff.y - 10
    if keyboard.down:
        schiff.y = schiff.y + 10
    if keyboard.space:
        reset_game()    
    if schiff.left < 0:
        schiff.left = 0
    if schiff.right > WIDTH:
        schiff.right = WIDTH
    if schiff.top < 0:
        schiff.top = 0
    if schiff.bottom > HEIGHT:
        schiff.bottom = HEIGHT
        
def reset_game():
    schiff.leben = 3
    schiff.x = WIDTH / 2
    schiff.y = HEIGHT / 2
    insel1.y = -100
    insel2.y = -450
             
def update():
    if keyboard.space:
        reset_game()
    if schiff.leben <= 0:
        schiff.leben = 0
        return
    bewege_schiff()
    bewegeWasser()
    bewegeHindernis(insel1)
    bewegeHindernis(insel2)
         
def bewegeWasser():
    if wasser.y == 0:
        wasser.y = 10
        time.sleep(0.1)
    elif wasser.y == 10:
        wasser.y = 300
        time.sleep(0.1)
    elif wasser.y == 300:
        wasser.y = HEIGHT
        time.sleep(0.1)
    elif wasser.y == HEIGHT:
        wasser.y = 0
        
def bewegeHindernis(hindernis):
    hindernis.y = hindernis.y + 10
    if hindernis.y > HEIGHT + 350:
        hindernis.y = -200
    if hindernis.colliderect(schiff):
        schiff.leben = schiff.leben - 1
        hindernis.y = -200

def zurücksetzen():
    schiff.x = WIDTH / 2
    schiff.y = HEIGHT - 60
    insel1.y = -100
    insel2.x = 270
    insel2.y = -450    
            
WIDTH = 384
HEIGHT = 768
TITLE = "Melvin"

wasser = Actor("wasser.png")
schiff = Actor("segelschiff_gelb.png")
insel1 = Actor("insel1.png")
insel2 = Actor("insel2.png")
schiff.leben = 3
schiff.x = WIDTH / 2 
schiff.y = 700

herz1 = Actor("herz.png")
herz1.x = 264
herz1.y = 35
herz2 = Actor("herz.png")
herz2.x = 304
herz2.y = 35
herz3 = Actor("herz.png")
herz3.x = 344
herz3.y = 35

reset_game()

zurücksetzen()  
pgzrun.go()
gumichele