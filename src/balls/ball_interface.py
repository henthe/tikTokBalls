from pymunk import Vec2d, Space, Body, Circle, moment_for_circle
from pygame import gfxdraw
from utils import loadImage


class Ball_Interface:
    def __init__(self, space: Space, mass, radius, position: Vec2d, velocity: Vec2d = (0.0,0.0) ,collision_type=0 ):
        
        inertia = moment_for_circle(mass, 0, radius)
        self.body = Body(mass, inertia)
        self.body.velocity = velocity
        self.body.position = position

        self.shape = Circle(self.body, radius)
        self.shape.elasticity = 1.00
        self.shape.friction = 0.0
        self.shape.collision_type = collision_type
 
        space.add(self.body, self.shape)
        
    def draw(self, screen):
        pass