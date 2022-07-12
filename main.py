import random
import pygame
import sys

screensize = (800,600)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()

wheelRotation = 0
  


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            wheelRotation +=1
            print(wheelRotation)

        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if x > 200 and x<600 :
                pygame.mouse.set_pos(601,y)
            

        if event.type == pygame.QUIT:
            pygame.quit()
            
            exit()
            
    pygame.display.update()    
    