import pygame


def set_pixel(screen, x, y, color):
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    if x >= screen.get_width():
        x = screen.get_width() - 1
    if y >= screen.get_height():
        y = screen.get_height() - 1

    pixel = pygame.Rect((x, y, 1, 1))
    pygame.draw.rect(screen, color, pixel)
