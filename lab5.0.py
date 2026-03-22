import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    # Region 1
    p1 = ry2 - (rx2 * ry) + (rx2 / 4)

    while (2 * ry2 * x) <= (2 * rx2 * y):
        plot_ellipse_points(xc, yc, x, y)

        if p1 < 0:
            x += 1
            p1 = p1 + (2 * ry2 * x) + ry2
        else:
            x += 1
            y -= 1
            p1 = p1 + (2 * ry2 * x) - (2 * rx2 * y) + ry2

    # Region 2
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)

        if p2 > 0:
            y -= 1
            p2 = p2 - (2 * rx2 * y) + rx2
        else:
            x += 1
            y -= 1
            p2 = p2 + (2 * ry2 * x) - (2 * rx2 * y) + rx2

def plot_ellipse_points(xc, yc, x, y):
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc - x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), WHITE)
    screen.set_at((xc - x, yc - y), WHITE)
    
def main():
    screen.fill(BLACK)


    midpoint_ellipse(400, 300, 150, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
