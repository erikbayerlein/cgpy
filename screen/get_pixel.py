def get_pixel(screen, x, y):
    color = screen.get_at((x, y))
    return (color[0], color[1], color[2], color[3])


def get_pixel_with_texture(texture, x, y):
    num_rows, num_cols, _ = texture.shape

    x = max(min(x, 1), 0)
    y = max(min(y, 1), 0)

    x = int(x * (num_cols - 1))
    y = int(y * (num_rows - 1))

    color = texture[y][x]

    return (color[0], color[1], color[2])
