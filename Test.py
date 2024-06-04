import pgzrun

WIDTH = 800
HEIGHT = 600

# Figur initialisieren
character = Actor('fairyforgame.png', (WIDTH // 2, HEIGHT - 50))

# Physik-Variablen
jumpstart = 0
jumping = False

def draw():
    screen.clear()
    character.draw()

def update():
    global jumpstart, jumping

    # Sprunglogik
    if keyboard.space and not jumping:
        jumpstart = -10
        jumping = True
    
    # Schwerkraft anwenden
    character.y += jumpstart
    jumpstart += 0.5
    
    # Boden berühren
    if character.y >= HEIGHT - 50:
        character.y = HEIGHT - 50
        jumpstart = 0
        jumping = False

    # Links und rechts bewegen
    if keyboard.left:
        character.x -= 5
    if keyboard.right:
        character.x += 5

    # Bildschirmgrenzen prüfen
    character.x = max(0, min(WIDTH, character.x))

pgzrun.go()
