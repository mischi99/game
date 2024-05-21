111
import pygame.mixer
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "0, 35"

import pgzrun
WIDTH = 1920
HEIGHT = 985
TITLE = "Informatik Projekt - Designed by Lynn and Michèle"

#squirrel
squirrel = Actor("squirrel1.png")
squirrel.x = 400
squirrel.y = 775

#speech bubble
speechbubble = Actor("speechbubble.png")
speechbubble.x = 650
speechbubble.y = 600

#background
background = Actor("background.jpg")
background.x = 0
background1 = Actor("background1.jpg")
background1.x = WIDTH

introfinished = False
startgame = False
starttext = False

def music():
    music = pygame.mixer.music.load('magicalFantasy.mp3') #die Musik-Datei wird geladen, damit sie anschliessend abgespielt werden kann
    pygame.mixer.music.play(2) #spielt die geladene Musik ab, (2) bedeutet, das die Musik 2x hintereinander abgespielt wird

def draw():
    screen.clear() #damit nur immer ein Bild dort ist und nicht übereindander, da sonst beim weiterdrücken ein teil des hinteren bildes noch zu sehen ist.
    background.draw()
    background1.draw()
            
    if starttext and not startgame: #wenn der starttext true ist und das startgame false, nur dann wird der Text angezeigt: also der Starttext soll angezeigt werden, wenn das Game noch nicht gestartet ist.
        white = 255, 255, 255
        screen.draw.text("Spiel beginnen", left=WIDTH/2 - 180, top=HEIGHT/2, fontsize=60, color=white, fontname="C:\\githubprojects\\game\\fonts\\handlee-regular.ttf", align="center", )
        screen.draw.text("press the spacebar!", left=WIDTH/2 -120, top=HEIGHT/2 + 70, fontsize=30, color=white, fontname="C:\\githubprojects\\game\\fonts\\handlee-regular.ttf", align="center", italic=True, )
    
    if not introfinished: #prüft ob not introfinished gleich false ist, was in diesem Fall stimmt --> not introfinished wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("firstbackground", (0, 0)) #fügt hintergrundbild mashrooms ein.
        squirrel.draw()
        screen.blit("flower", (0, 0)) #mashroom links unten in der Ecke, vor squirrel
        speechbubble.draw()
        black = 0, 0, 0
        screen.draw.text("Hey!\n> Weiter mit\nTabulatortaste :)", left=575, top=550, fontsize=23, color=black, fontname="C:\\githubprojects\\game\\fonts\\handlee-regular.ttf", align="left") #\n macht einen Brake (Zeilenumbruch) in den text
    
    
def update():
    global introfinished, startgame, starttext #damit das False der Variable introfinished, stargame und starttext überschrieben werden darf
    
    if keyboard.tab and not introfinished: #wenn die tabulatortaste gedrückt wird und das intro noch nicht fertig ist dann soll der Starttext noch nicht angezeigt werden.
        introfinished = True #prüft andauernd ob space taste gedrückt wurde, und setzt indiesem Falle den wert introfinished bei drücken der Taste auf True, wodurch if not introfinished gleich false ist, denn + und - = -
        starttext = True
        
    if keyboard.space and introfinished and not startgame: # wenn die Leertaste gedrückt wird und das intro fertig ist, jedoch das game nch nicht gestartet wurde, soll der Starttext angezeigt werden
        startgame = True #das Intro wird somit beendet
        starttext = False #der Starttext wird somit angezeigt
        
    if startgame:
        movebackground()
        
def movebackground():
    background.x = background.x -3  #bewegt den Hintergrund um 5 Pixel nach links --> erzeugen des Laufeffekts
    background1.x = background1.x -3
    
    if background.right < 0:  #wenn der Hintergrund aus dem Bild heraus ist
        background.left = background1.right  #setzt ihn wieder zurück auf die rechte Seite des Bildschirms --> so entsteht eine Dauerschleife
    if background1.right < 0:
        background1.left = background.right

music()
pgzrun.go()