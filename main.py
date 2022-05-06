import math

from DataReadWrite.initBlock import get_total
from DataReadWrite.readWriteBlock import get_new_vector
from pageranker1 import iterate, cal_diff, write_file ,sort_value
from matrix.sparse_matrix import SparseMatrix,SparseVector

e = 0.0001
"""
Accuracy
"""
if __name__ == '__main__':
    if_converge = False
    while not if_converge:
        iterate()
        D_value = cal_diff()
        print(D_value)
        if D_value < e:
            if_converge = True
            write_file()
            sort_value()
            s = 0
            for i in range(1, math.ceil(get_total() / 1000) + 1):
                s += get_new_vector(i).sum()
            print(s)
        else:
            if_converge = False
