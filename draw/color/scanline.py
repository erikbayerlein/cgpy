from draw.set_pixel import set_pixel


def scanline(screen, pol, intensity):
    initial_y = min([p[1] for p in pol.polygon])
    final_y = max([p[1] for p in pol.polygon])

    for y in range(initial_y, final_y+1):
        p_int = []

        initial_p = pol.polygon[0]
        for i in range(1, len(pol.polygon)):
            final_p = pol.polygon[i]
            p = intersection(y, initial_p, final_p)
            if p != -1:
                p_int.append(p)
            initial_p = final_p

        final_p = pol.polygon[0]
        p = intersection(y, initial_p, final_p)
        if p != -1:
            p_int.append(p)

        if len(p_int) != 0:
            print_scan(screen, p_int, intensity)

def print_scan(screen, p_int, intensity):
    p_int.sort(key=lambda p: p[0])

    y = p_int[0][1]

    for i in range(0, len(p_int)-1, 2):
        x1 = p_int[i][0]
        x2 = p_int[i+1][0]

        for x in range(round(x1), round(x2)+1):
            set_pixel(screen, round(x), y, intensity)

def intersection(y, initial, final):
    if initial[1] > final[1]:
        initial, final = final, initial

    if initial[1] == final[1]:
        return -1

    t = (y - initial[1]) / (final[1] - initial[1])

    if t <= 0 or t > 1:
        return -1

    x = initial[0] + t * (final[0] - initial[0])

    return [x, y]
