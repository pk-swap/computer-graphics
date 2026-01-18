import pygame
import sys 
pygame.init()
width,height=800,600
screen =pygame.display.set_mode((width,height))
pygame.display.set_caption("dda algorithm")
white=(255,255,255)
black=(0,0,0)


def draw_linedda(x1,y1,x2,y2):
    
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if dx>dy:
        step=dx
    else:
        step=dy
    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1
    for i in range(step):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),white)

    
def main():
    # x1= int(input('enter values of x1:'))
    # y1=int(input('enter values of x2:'))
    # x2=int(input('enter values of y1:'))
    # y2=int(input('enter values of y2:'))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.quit:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        draw_linedda(20,22,100,100)
        pygame.display.flip()

if __name__=="__main__":
    main()
