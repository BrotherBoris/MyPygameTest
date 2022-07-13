import pygame

screensize = (800,600)
gameScreen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Game")
pygame.init()



wheelRotation = 0
mouseIsDown = False

def chooseColor(key):
    if key == 0:
        #print("red")
        return(100,0,0)
    elif key ==1:
        #print("green")
        return(0,100,0)
    elif key == 2:
        #print("blue")
        return(0,0,100)
    else:
        #print("defalut")
        return (100,0,0)
    pass


while True:
    for event in pygame.event.get():

        pygame.draw.rect(gameScreen, (0,255,0), (0,0,40,40))
        
        if event.type == pygame.MOUSEWHEEL:            
            wheelRotation +=1
            if wheelRotation > 2:
                wheelRotation = 0 
            print(wheelRotation)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseIsDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseIsDown = False

        if event.type == pygame.MOUSEMOTION and mouseIsDown == True:
            x, y = pygame.mouse.get_pos()
            pygame.draw.circle(gameScreen, chooseColor(wheelRotation),(x,y),(5))
            

        if event.type == pygame.QUIT:
            pygame.quit()
            

            exit()
            
    pygame.display.update()    
    