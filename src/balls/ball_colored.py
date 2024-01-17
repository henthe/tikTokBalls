from balls.ball_interface import *

class Ball_Colored(Ball_Interface):
    def __init__(self, space: Space, mass: int, radius: int, position: Vec2d, velocity: Vec2d = (0.0,0.0), color=(255, 255, 255),
                darkerGrade: float = 0.7, outlineRadius: float = 0.8, collision_type=0):

        super().__init__(space, mass, radius, position, velocity, collision_type)

        
        self.darkerGrade = darkerGrade
        self.outlineRadius = outlineRadius
        self.color = color
        self.updateColor(color)

    def updateColor(self, color):
        self.color = color
        self.darkerColor = (color[0] * self.darkerGrade, color[1] * self.darkerGrade, color[2] * self.darkerGrade)

    def draw(self, screen):
        localx = int(self.body.position.x)
        localy = int(self.body.position.y)
        localr = int(self.shape.radius)
        gfxdraw.filled_circle(screen, localx, localy, localr, self.color)
        gfxdraw.aacircle(screen, localx, localy, localr, self.color)
        gfxdraw.filled_circle(screen, localx, localy, int(self.shape.radius * self.outlineRadius), self.darkerColor)
        gfxdraw.aacircle(screen, localx, localy, int(self.shape.radius * self.outlineRadius), self.darkerColor)