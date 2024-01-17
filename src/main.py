from random import random
import pygame 
from pygame.time import Clock
from pymunk import Space, Vec2d
from math import pi, sin
import pygame.mixer

#CustomImports
from balls.ball_interface import *
from hollowShape import *
from utils import *
from balls.ball_colored import *



WIDTH = 1920
HEIGHT = 1080
FPS = 144
INNER_RADIUS = 450
NUMBER_BALLS = 1
GRAVITY = 100.0
GROWTH = 0

BOUNCE_SOUND_PATH = "res/sound/bounce.wav"


pygame.init()
pygame.mixer.init()

bounceSound = pygame.mixer.Sound(BOUNCE_SOUND_PATH)

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

space = Space()
space.gravity = (0.0, GRAVITY)

clock = Clock()

balls: Ball_Interface = []
for i in range(NUMBER_BALLS):
    velocity: Vec2d = (sin(random() * 2 * pi)*300,sin(random() * 2 * pi)*300)
    position = randomPointinCircle(INNER_RADIUS-30,WIDTH,HEIGHT)

    balls.append(Ball_Colored(space, 1 , 20, position, velocity = velocity, color = randomColor(), collision_type = i+1))


#Ball-Wall Collision
for i,ball in enumerate(balls):
    handler = space.add_collision_handler(0, i + 1)
    handler.data["ball"] = balls[i]
    handler.data["sound"] = bounceSound
    handler.data["growth"] = GROWTH
    handler.begin = wallCollision

#Ball-Ball Collision
for i in range (NUMBER_BALLS):
    for j in range (i+1, NUMBER_BALLS):
        handler = space.add_collision_handler(i+1, j+1)
        handler.data["ball1"] = balls[i]
        handler.data["ball2"] = balls[j]
        handler.data["sound"] = bounceSound
        handler.begin = ballCollision


hollowShape1 = hollowShape(space, (WIDTH/2, HEIGHT/2), generateLinesFromVertices(generateVerticesFromPoints(INNER_RADIUS, INNER_RADIUS + 30, 10)))


# Run until the user asks to quit
running = True
while running:
   
    # Did the user click the window close button or escape key?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Fill the background with white
    screen.fill((20,20,20))

    dt: float = clock.tick(FPS)/1000
    space.step(dt)

    hollowShape1.draw(screen)
    
    for ball in balls:
        ball.draw(screen)
    #space.debug_draw(pymunk.pygame_util.DrawOptions(screen))
    pygame.display.set_caption("fps: " + str(clock.get_fps()))

    # Flip the display
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()