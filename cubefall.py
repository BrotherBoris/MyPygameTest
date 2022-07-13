"""
Cube fall

-cube cannot be faster tha 1 int per loop
-clipping can be avoided with a preentive calculation


"""
import random
import time
import pygame

screensize = (800,600)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()

x=0
y=0
newColor = (0,255,0)

class cube:
    def __init__(self, size):
        self.X = 0
        self.Y = 0
        self.Size = size

    def reposition(self,pos):
        x,y=pos
        self.X = x
        self.Y = y

    def randomizeColor():
        pass
    
    def moveItself(self, boundX, boundY):
        if self.X != boundX-self.Size:
            self.X+=1
        if self.Y != boundY-self.Size:
            self.Y+=1
        if self.X == boundX-self.Size and self.Y == boundY-self.Size:
            self.reposition((random.randint(0,200),random.randint(0,200)))
        

cube1 = cube(40)
cube2 = cube(20)

while True:
    for event in pygame.event.get():   

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()

    if x != 800-40:
        x+=1
    if y != 600-40:
        y+=1

    cube1.moveItself(800,600)
    cube2.moveItself(800,600)

    if x >= 800-40 and y >= 600-40:
        x=random.randint(0,200)
        y=random.randint(0,200)
        newColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print(newColor)

    gameScreen.fill((0,0,0))
    pygame.draw.rect(gameScreen, newColor, (x,y,40,40))

    pygame.draw.rect(gameScreen,(0,10,100),(cube1.X,cube1.Y,cube1.Size,cube1.Size))
    pygame.draw.rect(gameScreen,(0,255,100),(cube2.X,cube2.Y,cube2.Size,cube2.Size))

    pygame.display.update()
    time.sleep(0.01)
    