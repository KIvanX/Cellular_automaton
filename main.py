import pygame as pg
from modules import *

h, w = 600, 1200
pg.init()
window = pg.display.set_mode((w, h))
pg.display.set_caption("FPS: ")
clock = pg.time.Clock()
n, m = 100, 200
a = generate(n, m)
pg.display.flip()


game, FPS, drawing, deleting, pause = True, 30, False, False, True
while game:
    clock.tick(FPS if not pause else 100)
    txt = '    ПАУЗА' if pause else ''
    pg.display.set_caption("FPS: " + str(int(clock.get_fps())) + ' -> ' + str(FPS) + txt)

    window.fill((10, 50, 10))

    # for i in range(n):
    #     pg.draw.line(window, (0, 0, 0), (0, int(h/n*i)), (w, int(h/n*i)))
    # for i in range(m):
    #     pg.draw.line(window, (0, 0, 0), (int(w/m*i), 0), (int(w/m*i), h))

    if not pause:
        a = tick3(a, n, m)

    if drawing:
        x, y = pg.mouse.get_pos()
        a[int(y/h*n)][int(x/w*m)] = 1

    if deleting:
        x, y = pg.mouse.get_pos()
        a[int(y/h*n)][int(x/w*m)] = 0

    for i in range(n):
        for j in range(m):
            # if a[i][j] == 1:
            #     pg.draw.rect(window, (50, 200, 50), (w/m*j+1, h/n*i+1, w/m-1, h/n-1))
            if a[i][j] == 1:
                pg.draw.rect(window, (250, 0, 0), (w/m*j+1, h/n*i+1, w/m-1, h/n-1))
            if a[i][j] == 2:
                pg.draw.rect(window, (250, 150, 0), (w/m*j+1, h/n*i+1, w/m-1, h/n-1))
            if a[i][j] == 3:
                pg.draw.rect(window, (200, 200, 0), (w/m*j+1, h/n*i+1, w/m-1, h/n-1))

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True

        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            drawing = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            deleting = True

        if event.type == pg.MOUSEBUTTONUP and event.button == 3:
            deleting = False

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                pause = not pause

            if event.key == pg.K_ESCAPE:
                a = np.zeros((n, m))

            if event.key == pg.K_g:
                a = add_gliders(a, n, m)

            if event.key == pg.K_r:
                x, y = pg.mouse.get_pos()
                a = get_ruj(a, int(y / h * n), int(x / w * m))

    if pg.key.get_pressed()[pg.K_UP] and FPS < 400:
        FPS += 1

    if pg.key.get_pressed()[pg.K_DOWN] and FPS > 1:
        FPS -= 1
