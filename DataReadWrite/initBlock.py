import pickle
import os
import math
from matrix.sparse_matrix import SparseMatrix, SparseVector

out = {}
block_size = 1000
n = 8400


def init_matrixb():
    f = open("data.txt", 'r', encoding='utf-16')
    # out-degree
    m0 = SparseMatrix(block_size)
    for i in range(1, math.ceil(n / block_size) + 1):
        for j in range(1, math.ceil(n / block_size) + 1):
            with open('block' + str(i) + '_' + str(j) + '.pkl', 'wb') as fp:
                pickle.dump(m0, fp)
    while 1:
        lines = f.readlines(1000)
        if not lines:
            break
        for line in lines:
            x, y = map(int, line.split())
            if x not in out.keys():
                out[x] = 1
            else:
                out[x] += 1

            i = math.ceil(x / block_size)
            j = math.ceil(y / block_size)
            xi = x % block_size
            if xi == 0:
                xi = block_size
            yi = y % block_size
            if yi == 0:
                yi = block_size
            with open('block' + str(i) + '_' + str(j) + '.pkl', 'rb') as fr:
                m = pickle.load(fr)
                m.set(xi, yi, 1 / out[x])
            with open('block' + str(i) + '_' + str(j) + '.pkl', 'wb') as fw:
                pickle.dump(m, fw)

    f.close()


def init_vb():
    for i in range(math.ceil(n / block_size)):
        v0 = SparseVector(block_size)
        for j in range(block_size):
            v0.set(j, 1 / n)
        with open('oldVector' + str(i) + '.pkl', 'wb') as fp:
            pickle.dump(v0, fp)


if __name__ == '__main__':
    os.system("python readWriteBlock.py {}".format(out))
    init_matrixb()
    init_vb()
