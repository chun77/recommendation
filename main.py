import math
import time

from DataReadWrite.initBlock import get_total
from DataReadWrite.readWriteBlock import get_new_vector
from pageranker1 import iterate, cal_diff, write_file ,sort_value
from matrix.sparse_matrix import SparseMatrix,SparseVector

e = 0.00000001
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
        else:
            if_converge = False
