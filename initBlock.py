import pickle
import math
import time

from matrix.sparse_matrix import SparseMatrix, SparseVector

out = {}
block_size = 1000
# 有连接关系的个数
n = 0
# 向量长度
total_size = 0
srcs = []
dests = []
all_pages = []


def read_lines():
    f = open("data.txt", 'r', encoding='utf-16')
    while 1:
        lines = f.readlines(1000)
        if not lines:
            break
        for line in lines:
            x, y = map(int, line.split())
            srcs.append(x)
            dests.append(y)
            if x not in out.keys():
                out[x] = 1
            else:
                out[x] += 1
    global all_pages
    all_pages = list(set(srcs).union(dests))
    global n
    n = len(all_pages)
    global total_size
    total_size = max(all_pages)
    # print(number)
    # print(sorted(number))

    f.close()
    f1 = open("info.txt", 'w', encoding='utf-8')
    info = str(n) + " " + str(total_size)
    f1.write(info)

    return


# def my_sort(x, y):
#     Xy = [(xi, yi) for xi, yi in zip(X[:, 0], y)]
#     sorted_Xy = sorted(Xy)
#     sorted_X = [xi for xi, _ in sorted_Xy]
#     sorted_y = [yi for _, yi in sorted_Xy]
#     print(sorted_X)
#     print(sorted_y)
#     return x,y


def init_matrixb():
    f = open("data.txt", 'r', encoding='utf-16')
    # out-degree
    m0 = SparseMatrix(block_size)
    for i in range(1, math.ceil(total_size / block_size) + 1):
        for j in range(1, math.ceil(total_size / block_size) + 1):
            with open('matrixBlocks/block' + str(i) + '_' + str(j) + '.pkl', 'wb') as fp:
                pickle.dump(m0, fp)
    for index, x in enumerate(srcs):
        y = dests[index]
        i = math.ceil(x / block_size)
        j = math.ceil(y / block_size)
        xi = x % block_size
        if xi == 0:
            xi = block_size
        yi = y % block_size
        if yi == 0:
            yi = block_size
        with open('matrixBlocks/block' + str(j) + '_' + str(i) + '.pkl', 'rb') as fr:
            m = pickle.load(fr)
            m.set(yi, xi, 1 / out[x])
            # m.print()
        with open('matrixBlocks/block' + str(j) + '_' + str(i) + '.pkl', 'wb') as fw:
            pickle.dump(m, fw)


def init_vb():
    global all_pages
    for i in range(1, math.ceil(total_size / block_size) + 1):
        value0 = {}
        value1 = {}
        for k in range(1, block_size + 1):
            cur = k + (i - 1) * block_size
            if cur not in all_pages:
                value0[k] = 0
                value1[k] = 0
            else:
                value0[k] = 1
                value1[k] = 1 / n
        v0 = SparseVector(value0, block_size)
        # v0.print()
        with open('vectorBlocks/funcVector' + str(i) + '.pkl', 'wb') as fp:
            pickle.dump(v0, fp)
        v1 = SparseVector(value1, block_size)
        with open('vectorBlocks/oldVector' + str(i) + '.pkl', 'wb') as fp:
            pickle.dump(v1, fp)
    for i in range(1, math.ceil(total_size / block_size) + 1):
        value1 = {}
        for k in range(1, block_size + 1):
            cur = k + (i - 1) * block_size
            # print(cur)
            if cur not in all_pages:
                value1[k] = 0
            else:
                value1[k] = 1 / n
        v0 = SparseVector(value1, block_size)
        # v0.print()
        with open('vectorBlocks/newVector' + str(i) + '.pkl', 'wb') as fp:
            pickle.dump(v0, fp)


def get_n():
    return n


def get_total():
    return total_size


def init_block():
    print('=======begin init matrix========')
    begin_time = time.time()
    read_lines()
    init_matrixb()
    init_vb()
    end_time = time.time()
    total_time = round(end_time - begin_time, 4)
    print(f'total_time:{total_time}s')
    print("number is %d" % n)
    print("total_size is %d" % total_size)
    print('=======end init matrix=======')

    return


# if __name__ == '__main__':
#     print('=======begin init matrix========')
#     begin_time = time.time()
#     read_lines()
#     init_matrixb()
#     init_vb()
#     end_time = time.time()
#     total_time = round(end_time - begin_time, 4)
#     print(f'total_time:{total_time}s')
#     print("number is %d" % n)
#     print("total_size is %d" % total_size)
#     print('=======end init matrix=======')
