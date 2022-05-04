# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matrix.sparse_matrix as mat

if __name__ == '__main__':
    a_index=[(1,1),(2,2)]
    a_value=[1,2]
    b_index=[(1,1)]
    b_value=[3]
    mat1=mat.SparseMatrix(2,2,a_index,a_value)
    mat2=mat.SparseMatrix(2,1,b_index,b_value)
    mat1.print()
    mat2.print()
    res=mat1*mat2
    res.print()
    # res=mat1-mat2
    # res.print()
