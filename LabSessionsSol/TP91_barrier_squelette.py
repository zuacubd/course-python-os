# encoding: UTF-8

import threading, numpy


def sqmatrix_multiply_element(A, B, i, j):
    size = len(A)
    return sum(A[i, k] * B[k, j] for k in range(size))


def A_x_B_square_element(bar, AB, AB2, A, B, i, j):
    # calcule l'élément (i,j) de A*B, puis l'élément (i,j) de (A*B)^2
    ...


def A_x_B_square(A, B):
    size = len(A)
    # crée les matrices AB et AB2 pour stocker les résultats des calculs, puis
    # lance A_x_B_square_element sur size^2 threads, un pour chaque élément de la matrice résultat
    ...


# premier test:
M = numpy.ones((3, 3))
print(A_x_B_square(M,M))
