import pygame
from draw.line.bresenham.bresenham import bresenham
from draw.line.dda.dda import dda
from draw.wave import draw_wave
from screen.create_screen import create_screen

pygame.init()

screen = create_screen(800, 600)
draw_wave(screen)
bresenham(screen, 100, 20, 300, 600, (255, 255, 255))
dda(screen, 100, 20, 300, 600, (255, 255, 255))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
