import math

import numpy as np

from DataReadWrite.readWriteBlock import get_matrixb, get_new_vector, set_old_vector, \
    set_new_vector, get_old_vector, get_func_vector
from DataReadWrite.initBlock import get_n, get_total
from matrix import sparse_matrix as mat
from DataReadWrite import readWriteBlock

N = get_total()
n = get_n()
block_size = 1000
sum_row = math.ceil(N / block_size)
sum_col = math.ceil(N / block_size)
beta = 0.85


def leak_pagerank():
    """
    calculate S
    """
    s = 0
    for i in range(1, sum_row + 1):
        s += get_new_vector(i).sum()
    if s < 1:
        return s
    else:
        return -1


def fix_up_pagerank(s):
    """
    re_insert the leaked pagerank
    r_new=M*r_old
    """
    fix_up = (1 - s) / n
    for i in range(1, sum_row + 1):
        r_new = get_new_vector(i)
        r_func = get_func_vector(i)
        r_new_fixed = r_new + r_func * fix_up
        set_new_vector(i, r_new_fixed)


def iterate():
    """
    set new r
    """

    initial = {i: 0 for i in range(1, block_size + 1)}
    for i in range(1, sum_row + 1):
        r_new = mat.SparseVector(initial, block_size)
        for j in range(1, sum_col + 1):
            r_temp = get_new_vector(j)
            r_temp = r_temp * beta
            m = get_matrixb(i, j)
            r_new = m * r_temp + r_new
        # r_new = r_new * beta
        r_func = get_func_vector(i) * (1 / n)
        r_new = r_new + r_func * (1-beta)
        set_old_vector(i, get_new_vector(i))
        set_new_vector(i, r_new)
    if leak_pagerank() != -1:
        temp = leak_pagerank()
        fix_up_pagerank(temp)


def cal_diff():
    """
    calculate the d_value
    """
    diff_sum = 0
    for i in range(1, sum_row + 1):
        r_new = get_new_vector(i)
        r_old = get_old_vector(i)
        r_temp = r_new - r_old
        diff_sum += r_temp.sum()
    return diff_sum


def write_file():
    """
    result.txt
    """
    f = open('result.txt', 'w')
    for i in range(1, sum_row + 1):
        r = get_new_vector(i)
        for j in r.value:
            if r.value[j] != 0:
                temp = j + 1000 * (i - 1)
                f.write(f'{temp} {r.value[j]}\n')
    f.close()


def sort_value():
    f = open("result.txt", 'r', encoding='utf-8')
    numbers = []
    rank_values = []
    while 1:
        lines = f.readlines(1000)
        if not lines:
            break
        for line in lines:
            x, y = map(float, line.split())
            x = int(x)
            numbers.append(x)
            rank_values.append(y)
    f.close()
    rank_values, numbers = my_sort(rank_values, numbers)
    f = open("result1.txt", 'w', encoding='utf-8')
    numbers.reverse()
    rank_values.reverse()
    rank_values = rank_values[:100]
    for i, rv in enumerate(rank_values):
        line = str(numbers[i]) + '           ' + str(rv) + '\n'
        f.write(line)

    return


def my_sort(x, y):
    xy = [(xi, yi) for xi, yi in zip(x, y)]
    sorted_xy = sorted(xy)
    sorted_x = [xi for xi, _ in sorted_xy]
    sorted_y = [yi for _, yi in sorted_xy]
    # print(sorted_xy)
    return sorted_x, sorted_y

