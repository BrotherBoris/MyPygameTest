import random
import sys
import pygame
from pygame.locals import *
import matrix

screenHeight = 500
screenWidth = 500
gameScreen = pygame.display.set_mode((screenHeight,screenWidth))
pygame.display.set_caption("Game")
pygame.init()
frame = pygame.time.Clock()


class particle:
    def __init__(self, pos):
        self.x, self.y = pos
        self.color = (240,230,140)

    def simulate(self):
        pass

class Entity:
    def __init__(self,tagname,size):
        self.tagname = tagname
        self.x = 0
        self.y = 0
        self.size =  size
        self.color = (255,255,255)

    def detectInputMove(self):
        if pygame.key.get_pressed()[K_d]:
            self.x +=1
        if pygame.key.get_pressed()[K_a]:
            self.x -=1    
        if pygame.key.get_pressed()[K_w]:
            self.y -=1
        if pygame.key.get_pressed()[K_s]:
            self.y +=1                        

player = Entity("Player",20)

grains = []

while True:
    frame.tick(60)
    gameScreen.fill((0,0,0))
    player.detectInputMove()

    #for i in range(0,len(grains)):
    #    pygame.draw.rect(gameScreen,grains[i].color,(grains[i].x,grains[i].y,grains[i].size,grains[i].size))
        
    pygame.draw.rect(gameScreen,player.color,(player.x,player.y,player.size,player.size))



    for event in pygame.event.get():   
        

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()

    pygame.display.update()