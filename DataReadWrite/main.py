# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matrix.sparse_matrix as mat
import pickle
import DataReadWrite.readWriteBlock as read

# import matrix.sparse_vector as vec
if __name__ == '__main__':
    # a_index={1:[1],2:[1,2]}
    # a_value={1: {1:2},2:{1:2,2:3}}
    # b_index={1:[1],2:[2]}
    # b_value={1:{1:2},2:{2:1}}
    # c_value={1:2,2:1}
    # mat3=mat.SparseVector(c_value,2)
    # mat3.print()
    # mat3.set(1,10)
    # mat3.print()
    # mat1=mat.SparseMatrix(2,2,a_index,a_value)
    # mat2=mat.SparseMatrix(2,2,b_index,b_value)
    # mat1.print()
    # mat1.set(1,2,5)
    # mat1.print()
    # mat2.print()
    # res=mat1*3
    # res.print()
    # res=mat3*2
    # res.print()
    # res=mat1*3
    # res.print()
    # with open('DataReadWrite/block' + str(42) + '_' + str(42) + '.pkl', 'rb') as fr:
    #     m = pickle.load(fr)
    #     m.print()
    #     print(m.index)
    #     print(m.value[4][12])
    #     print(read.out[41*read.block_size+4])
    m = read.get_matrixb(1, 1)
    print(m.index)
    v = read.get_vector(1)
    print(v.value)
