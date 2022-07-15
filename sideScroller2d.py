import random
import sys
import pygame
from pygame.locals import *

screenBoundX, screenBoundY =(800,600)
screensize = (screenBoundX,screenBoundY)
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
        self.speed = 5
        self.fallSpeed = 5

    def detectInputMove(self):
        if pygame.key.get_pressed()[K_d]:
            self.x +=self.speed
        if pygame.key.get_pressed()[K_a]:
            self.x -=self.speed
     
    def fall(self):
        if self.fallSpeed > 0:
            self.y += self.fallSpeed

    def simulateGravity(self):
        if self.y != screenBoundY - self.size:
            self.fallSpeed = 5
        if self.y == screenBoundY - self.size:
            self.fallSpeed = 0
        if self.y > screenBoundY - self.size:
            self.y = screenBoundY - self.size
        self.fall()

    def enabled(self):
        self.detectInputMove()
        self.simulateGravity()                  

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
        enemy.x = random.randint(0,screenBoundX-20)
        enemy.y = random.randint(0,screenBoundY-20)

    player.enabled()

    for event in pygame.event.get():   
        

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()
    pygame.display.update()
    