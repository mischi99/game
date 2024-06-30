import pygame.mixer
import os
os.environ["SDL_VIDEO_CENTERED"] = "0, 0"

import random
import time
import pgzrun

WIDTH = 1920
HEIGHT = 985
TITLE = "Informatik Projekt - Designed by Lynn and Michèle"

#squirrel
squirrel = Actor("squirrel.png")
squirrel.x = 400
squirrel.y = 775

#squirrel intro1
squirrelintro1 = Actor("squirrel.png")
squirrelintro1.x = 500
squirrelintro1.y = 775

#squirrelmirrored
squirrelmirrored = Actor("squirrelmirrored.png")
squirrelmirrored.x = 1700
squirrelmirrored.y = 775

#speech bubble
speechbubble = Actor("speechbubble.png")
speechbubble.x = 650
speechbubble.y = 600

#speech bubble intro 1
speechbubbleintro1 = Actor("speechbubble.png")
speechbubbleintro1.x = 750
speechbubbleintro1.y = 600

#speech bubble mirrored
speechbubblemirrored = Actor("speechbubblemirrored.png")
speechbubblemirrored.x = 600
speechbubblemirrored.y = 600

#speech bubble troll
speechbubblet = Actor("speechbubble.png")
speechbubblet.x = 1250
speechbubblet.y = 500

#background
background = Actor("forestbackground.jpg")
background.x = 0
background1 = Actor("forestbackground1.jpg")
background1.x = WIDTH

bridge1 = Actor("bridge5-org.png")
bridge1.x = 1000
bridge2 = Actor ("bridge5.1-org.png")
bridge2.x = 1000
bridge3 = Actor("bridge6.1-org.png")
bridge3.x = 2920
bridge4 = Actor("bridge6-org.png")
bridge4.x = 2920
bridge5 = Actor("bridge7-org.png")
bridge5.x = 2920 + 1920
bridge6 = Actor("bridge7.1-org.png")
bridge6.x = 2920 + 1920
bridge7 = Actor("bridge7-org.png")
bridge7.x = 2920 + 1920 + 1920
bridge8 = Actor("bridge7.1-org.png")
bridge8.x = 2920 + 1920 + 1920

fairy = Actor("frame-022.gif")
fairy.x = 100
fairy.y = 500
fairy.life = 3

fairy1 = Actor("fairy1.png")
fairy1.x = 800 
fairy1.y = 700

ghost = Actor("ghost1.png")
ghost.x = 400
ghost.y = 660

lightningfull = Actor("lightningfull.png")
lightningfull.x = random.randrange(WIDTH)
lightningfull.y = random.randrange(HEIGHT)

activelightning = False
timelightning = 0
powerupnumber = 0

#Stern
star = Actor ("starforgametiny.png")
star.x = random.randrange(WIDTH)
star.y = random.randrange(HEIGHT)

activestar = False
timestar = 0
starcounter = 0

#intro
introfinished0 = False
introfinished1 = False
introfinished2 = False
introfinished3 = False
introfinished4 = False

#start
startgame = False
starttext = False

#zurückgelegte distanz
distance = 0

#life
fairy.life = 3

#gameover
gameover = False

def music():
    music = pygame.mixer.music.load('magicalFantasy.mp3') #die Musik-Datei wird geladen, damit sie anschliessend abgespielt werden kann
    pygame.mixer.music.play(-1) #spielt die geladene Musik ab, in diesem Fall unbestimmt lange. (2) würde bedeuten, das die Musik 2x hintereinander abgespielt wird

