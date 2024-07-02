import pygame

from draw.color.scanline import scanline
from screen.create_screen import create_screen

from draw.line.bresenham.bresenham import bresenham
from draw.line.dda.dda import dda

from draw.polygon.circumference import circumference
from draw.polygon.polygon import Polygon


pygame.init()

screen = create_screen(600, 600)

# draw_wave(screen)
bresenham(screen, 100, 30, 300, 600, (255, 255, 255))
dda(screen, 100, 0, 300, 600, (255, 255, 255))

triangle = Polygon()
triangle.insert_vertex(300, 300)
triangle.insert_vertex(100, 500)
triangle.insert_vertex(500, 500)
triangle.draw_polygon(screen, (255, 255, 255))

circle = circumference(screen, 300, 300, 50, (255, 255, 255))

scanline(screen, triangle, (255, 255, 255))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
