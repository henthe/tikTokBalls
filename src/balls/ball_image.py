from balls.ball_interface import *
from pygame import Surface, transform
from pygame import gfxdraw

class Ball_Image(Ball_Interface):
    def __init__(self, space: Space, mass: int, radius: int, position: Vec2d, image: Surface, velocity: Vec2d = (0.0,0.0),
                  collision_type=0, outlineRadius: float = 0.9):

        super().__init__(space, mass, radius, position, velocity, collision_type)
        self.image = image
        self.outlineRadius = outlineRadius


    def updateImage(self, image):
        self.image = image

    def draw(self, screen):
        localx = int(self.body.position.x)
        localy = int(self.body.position.y)
        localr = int(self.shape.radius)
        outlineColor = (255,255,255)
        drawimage = transform.scale(self.image, (localr*2 * self.outlineRadius, localr*2 * self.outlineRadius))

        gfxdraw.filled_circle(screen, localx, localy, int(self.shape.radius ), outlineColor)
        gfxdraw.aacircle(screen, localx, localy, int(self.shape.radius), outlineColor)
        screen.blit(drawimage, (localx - localr + (1-self.outlineRadius) * localr, localy - localr + (1-self.outlineRadius) * localr))
        
