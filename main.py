import pygame

from draw.color import Color
from draw.texture import Texture
from draw.draw import Draw
from draw.polygon.polygon import Polygon
from draw.polygon.texture_polygon import TexturePolygon
from screen.create_screen import create_screen


pygame.init()

screen = create_screen(600, 600)

Draw.bresenham(screen, 100, 30, 300, 300, (255, 255, 255))
Draw.dda(screen, 100, 30, 100, 100, (255, 255, 255))
#Draw.anti_alising_dda(screen, 100, 30, 500, 500, [255, 255, 255])
Draw.circumference(screen, 300, 300, 50, (255, 255, 255))

triangle = Polygon()
triangle.insert_vertex(300, 300)
triangle.insert_vertex(100, 500)
triangle.insert_vertex(500, 500)
Draw.draw_polygon(screen, triangle, (255, 255, 255))


Color.scanline_base(screen, triangle, (255, 255, 255))


cat_texture = Texture.import_texture("cat_cg.jpeg")
cat = TexturePolygon(
    [
        [100, 100, 0, 0],
        [100, 500, 0, 1],
        [500, 500, 1, 1],
        [500, 100, 1, 0]
    ]
)

Texture.scanline_with_texture(screen, cat, cat_texture)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
