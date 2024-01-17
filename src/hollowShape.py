from pymunk import Vec2d, Space, Body, Segment
from pygame import gfxdraw

class hollowShape:
    def __init__(self, space: Space, position: Vec2d, lines, color=(255, 255, 255)):
        self.body = Body(body_type=Body.STATIC)
        self.body.position = position
        self.segmentList = []
        self.color = color
        self.lines = lines
        

        for line in lines:
            tmpSeg = Segment(self.body, line[0],line[1], 1.0)
            tmpSeg.elasticity = 1.0
            tmpSeg.friction = 0.0
            tmpSeg.collision_type = 0
            self.segmentList.append(tmpSeg)
        space.add(*self.segmentList, self.body)

    def draw(self, screen):
        gfxdraw.filled_polygon(screen, [self.body.local_to_world(x[0]) for x in self.lines] + [self.body.local_to_world(self.lines[len(self.lines)-1][1])], self.color)
        gfxdraw.aapolygon(screen, [self.body.local_to_world(x[0]) for x in self.lines] + [self.body.local_to_world(self.lines[len(self.lines)-1][1])], self.color)