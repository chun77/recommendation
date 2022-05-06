import numpy as np

from DataReadWrite.readWriteBlock import  get_matrixb, get_new_vector, set_old_vector, \
    set_new_vector, get_old_vector
from matrix import sparse_matrix as mat
from DataReadWrite import readWriteBlock

N = 9000
block_size = 1000
sum_row = int(N/block_size)
sum_col = int(N/block_size)
beta = 0.85
e = 0.00001
# R_old = mat.SparseVector(dict.fromkeys(np.arange(block_size), 1/9000), N)
"""
index of matrix and vector
"""


def leak_pagerank():
    """
    calculate S
    """
    s = 0
    for i in range(sum_row):
        s += get_new_vector(i+1).sum()
    if s < 1:
        return s
    else:
        return -1


def fix_up_pagerank(s):
    """
    re_insert the leaked pagerank
    r_new=M*r_old
    """
    r_fix_up = (1-s)/N
    for i in range(sum_row):
        r_new = get_new_vector(i+1)
        r_new_fixed = r_new + r_fix_up
        set_new_vector(i+1, r_new_fixed)
    # r_new_fixed = mat.SparseVector(r_new, r_new.row_len)
    # r_new_fixed += r_fix_up


def iterate():
    """
    set new r
    """
    d_value = 0
    initial = dict.fromkeys(np.arange(block_size), '0')
    for i in range(sum_row):
        r_new = mat.SparseVector(initial, block_size)
        for j in range(sum_col):
            r_temp = get_new_vector(j+1)
            M = get_matrixb(i+1, j+1)
            r_new += M * r_temp
        r_new = r_new * beta
        set_old_vector(i+1, get_new_vector(i+1))
        set_new_vector(i+1, r_new)
        # r_temp = r_new - r_old
        # d_value = r_temp.sum()
    if leak_pagerank() != -1:
        temp = leak_pagerank()
        fix_up_pagerank(temp)


def cal_diff():
    """
    calculate the d_value
    """
    diff_sum = 0
    for i in range(sum_row):
        r_new = get_new_vector(i+1)
        r_old = get_old_vector(i+1)
        r_temp = r_new - r_old
        diff_sum += r_temp.sum()
    return diff_sum



def if_end(d_value):
    """
    d_value vs e
    """
    if d_value < e:
        return True
    else:
        return False


if __name__ == '__main__':
    if_converge = False
    while not if_converge:
        iterate()
        D_value = cal_diff()
        if D_value < e:
            if_converge = True
        else:
            if_converge = False








