# encoding: UTF-8

import threading, numpy


def sqmatrix_multiply_element(A, B, i, j):
    size = len(A)
    return sum(A[i, k] * B[k, j] for k in range(size))


def A_x_B_square_element(bar, AB, AB2, A, B, i, j):
    AB[i,j] = sqmatrix_multiply_element(A, B, i, j)
    bar.wait()
    AB2[i, j] = sqmatrix_multiply_element(AB, AB, i, j)
    bar.wait()


def A_x_B_square(A, B):
    size = len(A)
    AB = numpy.zeros((size, size))
    AB2 = numpy.zeros((size, size))
    bar = threading.Barrier(size**2 + 1)
    for i in range(size):
        for j in range(size):
            t = threading.Thread(target=A_x_B_square_element, args=(bar, AB, AB2, A, B, i, j))
            t.start()
    bar.wait()
    bar.wait()
    return AB2

M = numpy.ones((5, 5))
print(A_x_B_square(M,M))
