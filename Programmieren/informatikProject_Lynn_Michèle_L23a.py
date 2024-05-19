import pygame.mixer
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "0, 35"

import pgzrun
WIDTH = 1920
HEIGHT = 985

TITLE = "Informatik Projekt - Designed by Lynn and Michèle"


def music():
    music = pygame.mixer.music.load('magicalFantasy.mp3') #die Musik-Datei wird geladen, damit sie anschliessend abgespielt werden kann
    pygame.mixer.music.play(1) #spielt die geladene Musik ab, (2) bedeutet, das die Musik 2x hintereinander abgespielt wird

def draw():
   screen.blit("mashrooms", (0, 0))  #fügt hintergrundbild mashrooms ein.

music()
pgzrun.go()
