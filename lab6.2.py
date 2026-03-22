import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Drawing with Scaling")
white = (255, 255, 255)
black = (0, 0, 0)

def scale(x1, y1, x2, y2, sx, sy, cx, cy):

    x1_n = cx + (x1 - cx) * sx
    y1_n = cy + (y1 - cy) * sy
    x2_n = cx + (x2 - cx) * sx
    y2_n = cy + (y2 - cy) * sy
    return x1_n, y1_n, x2_n, y2_n

def bla_line_draw(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    lx = 1 if x2 > x1 else -1
    ly = 1 if y2 > y1 else -1
    x, y = x1, y1

    if dx > dy:
        p = 2 * dy - dx
        for i in range(dx):
            screen.set_at((round(x), round(y)), white)
            x += lx
            if p < 0:
                p += 2 * dy
            else:
                y += ly
                p += 2 * dy - 2 * dx
    else:
        p = 2 * dx - dy
        for i in range(dy):
            screen.set_at((round(x), round(y)), white)
            y += ly
            if p < 0:
                p += 2 * dx
            else:
                x += lx
                p += 2 * dx - 2 * dy

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    # Original line
    bla_line_draw(50, 100, 350, 100)

 # #scaling
    e,f,g,h=scale(50,100,350,100,2,2,200,100)

    bla_line_draw(e,f,g,h)

    pygame.display.flip()