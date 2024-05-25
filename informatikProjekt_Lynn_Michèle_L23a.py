import pygame.mixer
import os
os.environ["SDL_VIDEO_CENTERED"] = "0, 35"
os.environ["SDL_VIDEO_FULLSCREEN_DISPLAY"] = "0"

import pgzrun
WIDTH = 1920
HEIGHT = 985
TITLE = "Informatik Projekt - Designed by Lynn and Michèle"

#squirrel
squirrel = Actor("squirrel.png")
squirrel.x = 400
squirrel.y = 775

#squirrelmirrored
squirrelmirrored = Actor("squirrelmirrored.png")
squirrelmirrored.x = 1700
squirrelmirrored.y = 775

#speech bubble
speechbubble = Actor("speechbubble.png")
speechbubble.x = 650
speechbubble.y = 600

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

hhaa = Actor("bridgenewnew.png")
hhaa.x = 0
hhaa1 = Actor("bridgenewnewvorne.png")
hhaa2 = Actor("bridgenewnew.png")
hhaa1.x = WIDTH


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
    screen.clear() #damit nur immer ein Bild dort ist und nicht übereindander, da sonst beim weiterdrücken ein teil des hinteren bildes noch zu sehen ist.
    background.draw()
    background1.draw()
    hhaa2.draw()
    squirrel.draw()
    hhaa1.draw()
    
            
    if starttext and not startgame: #wenn der starttext true ist und das startgame false, nur dann wird der Text angezeigt: also der Starttext soll angezeigt werden, wenn das Game noch nicht gestartet ist.
        white = 255, 255, 255
        screen.draw.text("Spiel beginnen", left=WIDTH/2 - 180, top=HEIGHT/2, fontsize=60, color=white, fontname="..\\fonts\\handlee-regular.ttf", align="center", )
        screen.draw.text("press the spacebar!", left=WIDTH/2 -120, top=HEIGHT/2 + 70, fontsize=30, color=white, fontname="..\\fonts\\handlee-regular.ttf", align="center", italic=True, )
    
    if not introfinished1: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("firstbackground", (0, 0)) #fügt hintergrundbild mashrooms ein.
        squirrel.draw()
        screen.blit("flower", (0, 0)) #mashroom links unten in der Ecke, vor squirrel
        speechbubble.draw()
        screen.draw.text("Hey, Weisst du, wo Elena die Fee steckt, hast du sie gesehen?\n> Weiter mit\nTabulatortaste :)", left=575, top=550, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
    
    elif not introfinished2: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("firstbackground", (0, 0))
        troll.draw()
        speechbubblemirrored.draw()
        screen.draw.text("Nein, ich habe sie nicht gesehen, ich gehe sie suchen!\n> Weiter mit\nm-Taste", left=1375, top=550, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
     
    elif not introfinished3: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("firstbackground", (0, 0))
        squirrel.draw()
        speechbubble.draw()
        screen.draw.text("Okay ich bleibe hier!\n> Weiter mit\nx-Taste", left=575, top=550, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
    
    elif not introfinished4: #prüft ob not introfinished1 gleich false ist, was in diesem Fall stimmt --> not introfinished1 wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("jungle", (0, 0))
        troll1.draw()
        speechbubblet.draw()
        screen.draw.text("...", left=575, top=550, fontsize=23, color= (0,0,0), fontname="..\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text

def update():
    global introfinished1, introfinished2, introfinished3, introfinished4, startgame, starttext #damit das False der Variable introfinished1, stargame und starttext überschrieben werden darf
    
    if keyboard.tab and not introfinished1 and not introfinished2 and not introfinished3: #wenn die tabulatortaste gedrückt wird und das intro noch nicht fertig ist dann soll der Starttext noch nicht angezeigt werden.
        introfinished1 = True #prüft andauernd ob space taste gedrückt wurde, und setzt indiesem Falle den wert introfinished1 bei drücken der Taste auf True, wodurch if not introfinished1 gleich false ist, denn + und - = -
        introfinished2 = False
        introfinished3 = False
        starttext = True
        
    if keyboard.m and introfinished1 and not introfinished2 and not introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
        introfinished1 = True
        introfinished2 = True
        introfinished3 = False
        startgame = False
        starttext = True
        
    if keyboard.x and introfinished1 and introfinished2 and not introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
        introfinished1 = True
        introfinished2 = True
        introfinished3 = True
        introfinished4 = False 
        startgame = False
        starttext = False
        
    if keyboard.y and introfinished1 and introfinished2 and introfinished3 and not introfinished4 and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
        introfinished1 = True
        introfinished2 = True
        introfinished3 = True
        introfinished4 = True
        startgame = False
        starttext = True
        
    if keyboard.space and introfinished1 and introfinished2 and introfinished3 and not startgame:
        startgame = True #das Intro wird somit beendet
        starttext = False #der Starttext wird somit angezeigt

    if startgame:
        movebackground()
        
def movebackground():
    background.x = background.x -3
    background1.x = background1.x -3
    
    if background.right < 0:
        background.left = background1.right
    if background1.right < 0:
        background1.left = background.right
    
    hhaa1.x = hhaa1.x -3
    hhaa2.x = hhaa2.x -3
    
    if hhaa1.right < 0:
        hhaa1.left = hhaa2.right
    if hhaa2.right < 0:
        hhaa2.left = hhaa1.right
music()
pgzrun.go()