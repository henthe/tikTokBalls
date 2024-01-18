from pymunk import Vec2d, Space, Body, Segment
from pygame import gfxdraw, draw
from utils import generateVerticesFromPoints, generateLinesFromVertices
import math 
from math import pi

class hollowShape:
    def __init__(self, space: Space, position: Vec2d, numberSides:int, innerRadius:int, color=(255, 255, 255)):
        self.space = space
        self.body = Body(body_type=Body.STATIC)
        self.body.position = position
        self.segmentList = []
        self.color = color
        self.numberSides = numberSides
        self.innerRadius = innerRadius
        
        self.regenerate()
        

    def regenerate(self):
        if self.space.shapes:
            self.space.remove(*self.segmentList)
            self.segmentList = []
        tmpPos = self.body.position
        if self.space.bodies:
            self.space.remove(self.body)
            self.body = Body(body_type=Body.STATIC)
            self.body.position = tmpPos
            
        outerRadius = self.innerRadius + 30
        self.lines = generateLinesFromVertices(generateVerticesFromPoints(self.innerRadius, outerRadius, self.numberSides))
        
        for line in self.lines:
            tmpSeg = Segment(self.body, line[0],line[1], 1.0)
            tmpSeg.elasticity = 1.0
            tmpSeg.friction = 0.0
            tmpSeg.collision_type = 0
            self.segmentList.append(tmpSeg)
        self.space.add(*self.segmentList, self.body)

    def getIncircleRadius(self): 
        return self.innerRadius * math.cos(pi/self.numberSides)
        


    def draw(self, screen):
        gfxdraw.filled_polygon(screen, [self.body.local_to_world(x[0]) for x in self.lines] + [self.body.local_to_world(self.lines[len(self.lines)-1][1])], self.color)
        gfxdraw.aapolygon(screen, [self.body.local_to_world(x[0]) for x in self.lines] + [self.body.local_to_world(self.lines[len(self.lines)-1][1])], self.color)

        