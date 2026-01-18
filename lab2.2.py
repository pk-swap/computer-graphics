import pygame
import sys 
pygame.init()
width,height=800,600
screen =pygame.display.set_mode((width,height))
pygame.display.set_caption("dda algorithm")
white=(255,255,255)
black=(0,0,0)


def draw_linedda(x1,y1,x2,y2):
    
    dx=x2-x1
    dy=y2-y1
    if abs(dx>dy):
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
        
        draw_linedda(100, 50, 50, 100)
        draw_linedda(100, 50, 150, 100)
        draw_linedda(50, 100, 150, 100)
        draw_linedda(50, 100, 50, 200)
        draw_linedda(150, 100, 150, 200)
        draw_linedda(50, 200, 150, 200)

        draw_linedda(80, 160, 80, 200)
        draw_linedda(120, 160, 120, 200)
        draw_linedda(80, 160, 120, 160)
        pygame.display.flip()

if __name__=="__main__":
    main()
