"""
Cube fall

-cube cannot be faster tha 1 int per loop
-clipping can be avoided with a preentive calculation

_mouseclick for spawning


"""
import random
import time
import pygame

screensize = (800,600)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()

class cube:
    def __init__(self, size):
        self.Size = size
        self.X = 799-self.Size
        self.Y = 599-self.Size
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def reposition(self,pos):
        x,y=pos
        self.X = x
        self.Y = y
        self.randomizeColor()

    def randomizeColor(self):
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    def moveItself(self, boundX, boundY):
        if self.X != boundX-self.Size:
            self.X+=1
        if self.Y != boundY-self.Size:
            self.Y+=1
        if self.X == boundX-self.Size and self.Y == boundY-self.Size:
            self.reposition((random.randint(0,400),random.randint(0,1)))
        

def createCube():
    cubex = cube(20)
    return cubex

cube1 = cube(20)
cube2 = cube(20)
cube3 = cube(20)
cube4 = cube(20)

cubes = [cube1, cube2, cube3, cube4]

while True:
    for event in pygame.event.get():   

        if event.type == pygame.MOUSEBUTTONDOWN:
            cubes.append(createCube())

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()

    #cube1.moveItself(800,600)
    #cube2.moveItself(800,600)
    #cube3.moveItself(800,600)
    #cube4.moveItself(800,600)

    gameScreen.fill((0,0,0))

    for i in range(0,len(cubes)):
        pygame.draw.rect(gameScreen,cubes[i].color,(cubes[i].X,cubes[i].Y,cubes[i].Size,cubes[i].Size))
        cubes[i].moveItself(800,600)


    #pygame.draw.rect(gameScreen,cube1.color,(cube1.X,cube1.Y,cube1.Size,cube1.Size))
    #pygame.draw.rect(gameScreen,cube2.color,(cube2.X,cube2.Y,cube2.Size,cube2.Size))
    #pygame.draw.rect(gameScreen,cube3.color,(cube3.X,cube3.Y,cube3.Size,cube3.Size))
    #pygame.draw.rect(gameScreen,cube4.color,(cube4.X,cube4.Y,cube4.Size,cube4.Size))

    pygame.display.update()
    time.sleep(0.01)
    