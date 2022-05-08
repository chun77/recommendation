from pageranker1 import iterate, cal_diff, write_file, sort_value
from initBlock import init_block
import time
e = 0.00000001
"""
Accuracy
"""
if __name__ == '__main__':
    init_block()
    if_converge = False
    iter_count = 1
    begin_time = time.time()
    while not if_converge:
        print(f'iter:{iter_count}')
        iterate()
        D_value = cal_diff()
        end_time = time.time()
        total_time = round(end_time - begin_time,4)
        print(f'D_value:{D_value}   time:{total_time}s')
        if D_value < e:
            if_converge = True
            write_file()
            sort_value()
        else:
            if_converge = False
            iter_count += 1
    end_time = time.time()
    total_time = round(end_time - begin_time, 4)
    print(f'eps:{e} ,pagerank total time:{total_time}s')