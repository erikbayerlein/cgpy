import pygame
from draw.set_pixel import set_pixel
from draw.wave import draw_wave
from screen.create_screen import create_screen

pygame.init()

screen = create_screen(800, 600)
draw_wave(screen)
#set_pixel(screen, 700, 30, (255, 255, 255))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
