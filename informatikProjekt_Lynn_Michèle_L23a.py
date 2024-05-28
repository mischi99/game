import pygame.mixer
import os
os.environ["SDL_VIDEO_CENTERED"] = "0, 35"
os.environ["SDL_VIDEO_FULLSCREEN_DISPLAY"] = "0"

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

bridge1 = Actor("bridge5.png")
bridge1.x = 0
bridge2 = Actor ("bridge5.1.png")
bridge2.x = 0
bridge3 = Actor("bridge6.1.png")
bridge3.x = 1920
bridge4 = Actor("bridge6.png")
bridge4.x = 1920

test = Actor("mensch1.png")
test.x = 100
test.y = 500

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
    
    bridge1.draw()
    bridge4.draw()  
    test.draw()
    kostuemwechseln()
    bridge2.draw()
    bridge3.draw()
    

    if starttext and not startgame: #wenn der starttext true ist und das startgame false, nur dann wird der Text angezeigt: also der Starttext soll angezeigt werden, wenn das Game noch nicht gestartet ist.
        white = 255, 255, 255
        screen.draw.text("Spiel beginnen", left=WIDTH/2 - 180, top=HEIGHT/2, fontsize=60, color=white, fontname="..\\fonts\\handlee-regular.ttf", align="center", )
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
    global introfinished1, introfinished2, introfinished3, introfinished4, startgame, starttext #damit das False der Variable introfinished1, stargame und starttext überschrieben werden darf   
  
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
            
def movebridge():

    bridge1.x = bridge1.x - 3  
    bridge2.x = bridge2.x - 3
    bridge3.x = bridge3.x - 3  
    bridge4.x = bridge4.x - 3
    
    if bridge1.right < 0:
        bridge1.left = bridge3.right
    
    if bridge2.right < 0:
        bridge2.left = bridge4.right
    
    if bridge3.right < 0:
        bridge3.left = bridge1.right
    
    if bridge4.right < 0:
        bridge4.left = bridge2.right
        
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
          
music()
pgzrun.go()