import pygame.mixer
import os
os.environ["SDL_VIDEO_CENTERED"] = "0, 35"
os.environ["SDL_VIDEO_FULLSCREEN_DISPLAY"] = "0"

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

#troll
troll = Actor("troll2.png")
troll.x = 850
troll.y = 740

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
# starcount = 0
starcounter = 0

#intro
introfinished1 = False
introfinished2 = False
introfinished3 = False
introfinished4 = False

#start
startgame = False
starttext = False

#hüpfen
jump_speed = -10
gravity = 0.5
jumpstart = 0
jumping = False

#zurückgelegte distanz
distance = 0

def music():
    music = pygame.mixer.music.load('magicalFantasy.mp3') #die Musik-Datei wird geladen, damit sie anschliessend abgespielt werden kann
    pygame.mixer.music.play(2) #spielt die geladene Musik ab, (2) bedeutet, das die Musik 2x hintereinander abgespielt wird

def draw():
    global powerupnumber, starcount
    
    screen.clear() #damit nur immer ein Bild dort ist und nicht übereindander, da sonst beim weiterdrücken ein teil des hinteren bildes noch zu sehen ist.
    background.draw()
    background1.draw()
    
    bridge1.draw()
    bridge4.draw()
    bridge6.draw()
    bridge8.draw()
    fairy.draw()
    kostuemwechseln()
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
   
#     if starttext and not startgame: #wenn der starttext true ist und das startgame false, nur dann wird der Text angezeigt: also der Starttext soll angezeigt werden, wenn das Game noch nicht gestartet ist.
#         white = 255, 255, 255
#         screen.draw.text("Spiel beginnen", left=WIDTH/2 - 180, top=HEIGHT/2, fontsize=60, color=(255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center", )
#         screen.draw.text("press the spacebar!", left=WIDTH/2 -120, top=HEIGHT/2 + 70, fontsize=30, color=white, fontname="..\\fonts\\handlee-regular.ttf", align="center", italic=True, )
#     
    if not introfinished1: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("gamedirections", (0, 0)) #fügt hintergrundbild mashrooms ein.
        screen.draw.text("Spielanleitung", left=800, top=HEIGHT/2 - 50, fontsize=50, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center") #\n macht einen Brake (Zeilenumbruch) in den text
        screen.draw.text("...", left=930, top=HEIGHT/2 + 50, fontsize=30, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center") #\n macht einen Brake (Zeilenumbruch) in den text
        
    elif not introfinished2: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("firstbackground6", (0, 0))
        screen.blit("arrow", (1700, 750))
        squirrelintro1.draw()
        screen.blit("firstbackground6.1", (0,0))
        speechbubbleintro1.draw()
        screen.draw.text("Hey, Weisst du,\nwo Elena die Fee steckt?\nHast du sie gesehen?", left=648, top=545, fontsize=22, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
        
    elif not introfinished3: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("backgroundnew", (0, 0))
        troll.draw()
        speechbubblemirrored.draw()
        screen.draw.text("Nein, ich habe sie\nnicht gesehen.\nIch gehe sie suchen!\n", left=515, top=550, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
        
    elif not introfinished4: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("backgroundtransparent", (0, 0))
        screen.draw.text("Starten", left=WIDTH/2, top=HEIGHT/2, fontsize=40, color= (255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
        
def update():
    global introfinished1, introfinished2, introfinished3, introfinished4, startgame, starttext, powerupnumber #damit das False der Variable introfinished1, stargame und starttext überschrieben werden darf   
     
    if keyboard.tab:
        if not introfinished1 and not introfinished2 and not introfinished3:
            introfinished1 = True #prüft andauernd ob space taste gedrückt wurde, und setzt indiesem Falle den wert introfinished1 bei drücken der Taste auf True, wodurch if not introfinished1 gleich false ist, denn + und - = -
            introfinished2 = False
            introfinished3 = False
            introfinished4 = False
            startgame = False
            starttext = True
            
        elif  introfinished1 and not introfinished2 and not introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
            introfinished1 = True
            introfinished2 = True
            introfinished3 = False
            introfinished4 = False
            startgame = False
            starttext = False
            
        elif introfinished1 and introfinished2 and not introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
            introfinished1 = True
            introfinished2 = True
            introfinished3 = True
            introfinished4 = False 
            startgame = False
            starttext = False                
      
    if startgame:
        movebridge()
        movebackground()
        movefigure()
        powerup_lightning()
        powerup_star()
        jump()
    
    if starcounter == 1:
        startgame = False
               
def movebridge():
    global distance
    bridgespeed = 5
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
    speedbackground = 5
    background.x = background.x - speedbackground
    background1.x = background1.x - speedbackground
    
    if background.right < 0:
        background.left = background1.right
    if background1.right < 0:
        background1.left = background.right

# Kostümwechsel zwischen mensch1 und mensch2
def kostuemwechseln():
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
    
def jump():
    global jumpstart, jumping
    
    if keyboard.m and not jumping:
        jumpstart = jump_speed
        jumping = True

    # Schwerkraft anwenden
    if jumping:
        fairy.y += jumpstart
        jumpstart += gravity

        # Bodenberührung prüfen
        if fairy.y >= 730:
            fairy.y = 730
            jumping = False
            jumpstart = 0

def powerup_lightning():
    global activelightning, timelightning, powerupnumber

    lightningfull.x = lightningfull.x - 5
    lightningfull.bottom = min(lightningfull.bottom, 730)
    lightningfull.top = max(lightningfull.top, 100)
    
    currenttime = time.time() # time.time() Anzahl der Sekunden
    
    if not activelightning and currenttime - timelightning > 10: #10 ist die zeit in Sekunden, danach kommt ein neuer powerup
        lightningfull.x = 1920
        lightningfull.y = random.randrange(HEIGHT)
        
        activelightning = True
        timelightning = currenttime
    
    if fairy.colliderect(lightningfull):
        activelightning = False
        lightningfull.x = -100
        powerupnumber = powerupnumber + 1
        
def powerup_star():
    global activestar, timestar, starcounter

    star.x = star.x - 10
    star.bottom = min(star.bottom, 730)
    star.top = max(star.top, 100)
    
    currenttime = time.time()
    
    if not activestar and currenttime - timestar > 5: 
        star.x = 1920
        star.y = random.randrange(HEIGHT)
        
        activestar = True
        timestar = currenttime
    
    if fairy.colliderect(star):
        if fairy.colliderect(star):
            activestar = False
            star.x = -100
            starcounter = starcounter + 1  # Erhöhe die Sternanzahl um 1, wenn ein Stern eingesammelt wird
            
def on_mouse_down1(pos):
    global introfinished4, startgame
    text_width = 80  # Geschätzte Breite des Textes 
    text_height = 40 # Geschätzte Höhe des Textes 
    if not introfinished4 and WIDTH/2 < pos[0] < WIDTH/2 + text_width and HEIGHT/2 < pos[1] < HEIGHT/2 + text_height: #liegt der Mausklick zwischen den positionen pos[0] und pos[1]
        introfinished4 = True
        startgame = True
          
music()
pgzrun.go()