import pygame.mixer
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "0, 35"

import pgzrun
WIDTH = 1920
HEIGHT = 985
TITLE = "Informatik Projekt - Designed by Lynn and Michèle"

#squirrel
squirrel = Actor("squirrel1.png")
squirrel.x = 200
squirrel.y = 775

#speech bubble
speechbubble = Actor("speechbubble.png")
speechbubble.x = 450
speechbubble.y = 600

#background
background = Actor("background.png")
background.x = 0
background1 = Actor("background1.png")
background1.x = WIDTH

introfinished = False

def music():
    music = pygame.mixer.music.load('magicalFantasy.mp3') #die Musik-Datei wird geladen, damit sie anschliessend abgespielt werden kann
    pygame.mixer.music.play(2) #spielt die geladene Musik ab, (2) bedeutet, das die Musik 2x hintereinander abgespielt wird

def draw():
    screen.clear() #damit nur immer ein Bild dort ist und nicht übereindander, da sonst beim weiterdrücken ein teil des hinteren bildes noch zu sehen ist.
    background.draw()
    background1.draw()
    if not introfinished: #prüft ob not introfinished gleich false ist, was in diesem Fall stimmt --> not introfinished wird zu True - und - = + daher wird der Code ausgeführt
        screen.blit("mashrooms", (0, 0))  #fügt hintergrundbild mashrooms ein.
        squirrel.draw()
        screen.blit("mashrooms1", (0, 0)) #mashroom links unten in der Ecke, vor squirrel
        speechbubble.draw()
        black = 0, 0, 0
        screen.draw.text("Hallo :)", left=420, top=590, fontsize=30, color=black)
    
    
def update():
    global introfinished #damit das False der Variable introfinished überschrieben werden darf
    if keyboard.space:
      introfinished = True #prüft andauernd ob space taste gedrückt wurde, und setzt indiesem Falle den wert introfinished bei drücken der Taste auf True, wodurch if not introfinished gleich false ist, denn + und - = -
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