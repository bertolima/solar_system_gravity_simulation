import pygame
import math

RADIANS = math.pi/180

class Sphere(pygame.sprite.Sprite):
    def __init__(self, pos, speed, mass, radius, image):
        super().__init__()
        self.radius = radius
        self.speed = speed
        self.mass = mass
        self.image = image
        self.resizeImage()
        self.rect = self.image.get_rect(center=pos)
        self.degree = 1

    def resizeImage(self):
        self.image = pygame.transform.scale(self.image, (self.radius*2, self.radius*2))


    def updatePosition(self, orbit, dt):
        d = math.hypot(self.rect.x - orbit.rect.x, self.rect.y - orbit.rect.y)
        self.rect.x = math.cos((RADIANS*self.degree)) * d
        self.rect.y = math.sin((RADIANS*self.degree)) * d

        self.degree+=1
        if(self.degree>360): self.degree = 0

    def update(self, orbit, dt):
        self.updatePosition(orbit, dt)


    

