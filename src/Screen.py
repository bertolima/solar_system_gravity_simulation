import pygame
import os
from src.Sphere import Sphere

def loadImage(path, directory, image):
    return pygame.image.load(os.path.join(path, directory, image))

class Screen:
    def __init__(self):
        self.screen:pygame.Surface = None
        self.running:bool = None
        self.clock:pygame.time.Clock = None
        self.dt = None
        


        sourceFileDir = os.path.dirname(os.path.abspath(__file__))

        self.objectGroups:dict[str, pygame.sprite.Group] = {}
        self.initVariables()
        self.initObjects(sourceFileDir)

    def initVariables(self):
        self.screen = pygame.display.set_mode((800,600))
        self.running = True
        self.clock:pygame.time.Clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000

    def initObjects(self, source):
        self.objectGroups['SUN'] = pygame.sprite.Group()
        self.objectGroups['PLANETS'] = pygame.sprite.Group()
        sunImage = loadImage(source, 'skins', 'sun.png')
        planet1 = loadImage(source, 'skins', 'planet00.png')
        
        sun = Sphere((400,300),pygame.Vector2(0,0), 50, 100, sunImage)
        planet01 = Sphere((600, 300),pygame.Vector2(0,0), 50, 40, planet1)
        self.objectGroups['SUN'].add(sun)
        self.objectGroups['PLANETS'].add(planet01)


    def isRunning(self):
        return self.running

    def poolEvent(self):
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.running = False

    def update(self):
        self.poolEvent()
        self.objectGroups['PLANETS'].update(self.objectGroups['SUN'].sprites()[0], self.dt)

    def render(self):
        self.screen.fill("black")

        self.objectGroups['SUN'].draw(self.screen)
        self.objectGroups['PLANETS'].draw(self.screen)
        
        pygame.display.flip()
        self.dt = self.clock.tick(60) / 1000
