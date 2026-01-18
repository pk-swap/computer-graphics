import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smiley Face with Midpoint Circle")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    screen.set_at((round(x),round(y)),WHITE)

    while x < y:
        x += 1
        if d < 0:
            d = d + 2 * x + 1
        else:
            y -= 1
            d = d + 2 * x - 2 * y + 1
            screen.set_at((xc + x, yc + y), WHITE)
            screen.set_at((xc - x, yc + y), WHITE)
            screen.set_at((xc + x, yc - y), WHITE)
            screen.set_at((xc - x, yc - y), WHITE)
            screen.set_at((xc + y, yc + x), WHITE)
            screen.set_at((xc - y, yc + x), WHITE)
            screen.set_at((xc + y, yc - x), WHITE)
            screen.set_at((xc - y, yc - x), WHITE)

def smile(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    screen.set_at((round(x),round(y)),WHITE)
    while x < y:
        x += 1
        if d < 0:
            d=d+ 2 * x + 1
        else:
            y -= 1
            d=d+ 2 * x - 2 * y + 1
        screen.set_at(((xc+x),(yc+y)),WHITE)
        screen.set_at(((xc-x),(yc+y)),WHITE)
        screen.set_at(((xc+y),(yc+x)),WHITE)
        screen.set_at(((xc-y),(yc+x)),WHITE)       

def main():


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        
        midpoint_circle(300,300,190)
        midpoint_circle(200,210,30)
        midpoint_circle(390,200,30)
        smile(300,330,100)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()