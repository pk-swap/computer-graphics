def draw_linebla(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    lx = 1 if x2 > x1 else -1
    ly = 1 if y2 > y1 else -1

    x, y = x1, y1
    print(x, y)  # starting point

    if dx > dy:
        p = 2 * dy - dx
        while x != x2:   # FIXED condition
            x += lx
            if p >= 0:
                y += ly
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
            print(x, y)
    else:
        p = 2 * dx - dy
        while y != y2:   # FIXED condition
            y += ly
            if p >= 0:
                x += lx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx
            print(x, y)

def main():
    draw_linebla(2, 4, 10, 12)

main()    