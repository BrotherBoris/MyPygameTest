import random
import sys
import pygame
from pygame.locals import *

screensize = (800,600)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()
frame = pygame.time.Clock()


class Entity:
    def __init__(self,tagname,size):
        self.tagname = tagname
        self.x = 0
        self.y = 0
        self.size =  size
        self.color = (255,255,255)

    def detectInputMove(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_d:
                self.x +=1
            if event.key == K_a:
                self.x -=1
            if event.key == K_w:
                self.y -=1
            if event.key == K_s:
                self.y +=1

entities = []

player = Entity("Player",20)

while True:
    gameScreen.fill((0,0,0))
    frame.tick(60)

    #for i in range(0,len(entities)):
    #    pygame.draw.rect(gameScreen,entities[i].color,(entities[i].x,entities[i].y,entities[i].size,entities[i].size))
        
    pygame.draw.rect(gameScreen,player.color,(player.x,player.y,player.size,player.size))

    pygame.display.update()

    for event in pygame.event.get():   
        
        player.detectInputMove(event)

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()
    