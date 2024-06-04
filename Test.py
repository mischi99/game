import pgzrun

WIDTH = 800
HEIGHT = 600

# Figur initialisieren
character = Actor('fairyforgame.png', (WIDTH // 2, HEIGHT - 50))

# Physik-Variablen
jump.y = 0
jumping = False
gravity = 0.5
jump_power = -10

def draw():
    screen.clear()
    character.draw()

def update():
    global jump.y, jumping
    
    # Sprunglogik
    if keyboard.space and not jumping:
        jump = jump_power
        jumping = True
    
    # Schwerkraft anwenden
    jump.y += gravity
    character.y += velocity_y
    
    # Boden berühren
    if character.y >= HEIGHT - 50:
        character.y = HEIGHT - 50
        jump.y = 0
        jumping = False

    # Links und rechts bewegen
    if keyboard.left:
        character.x -= 5
    if keyboard.right:
        character.x += 5

    # Bildschirmgrenzen prüfen
    character.x = max(0, min(WIDTH, character.x))

pgzrun.go()
