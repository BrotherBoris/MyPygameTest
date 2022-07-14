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

    def detectInputMove(self):
        if pygame.key.get_pressed()[K_d]:
            self.x +=1
        if pygame.key.get_pressed()[K_a]:
            self.x -=1    
        if pygame.key.get_pressed()[K_w]:
            self.y -=1
        if pygame.key.get_pressed()[K_s]:
            self.y +=1                        

entities = []

player = Entity("Player",20)

enemy = Entity("Enemy", 20)
enemy.color = (255,0,0)
enemy.x = enemy.y = 200

while True:
    frame.tick(60)
    gameScreen.fill((0,0,0))

    #for i in range(0,len(entities)):
    #    pygame.draw.rect(gameScreen,entities[i].color,(entities[i].x,entities[i].y,entities[i].size,entities[i].size))
        
    player_body = pygame.draw.rect(gameScreen,player.color,(player.x,player.y,player.size,player.size))
    enemy_body = pygame.draw.rect(gameScreen,enemy.color,(enemy.x,enemy.y,enemy.size,enemy.size))

    
    if player_body.colliderect(enemy_body):
        enemy.x = random.randint(0,800-20)
        enemy.y = random.randint(0,600-20)

    player.detectInputMove()

    for event in pygame.event.get():   
        

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()
    pygame.display.update()
    