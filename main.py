# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matrix.sparse_matrix as mat
# import matrix.sparse_vector as vec
if __name__ == '__main__':
    a_index={1:[1],2:[1,2]}
    a_value={1: {1:2},2:{1:2,2:3}}
    b_index={1:[1],2:[2]}
    b_value={1:{1:2},2:{2:1}}
    c_value={1:2,2:1}
    mat3=mat.SparseVector(c_value,2)
    # mat3.print()
    mat1=mat.SparseMatrix(2,2,a_index,a_value)
    mat2=mat.SparseMatrix(2,2,b_index,b_value)
    mat1.print()
    mat1.set(1,2,5)
    mat1.print()
    # mat2.print()
    # res=mat1*3
    # res.print()
    # res=mat3*2
    # res.print()
    # res=mat1*3
    # res.print()
