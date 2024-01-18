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
from balls.ball_image import *



WIDTH = 1920
HEIGHT = 1080
FPS = 144
GRAVITY = 100.0
INNER_RADIUS = 450
NUMBER_SIDES = 8
NUMBER_BALLS = 19
GROWTH = 0
BALL_SIZE = 20


BOUNCE_SOUND_PATH = "tikTokBalls/res/sound/bounce.wav"


pygame.init()
pygame.mixer.init()

bounceSound = pygame.mixer.Sound(BOUNCE_SOUND_PATH)

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

space = Space()
space.gravity = (0.0, GRAVITY)

clock = Clock()

hollowShape1 = hollowShape(space, (WIDTH/2, HEIGHT/2), numberSides=NUMBER_SIDES, innerRadius=INNER_RADIUS)

balls: Ball_Interface = []
imagePath = "tikTokBalls/res/images/flags/"
countries = ["de", "fr", "gb", "it", "ru", "us", "dk", "es", "fi", "gr", "hu", "ie", "nl", "no", "pl", "pt", "se", "tr", "ua"]
for i in range(NUMBER_BALLS):
    velocity: Vec2d = (sin(random() * 2 * pi)*300,sin(random() * 2 * pi)*300)
    position = randomPointinCircle(hollowShape1.getIncircleRadius() - BALL_SIZE,WIDTH,HEIGHT)

    countryPath = imagePath + countries[i%len(countries)] + ".png"
    #balls.append(Ball_Colored(space, 1 , 20, position, velocity = velocity, color = randomColor(), collision_type = i+1))
    balls.append(Ball_Image(space, 1 , BALL_SIZE, position,loadImage(countryPath), velocity = velocity, collision_type = i+1))




#Ball-Wall Collision
for i,ball in enumerate(balls):
    handler = space.add_collision_handler(0, i + 1)
    handler.data["ball"] = balls[i]
    handler.data["sound"] = bounceSound
    handler.data["growth"] = GROWTH
    handler.data["hollowShape"] = hollowShape1
    handler.begin = wallCollision

#Ball-Ball Collision
for i in range (NUMBER_BALLS):
    for j in range (i+1, NUMBER_BALLS):
        handler = space.add_collision_handler(i+1, j+1)
        handler.data["ball1"] = balls[i]
        handler.data["ball2"] = balls[j]
        handler.data["sound"] = bounceSound
        handler.begin = ballImageCollision





# Run until the user asks to quit
running = True
while running:
   
    # Did the user click the window close button or escape key?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    i = 1
    ball1 = balls[0]
    while ball1.image == balls[i].image:
        if i == len(balls)-1:
            
            running = False
            break
        i += 1

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
screen.blit(balls[0].image, (WIDTH/2, HEIGHT/2))
pygame.display.flip()
pygame.time.wait(3000)
# Done! Time to quit.
pygame.quit()