def draw():
    global powerupnumber, starcount, startgame
    
    screen.clear() #damit nur immer ein Bild dort ist und nicht übereindander, da sonst beim weiterdrücken ein teil des hinteren bildes noch zu sehen ist.
    background.draw()
    background1.draw()
    bridge1.draw()
    bridge4.draw()
    bridge6.draw()
    bridge8.draw()
    fairy.draw()
    
    ghost.draw()
    
    changecostume()
    bridge2.draw()
    bridge3.draw()
    bridge5.draw()
    bridge7.draw()
    
    lightningfull.draw()
    screen.blit("lightningfullblack.png", (1800, 50))
    screen.blit("lightninghalffullblack.png", (1750, 50))
    screen.blit("lightningalmostemptyblack.png", (1700, 50))
    screen.blit("lightningemptyblack.png", (1650, 50))
    
    if powerupnumber == 0:
        screen.blit("lightningempty.png", (1650, 50))
        
    elif powerupnumber == 1:
        screen.blit("lightningempty.png", (1650, 50))
        screen.blit("lightningalmostempty.png", (1700, 50))
        
    elif powerupnumber == 2:
        screen.blit("lightningempty.png", (1650, 50))
        screen.blit("lightningalmostempty.png", (1700, 50))
        screen.blit("lightninghalffull.png", (1750, 50))
    
    elif powerupnumber == 3:
        screen.blit("lightningempty.png", (1650, 50))
        screen.blit("lightningalmostempty.png", (1700, 50))
        screen.blit("lightninghalffull.png", (1750, 50))
        screen.blit("lightningfull.png", (1800, 50))
        screen.draw.text("press the spacebar", left=WIDTH/2 - 180, top=HEIGHT/2, fontsize=60, color=(255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center")

        if keyboard.space: # Wenn die Leertaste  gedrückt wird, setze die Blitzsymbole zurück
            powerupnumber = 0
            powerupactive = True
    
    #anzahl eingesammelte Sternen
    star.draw()
    screen.draw.text(str(starcounter), (85, 35), fontsize=40, color=(255, 255, 255))
    screen.blit("starforgametiny.png", (20, 20))
    
    #zurückgelegte Strecke
    screen.draw.text(f"Zurückgelegte Strecke: {distance/100} m", (20, 80), fontsize=40, color=(255, 255, 255))
   
    if not introfinished0:
        screen.fill((0, 0, 0)) #füllt hintergrund schwarz aus
        screen.blit("arrowblack", (1770, 835))
        screen.draw.text("Wings of the Night", left=700, top=450, fontsize=80, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center") #\n macht einen Brake (Zeilenumbruch) in den text
        

    elif not introfinished1: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.fill((0, 0, 0)) #füllt hintergrund schwarz aus
        screen.blit("arrowblack", (1770, 835))
        screen.blit("heart", (890, 300))
        screen.blit("lightningfull", (775, 340))
        screen.blit("starforgametiny.png", (560, 390))
        screen.blit("steering", (760, 550))
        screen.draw.text("Spielanleitung", left=800, top=200, fontsize=60, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center") #\n macht einen Brake (Zeilenumbruch) in den text
        screen.draw.text("= Leben\n= Schnelligkeitszunahme\n= Punkte zähler; Ab 100 Punkten gibt es ein Level up\nSteuerung mit den Pfeilen", left=620, top=300, fontsize=35, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center") #\n macht einen Brake (Zeilenumbruch) in den text
        
    elif not introfinished2: 
        screen.blit("firstbackground6", (0, 0))
        screen.blit("arrowwhite", (1770, 835))
        squirrelintro1.draw()
        screen.blit("firstbackground6.1", (0,0))
        speechbubbleintro1.draw()
        screen.draw.text("Hey, Weisst du, wo\nSparky der Troll steckt?\nHast du ihn gesehen?", left=647, top=545, fontsize=22, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
        
    elif not introfinished3: 
        screen.blit("backgroundnew", (0, 0))
        screen.blit("arrowwhite", (1770, 835))
        fairy1.draw()
        speechbubblemirrored.draw()
        screen.draw.text("Nein, ich habe ihn\nnicht gesehen.\nIch gehe ihn suchen!\n", left=514, top=550, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
        
    elif not introfinished4:
        screen.blit("gamedirections", (0, 0))
        screen.blit("glow", (0, 0))
        screen.blit("glow", (50, 50))
        screen.blit("glow", (-50, -50))
        screen.blit("button", (WIDTH/2, HEIGHT/2))
        screen.draw.text("Starten", left=WIDTH/2, top=HEIGHT/2, fontsize=40, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
    
#     if starcounter == 2:
#         startgame = False
#         gameover()
        
    if startgame == True:    
        if fairy.life >= 3:
            screen.blit("herz1.png", (264, 43))
            screen.blit("herz1.png", (314, 43))
            screen.blit("herz1.png", (364, 43))
        elif fairy.life == 2:
            screen.blit("herz1.png", (264, 43))
            screen.blit("herz1.png", (314, 43))
            screen.blit("herzgrey.png", (364, 43))
        elif fairy.life == 1:
            screen.blit("herz1.png", (264, 43))
            screen.blit("herzgrey.png", (314, 43))
            screen.blit("herzgrey.png", (364, 43))
        elif fairy.life <= 0:
            screen.blit("herzgrey.png", (264, 43))
            screen.blit("herzgrey.png", (314, 43))
            screen.blit("herzgrey.png", (364, 43))    
        
        if fairy.life == 0:
            gameover()
        
def update():
    global introfinished0, introfinished1, introfinished2, introfinished3, introfinished4, startgame, starttext, powerupnumber, gameover, fairy

    if startgame:
        movebridge()
        movebackground()
        movefigure()
        powerup_lightning()
        powerup_star()
        ghostcollision(ghost)  # Hier wird die Funktion für die Kollision zwischen Fee und Geist aufgerufen
        moveghost()

    if fairy.life == 0:
        gameover()
                
def ghostcollision(ghost):
    global fairy
    if fairy.colliderect(ghost):
        fairy.life = fairy.life - 1
        ghost.x = WIDTH  # Setze den Geist auf die rechte Seite des Bildschirms zurück
        ghost.y = random.randint(100, 730)  # Generate a random y-coordinate between 100 and 730
        
    if fairy.life == 3:
        screen.blit("herz1.png", (264, 43))
        screen.blit("herz1.png", (314, 43))
        screen.blit("herz1.png", (364, 43))
    elif fairy.life == 2:
        screen.blit("herz1.png", (264, 43))
        screen.blit("herz1.png", (314, 43))
        screen.blit("herzgrey.png", (364, 43))
    elif fairy.life == 1:
        screen.blit("herz1.png", (264, 43))
        screen.blit("herzgrey.png", (314, 43))
        screen.blit("herzgrey.png", (364, 43))
    elif fairy.life < 1:
        screen.blit("herzgrey.png", (264, 43))
        screen.blit("herzgrey.png", (314, 43))
        screen.blit("herzgrey.png", (364, 43))

def moveghost():
    global ghost

    if fairy.colliderect(ghost):
        fairy.life = fairy.life - 1
        ghost.x = random.randint(0, WIDTH)  # Setze den Geist auf eine zufällige x-Position
        ghost.y = random.randint(100, 730)  # Setze den Geist auf eine zufällige y-Position

    ghost.x = ghost.x - 15
    ghost.bottom = min(ghost.bottom, 730)
    ghost.top = max(ghost.top, 100)

    if ghost.right < 0:  # Wenn die rechte Seite des Geistes den linken Bildschirmrand überschreitet
        ghost.x = WIDTH  # Setze den Geist auf die rechte Seite des Bildschirms zurück
        ghost.y = random.randint(100, 730)  # Generate a random y-coordinate between 100 and 730
        
def movebridge():
    global distance
    bridgespeed = 8
    bridge1.x = bridge1.x - bridgespeed
    bridge2.x = bridge2.x - bridgespeed
    bridge3.x = bridge3.x - bridgespeed
    bridge4.x = bridge4.x - bridgespeed
    bridge5.x = bridge5.x - bridgespeed
    bridge6.x = bridge6.x - bridgespeed
    bridge7.x = bridge7.x - bridgespeed
    bridge8.x = bridge8.x - bridgespeed
    
    distance = distance + 1
    
    if bridge1.right < 0 and bridge2.right < 0 and bridge3.right < 0 and bridge4.right < 0:
        bridge1.x = bridge1.x - WIDTH
        bridge2.x = bridge2.x - WIDTH
        bridge3.x = bridge3.x - WIDTH
        bridge4.x = bridge3.x - WIDTH
        
    if bridge5.right < 0:
        bridge5.left = bridge6.right
    
    if bridge6.right < 0:
        bridge6.left = bridge7.right
    
    if bridge7.right < 0:
        bridge7.left = bridge8.right
    
    if bridge8.right < 0:
        bridge8.left = bridge5.right
           
def movebackground():
    speedbackground = 8
    background.x = background.x - speedbackground
    background1.x = background1.x - speedbackground
    
    if background.right < 0:
        background.left = background1.right
    if background1.right < 0:
        background1.left = background.right

# Kostümwechsel animierte Fairy
def changecostume():
    if fairy.image == "frame-033.gif":
        fairy.image = "frame-034.gif"
        time.sleep(0.1)
                  
    elif fairy.image == "frame-034.gif":
        fairy.image = "frame-035.gif"
        time.sleep(0.1)
        
    elif fairy.image == "frame-035.gif":
        fairy.image = "frame-036.gif"
        time.sleep(0.1)
        
    elif fairy.image == "frame-036.gif":
        fairy.image = "frame-037.gif"
        time.sleep(0.1)
        
    elif fairy.image == "frame-037.gif":
        fairy.image = "frame-038.gif"
        time.sleep(0.1)
        
    elif fairy.image == "frame-038.gif":
        fairy.image = "frame-039.gif"
        time.sleep(0.1)
        
    elif fairy.image == "frame-039.gif":
        fairy.image = "frame-040.gif"
        time.sleep(0.1)
        
    elif fairy.image == "frame-040.gif":
        fairy.image = "frame-041.gif"
        time.sleep(0.1)
            
    else:
        fairy.image = "frame-033.gif"
        time.sleep(0.1)

def movefigure():
    global jumpstart, jumping
    steps = 10
    if keyboard.left:
        fairy.x = fairy.x - steps
    if keyboard.right:
        fairy.x = fairy.x + steps
    if keyboard.up:
        fairy.y = fairy.y - steps
    if keyboard.down:
        fairy.y = fairy.y + steps
    if fairy.left < 0:
        fairy.left = 0
    if fairy.right > WIDTH:
        fairy.right = WIDTH
    if fairy.top < 0:
        fairy.top = 0
    if fairy.bottom > HEIGHT:
        fairy.bottom = HEIGHT
        
    fairy.bottom = min(fairy.bottom, 800)
    
def powerup_lightning():
    global activelightning, timelightning, powerupnumber

    currenttime = time.time()

    if not activelightning and currenttime - timelightning > 5:
        lightningfull.x = 1920
        lightningfull.y = random.randint(100, 730)

        activelightning = True
        timelightning = currenttime

    if fairy.colliderect(lightningfull):
        activelightning = False
        lightningfull.x = -100
        powerupnumber = powerupnumber + 1
        lightningfull.x = WIDTH - 200  # Zurücksetzen der Position des Powerups nach Kollision

    lightningfull.x = lightningfull.x - 5
    lightningfull.bottom = min(lightningfull.bottom, 730)
    lightningfull.top = max(lightningfull.top, 100)

    if lightningfull.right < 0:
        lightningfull.x = WIDTH  # Zurücksetzen der Position des Powerups nach Kollision
        
def powerup_star():
    global activestar, timestar, starcounter

    star.x = star.x - 5
    star.bottom = min(star.bottom, 730)
    star.top = max(star.top, 100)

    currenttime = time.time()

    if not activestar and currenttime - timestar > 5:
        star.x = 1920
        star.y = random.randint(100, 730)  # Generate a random y-coordinate between 100 and 730

        activestar = True
        timestar = currenttime

    if fairy.colliderect(star):
        if fairy.colliderect(star):
            activestar = False
            star.x = -100
            starcounter = starcounter + 1  # Erhöhe die Sternanzahl um 1, wenn ein Stern eingesammelt wird
            star.x = WIDTH - 200  # Zurücksetzen der Position des Sterns nach Kollision
            star.y = random.randint(100, 730)  # Generate a random y-coordinate between 100 and 730

    if star.right < 0:  # Wenn die rechte Seite des Sterns den linken Bildschirmrand überschreitet
        star.x = WIDTH  # Setze den Stern auf die rechte Seite des Bildschirms zurück
        star.y = random.randint(100, 730)  # Generate a random y-coordinate between 100 and 730
        
def on_mouse_down(pos):
    global introfinished0, introfinished1, introfinished2, introfinished3, introfinished4, startgame, gameover
    
    if not introfinished0:
        text_width = 100  # Geschätzte Breite des Textes 
        text_height = 100 # Geschätzte Höhe des Textes 
        if not introfinished0 and 1770 < pos[0] < 1770  + text_width and 835 < pos[1] < 835 + text_height: #liegt der Mausklick zwischen den positionen pos[0] und pos[1]
            introfinished0 = True
            startgame = False
            
    elif not introfinished1:
        text_width = 100  # Geschätzte Breite des Textes 
        text_height = 100 # Geschätzte Höhe des Textes 
        if not introfinished1 and 1770 < pos[0] < 1770  + text_width and 835 < pos[1] < 835 + text_height: #liegt der Mausklick zwischen den positionen pos[0] und pos[1]
            introfinished1 = True
            startgame = False
            
    elif not introfinished2:
        text_width = 100  # Geschätzte Breite des Textes 
        text_height = 100 # Geschätzte Höhe des Textes 
        if not introfinished2 and 1770 < pos[0] < 1770  + text_width and 835 < pos[1] < 835 + text_height: #liegt der Mausklick zwischen den positionen pos[0] und pos[1]
            introfinished2 = True
        
    elif not introfinished3:
        text_width = 100  # Geschätzte Breite des Textes 
        text_height = 100 # Geschätzte Höhe des Textes 
        if not introfinished3 and 1770 < pos[0] < 1770  + text_width and 835 < pos[1] < 835 + text_height: #liegt der Mausklick zwischen den positionen pos[0] und pos[1]
            introfinished3 = True
            
    elif not introfinished4:
        text_width = 80  # Geschätzte Breite des Textes 
        text_height = 40 # Geschätzte Höhe des Textes 
        if not introfinished4 and WIDTH/2 < pos[0] < WIDTH/2 + text_width and HEIGHT/2 < pos[1] < HEIGHT/2 + text_height: #liegt der Mausklick zwischen den positionen pos[0] und pos[1]
            introfinished4 = True
            startgame = True
            
    elif gameover:
        gameover = False
        starttext = False
        startgame = False
        
        text_width = 100  # Geschätzte Breite des Textes 
        text_height = 100 # Geschätzte Höhe des Textes 
        if not gameover and 720 < pos[0] < 720 + text_width and 650 < pos[1] < 650 + text_height: #liegt der Mausklick zwischen den positionen pos[0] und pos[1]
            screen.draw.text("Suuppii", center=(WIDTH/2, HEIGHT/2), color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center")
            reset_game()
        
def reset_game():
    global fairy, powerupnumber, activelightning, activestar, timestar, timelightning, starcounter, distance
    
    fairy.life = 3
    powerupnumber = 0
    activelightning = False
    activestar = False
    timestar = 0
    timelightning = 0
    starcounter = 0
    distance = 0
    
def gameover():
    global fairy, distance
    screen.fill((0, 0, 0))
    screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2 - 100), fontsize=70, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center")
    screen.draw.text(f"Punkte: {starcounter}", center=(WIDTH/2, HEIGHT/2 + 50), fontsize=50, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center")
    screen.draw.text(f"Score: {distance/100} meters", center=(WIDTH/2, HEIGHT/2 + 100), fontsize=50, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center")
    screen.blit("starforgametiny", (WIDTH/2 + 20, HEIGHT/2 + 60))
    screen.blit("replay", (720, 650))
    screen.blit("arrowblack", (1200, 650))
    
music()
pgzrun.go()