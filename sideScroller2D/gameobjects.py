import pygame
from pygame.locals import *

class Entity:
    def __init__(self,tagname,size):
        self.tagname = tagname
        self.x = 0
        self.y = 0
        self.size =  size
        self.color = (255,255,255)
        self.speed = 5
        self.fallSpeed = 5
        self.body = None

    def detectInputMove(self):
        if pygame.key.get_pressed()[K_d]:
            self.x +=self.speed
        if pygame.key.get_pressed()[K_a]:
            self.x -=self.speed
     
    def fall(self):
        if self.fallSpeed > 0:
            self.y += self.fallSpeed

    def simulateGravity(self, screenBoundY):
        #if self.y != screenBoundY - self.size:
        #    self.fallSpeed = 5
        if self.y == screenBoundY - self.size:
            self.fallSpeed = 0
        if self.y > screenBoundY - self.size:
            self.y = screenBoundY - self.size
        self.fall()

    def drawnItself(self, screen):
        self.body = pygame.draw.rect(screen,self.color,(self.x,self.y,self.size,self.size))
        
    def enabled(self, screen,screenBoundY):
        self.drawnItself(screen)
        self.detectInputMove()
        self.simulateGravity(screenBoundY)  

class Terrain:
    def __init__(self,pos,size,color):
        self.x, self.y = pos
        self.sizeW, self.sizeH =  size
        self.color = color
        self.body = None
    
    def drawnItself(self, screen):
        self.body = pygame.draw.rect(screen,self.color,(self.x,self.y,self.sizeW,self.sizeH))  

class TerrainList:
    def __init__(self):
        self.terrainlist = []

    def returnAllBodies(self):
        albds=[]
        for i in range(0, len(self.terrainlist)):
            albds.append(self.terrainlist[i].body)
        return albds
        