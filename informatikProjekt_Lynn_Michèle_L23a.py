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
speechbubblemirrored.x = 1450
speechbubblemirrored.y = 600

#speech bubble troll
speechbubblet = Actor("speechbubble.png")
speechbubblet.x = 1250
speechbubblet.y = 500

#troll
troll = Actor("troll2.png")
troll.x = 1700
troll.y = 775

#provisorisch troll
troll1 = Actor("2150251023-removebg-preview.png")
troll1.x = 1000
troll1.y = 670

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

test = Actor("mensch1.png")
test.x = 100
test.y = 500

lightningfull = Actor("lightningfull.png")
lightningfull.x = random.randrange(WIDTH)
lightningfull.y = random.randrange(HEIGHT)

timelightning = 0
activelightning = False
powerupnumber = 0

#intro
introfinished1 = False
introfinished2 = False
introfinished3 = False
introfinished4 = False

#start
startgame = False
starttext = False

def music():
    music = pygame.mixer.music.load('magicalFantasy.mp3') #die Musik-Datei wird geladen, damit sie anschliessend abgespielt werden kann
    pygame.mixer.music.play(2) #spielt die geladene Musik ab, (2) bedeutet, das die Musik 2x hintereinander abgespielt wird

def draw():
    global powerupnumber
    
    screen.clear() #damit nur immer ein Bild dort ist und nicht übereindander, da sonst beim weiterdrücken ein teil des hinteren bildes noch zu sehen ist.
    background.draw()
    background1.draw()
    
    bridge1.draw()
    bridge4.draw()
    bridge6.draw()
    bridge8.draw()
    test.draw()
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
    
    if starttext and not startgame: #wenn der starttext true ist und das startgame false, nur dann wird der Text angezeigt: also der Starttext soll angezeigt werden, wenn das Game noch nicht gestartet ist.
        white = 255, 255, 255
        screen.draw.text("Spiel beginnen", left=WIDTH/2 - 180, top=HEIGHT/2, fontsize=60, color=(255,255,255), fontname="..\\fonts\\handlee-regular.ttf", align="center", )
        screen.draw.text("press the spacebar!", left=WIDTH/2 -120, top=HEIGHT/2 + 70, fontsize=30, color=white, fontname="..\\fonts\\handlee-regular.ttf", align="center", italic=True, )
    
    if not introfinished1: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("magic", (0, 0)) #fügt hintergrundbild mashrooms ein.
        squirrelintro1.draw()
        screen.blit("magicplant", (0, 0))
        speechbubbleintro1.draw()
        screen.draw.text("Hey, Weisst du,\nwo Elena die Fee steckt?\nHast du sie gesehen?", left=648, top=545, fontsize=22, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
    
    elif not introfinished2: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("firstbackground", (0, 0))
        troll.draw()
        speechbubblemirrored.draw()
        screen.draw.text("Nein, ich habe sie\nnicht gesehen.\nIch gehe sie suchen!\n", left=1365, top=550, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
     
    elif not introfinished3: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("firstbackground", (0, 0))
        squirrel.draw()
        screen.blit("flower", (0, 0)) #mashroom links unten in der Ecke, vor squirrel
        speechbubble.draw()
        screen.draw.text("Okay, ich bleibe hier!\n> Weiter mit x-Taste", left=549, top=570, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
    
    elif not introfinished4: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("jungle", (0, 0))
        troll1.draw()
        speechbubblet.draw()
        screen.draw.text("Los geht's!\n> Weiter mit\ny-Taste", left=1160, top=445, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text

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
            
        elif introfinished1 and introfinished2 and introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
            introfinished1 = True
            introfinished2 = True
            introfinished3 = True
            introfinished4 = True
            startgame = False
            starttext = True
        
    if keyboard.space and introfinished1 and introfinished2 and introfinished3 and not startgame:
        startgame = True #das Intro wird somit beendet
        starttext = False #der Starttext wird somit angezeigt    
   
#     if keyboard.tab and not introfinished1 and not introfinished2 and not introfinished3: #wenn die tabulatortaste gedrückt wird und das intro noch nicht fertig ist dann soll der Starttext noch nicht angezeigt werden.
#         introfinished1 = True #prüft andauernd ob space taste gedrückt wurde, und setzt indiesem Falle den wert introfinished1 bei drücken der Taste auf True, wodurch if not introfinished1 gleich false ist, denn + und - = -
#         introfinished2 = False
#         introfinished3 = False
#         starttext = True
        
#     if keyboard.m and introfinished1 and not introfinished2 and not introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
#         introfinished1 = True
#         introfinished2 = True
#         introfinished3 = False
#         startgame = False
#         starttext = True
        
#     if keyboard.x and introfinished1 and introfinished2 and not introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
#         introfinished1 = True
#         introfinished2 = True
#         introfinished3 = True
#         introfinished4 = False 
#         startgame = False
#         starttext = False
        
#     if keyboard.y and introfinished1 and introfinished2 and introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
#         introfinished1 = True
#         introfinished2 = True
#         introfinished3 = True
#         introfinished4 = True
#         startgame = False
#         starttext = True
        
#     if keyboard.space and introfinished1 and introfinished2 and introfinished3 and not startgame:
#         startgame = True #das Intro wird somit beendet
#         starttext = False #der Starttext wird somit angezeigt

    if startgame:
        movebridge()
        movebackground()
        movefigure()
        powerup()

def movebridge():

    bridge1.x = bridge1.x - 3
    bridge2.x = bridge2.x - 3
    bridge3.x = bridge3.x - 3
    bridge4.x = bridge4.x - 3
    bridge5.x = bridge5.x - 3
    bridge6.x = bridge6.x - 3
    bridge7.x = bridge7.x - 3
    bridge8.x = bridge8.x - 3
        
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
    background.x = background.x -3
    background1.x = background1.x -3
    
    if background.right < 0:
        background.left = background1.right
    if background1.right < 0:
        background1.left = background.right

# Kostümwechsel zwischen mensch1 und mensch2
def kostuemwechseln():
    if test.image == "mensch1.png":
        test.image = "mensch2.png"
#         time.sleep(0)
    else:
        test.image = "mensch1.png"
#         time.sleep(0)

def movefigure():
    if keyboard.left:
        test.x = test.x - 10
    if keyboard.right:
        test.x = test.x + 10
    if keyboard.up:
        test.y = test.y - 10
    if keyboard.down:
        test.y = test.y + 10
    if test.left < 0:
        test.left = 0
    if test.right > WIDTH:
        test.right = WIDTH
    if test.top < 0:
        test.top = 0
    if test.bottom > HEIGHT:
        test.bottom = HEIGHT
        
    test.bottom = min(test.bottom, 730)

def powerup():
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
    
    if test.colliderect(lightningfull):
        activelightning = False
        lightningfull.x = -100
        powerupnumber = powerupnumber + 1

music()
pgzrun.go()