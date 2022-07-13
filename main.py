import pygame

screensize = (800,600)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()

x=0
y=0


while True:
    for event in pygame.event.get():

        pygame.draw.rect(gameScreen, (0,255,0), (0,0,40,40))
            

        if event.type == pygame.QUIT:
            pygame.quit()
        
            exit()
            
    pygame.display.update()    
    