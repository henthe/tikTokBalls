
from random import random
from math import sqrt, pi, cos, sin
import pygame.mixer


def randomPointinCircle(radius, WIDTH, HEIGHT):
    r = sqrt(random()) * radius
    theta = random() * 2 * pi
    x = r * cos(theta)
    y = r * sin(theta)
    x += WIDTH/2
    y += HEIGHT/2
    return (x, y)

def PointsInCircum(r,n=100):
    return [(cos(2*pi/n*x)*r,sin(2*pi/n*x)*r) for x in range(0,n+1)]

def generateVerticesFromPoints(innerRadius, outerRadius, numberOfPoints):
    return PointsInCircum(outerRadius, numberOfPoints) + PointsInCircum(innerRadius, numberOfPoints)[::-1]
  
def generateLinesFromVertices(vertices):
    lines = []
    for i in range(len(vertices)-1):
        lines.append((vertices[i], vertices[i+1]))
    return lines
    
def randomColor():
    return (random()*255, random()*255, random()*255)


#Collision Handlers
def wallCollision(arbiter, space, data):
    data["ball"].shape.unsafe_set_radius(data["ball"].shape.radius + data["growth"])
    pygame.mixer.Sound.play(data["sound"])
    #data["hollowShape"].numberSides += 1
    #data["hollowShape"].regenerate()
    return True

def ballColoredCollision(arbiter, space, data):
    
    pygame.mixer.Sound.play(data["sound"])
    ball1 = data["ball1"]
    ball2 = data["ball2"]
    rand = random()
    if rand > 0.5:
        ball1.updateColor(ball2.color)
    else:
        ball2.updateColor(ball1.color)
    return True

def ballImageCollision(arbiter, space, data):
    
    pygame.mixer.Sound.play(data["sound"])
    ball1 = data["ball1"]
    ball2 = data["ball2"]
    rand = random()
    if rand > 0.5:
        ball1.updateImage(ball2.image)
    else:
        ball2.updateImage(ball1.image)
    return True



def loadImage(path):
    return pygame.image.load(path).convert_alpha()
