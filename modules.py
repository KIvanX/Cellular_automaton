import numpy as np
from numba import njit


@njit
def tick(a, n, m):
    b = np.zeros((n, m), dtype=np.int32)

    for i in range(1, n-1):
        for j in range(1, m-1):
            k = a[i-1][j-1] + a[i-1][j] + a[i-1][j+1] + a[i][j-1] + \
                a[i][j+1] + a[i+1][j-1] + a[i+1][j] + a[i+1][j+1]
            if (not a[i][j] and 2 < k < 4) or (a[i][j] and 1 < k < 4):
                b[i][j] = 1
    return b


@njit
def tick3(a, n, m):
    b = np.zeros((n, m), dtype=np.int32)

    for i in range(1, n-1):
        for j in range(1, m-1):
            k = [a[i-1][j-1], a[i-1][j], a[i-1][j+1],
                 a[i][j-1],              a[i][j+1],
                 a[i+1][j-1], a[i+1][j], a[i+1][j+1]]

            k1, k2, k3 = k.count(1), k.count(2), k.count(3)

            if a[i][j] == 1 and k2 >= 3:
                b[i][j] = 2
            elif a[i][j] == 2 and k3 >= 3:
                b[i][j] = 3
            elif a[i][j] == 3 and k1 >= 3:
                b[i][j] = 1
            else:
                b[i][j] = a[i][j]
    return b


def generate(n, m):
    a = np.zeros((n, m))

    # n1 = min(n, m)
    # for k in range(n1):
    #     a[n1//2][k], a[k][n1//2] = 1, 1

    # n1 = min(n, m)
    # for k in range(0, n1):
    #     a[k][k], a[k][n1-k-1] = 1, 1

    # for i in range(0, n, 3):
    #     for j in range(0, m, 3):
    #         a[i][j], a[i][j+1], a[i+1][j], a[i+1][j+1] = 1, 1, 1, 1
    #
    # a[n//2+2][m//2+1] = 1

    from random import randint
    for i in range(0, n):
        for j in range(0, m):
            a[i][j] = randint(1, 3)

    # for i in range(0, n):
    #     for j in range(0, m):
    #         a[i][j] = 1
    # for i in range(0, 100):
    #     for j in range(0, 100):
    #         a[i][j] = 2
    # for i in range(50, 150):
    #     for j in range(50, 150):
    #         a[i][j] = 3

    # for i in range(1, 125, 5):
    #     for j in range(1, 100, 5):
    #         a[i+2][j+1] = a[i+3][j+2] = a[i+3][j+3] = a[i+2][j+3] = a[i+1][j+3] = 1
    # for i in range(175, n, 5):
    #     for j in range(200, m, 5):
    #         a[i+1][j+1] = a[i+2][j+1] = a[i+3][j+2] = a[i+1][j+2] = a[i+1][j+3] = 1

    return a


def add_gliders(a, n, m):
    j = 1
    for i in range(1, 100, 5):
        a[i + 2][j + 1] = a[i + 3][j + 2] = a[i + 3][j + 3] = a[i + 2][j + 3] = a[i + 1][j + 3] = 1
    i = 1
    for j in range(1, 125, 5):
        a[i + 2][j + 1] = a[i + 3][j + 2] = a[i + 3][j + 3] = a[i + 2][j + 3] = a[i + 1][j + 3] = 1

    j = m - 5
    for i in range(175, n, 5):
        a[i + 1][j + 1] = a[i + 2][j + 1] = a[i + 3][j + 2] = a[i + 1][j + 2] = a[i + 1][j + 3] = 1
    i = n - 5
    for j in range(200, m, 5):
        a[i + 1][j + 1] = a[i + 2][j + 1] = a[i + 3][j + 2] = a[i + 1][j + 2] = a[i + 1][j + 3] = 1

    return a


def get_ruj(a, x, y):
    x -= 6
    y -= 2

    a[x+6][y+2] = a[x+6][y+3] = 1
    a[x+7][y+2] = a[x+7][y+3] = 1

    a[x+4][y+15] = 1
    a[x+5][y+14] = a[x+5][y+16] = 1
    a[x+6][y+13] = a[x+6][y+17] = a[x+6][y+18] = 1
    a[x+7][y+13] = a[x+7][y+17] = a[x+7][y+18] = 1
    a[x+8][y+13] = a[x+8][y+17] = a[x+8][y+18] = 1
    a[x+9][y+14] = a[x+9][y+16] = 1
    a[x+10][y+15] = 1

    a[x+2][y+27] = 1
    a[x+3][y+24] = a[x+3][y+25] = a[x+3][y+26] = a[x+3][y+27] = 1
    a[x+4][y+23] = a[x+4][y+24] = a[x+4][y+25] = a[x+4][y+26] = 1
    a[x+5][y+23] = a[x+5][y+26] = 1
    a[x+6][y+23] = a[x+6][y+24] = a[x+6][y+25] = a[x+6][y+26] = 1
    a[x+7][y+24] = a[x+7][y+25] = a[x+7][y+26] = a[x+7][y+27] = 1
    a[x+8][y+27] = 1

    a[x+6][y+32] = a[x+7][y+32] = 1

    a[x+4][y+36] = a[x+4][y+37] = 1
    a[x+5][y+36] = a[x+5][y+37] = 1

    return a
