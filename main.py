import random
import sys
import pygame
from pygame.locals import *

screensize = (800,600)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()
frame = pygame.time.Clock()
text = pygame.font.SysFont("comicsansms",20,True,True)

class Entity:
    def __init__(self,tagname,size):
        self.tagname = tagname
        self.x = 0
        self.y = 0
        self.size =  size
        self.color = (255,255,255)
        self.speed = 5

    def detectInputMove(self):
        if pygame.key.get_pressed()[K_d]:
            self.x +=self.speed
        if pygame.key.get_pressed()[K_a]:
            self.x -=self.speed    
        if pygame.key.get_pressed()[K_w]:
            self.y -=self.speed
        if pygame.key.get_pressed()[K_s]:
            self.y +=self.speed                        

entities = []

collisionTimes = 0

player = Entity("Player",20)

enemy = Entity("Enemy", 20)
enemy.color = (255,0,0)
enemy.x = enemy.y = 200
#print(pygame.font.get_fonts())

while True:
    frame.tick(60)
    gameScreen.fill((0,0,0))

    #for i in range(0,len(entities)):
    #    pygame.draw.rect(gameScreen,entities[i].color,(entities[i].x,entities[i].y,entities[i].size,entities[i].size))
    

    message = f'collisions: {collisionTimes}'
    formatedText = text.render(message, True, (255,255,255))

    player_body = pygame.draw.rect(gameScreen,player.color,(player.x,player.y,player.size,player.size))
    enemy_body = pygame.draw.rect(gameScreen,enemy.color,(enemy.x,enemy.y,enemy.size,enemy.size))

    
    if player_body.colliderect(enemy_body):
        collisionTimes += 1
        enemy.x = random.randint(0,800-20)
        enemy.y = random.randint(0,600-20)

    player.detectInputMove()
    gameScreen.blit(formatedText, (0,0))

    for event in pygame.event.get():   
        

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()
    pygame.display.update()
    