import random
import os

from gameobjects import Entity
from gameobjects import Terrain
from gameobjects import TerrainList

import pygame
from pygame.locals import *

screenBoundX, screenBoundY =(800,600)
screensize = (screenBoundX,screenBoundY)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()
frame = pygame.time.Clock()

entities = []

text = pygame.font.SysFont("comicsansms",20,True,True)
collisionTimes = 0

#terrains = TerrainList([Terrain((0,500-20),(100,20),(0,255,255)) ,Terrain((0,500-20),(100,20),(0,255,0)),Terrain((120,500-20),(100,20),(0,100,0))])
terrains = TerrainList()
terrains.terrainlist.append(Terrain((0,200-20),(100,20),(0,255,255)))
terrains.terrainlist.append(Terrain((0,500-20),(100,20),(0,255,0)))
terrains.terrainlist.append(Terrain((120,500-20),(100,20),(0,100,0)))


player = Entity("Player",20)

enemy = Entity("Enemy", 20)
enemy.color = (255,0,0)
enemy.x = enemy.y = 200

while True:
    frame.tick(60)
    gameScreen.fill((0,0,0))

    #for i in range(0,len(entities)):
    #    pygame.draw.rect(gameScreen,entities[i].color,(entities[i].x,entities[i].y,entities[i].size,entities[i].size))
   
    #enemy_body = pygame.draw.rect(gameScreen,enemy.color,(enemy.x,enemy.y,enemy.size,enemy.size))
    #if player_body.colliderect(enemy_body):
    #    enemy.x = random.randint(0,screenBoundX-20)
    #    enemy.y = random.randint(0,screenBoundY-20)
        
    for i in range(0,len(terrains.terrainlist)):
       terrains.terrainlist[i].drawnItself(gameScreen)

    player.enabled(gameScreen, screenBoundY)


    #terrain = pygame.draw.rect(gameScreen,(0,255,0),(0,500-20,100,20))

    #terrain = pygame.draw.rect(gameScreen,(0,100,0),(120,500-20,100,20))

    message = f'fs: {player.fallSpeed}'
    formatedText = text.render(message, True, (255,255,255))
    gameScreen.blit(formatedText, (0,0))
    
    #if player.body.colliderect(terrain):
    #if player.body.collidelist(terrains.returnAllBodies()) != -1:
    #    player.fallSpeed = 0
    #else :
    #    player.fallSpeed = 5
    if player.body.collidepoint(600,0):
        print("worked")


    for event in pygame.event.get():   
        

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()
    pygame.display.update()