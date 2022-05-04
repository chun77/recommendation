import numpy as np
class SparseMatrix:

    def __init__(self,row,col,index,value):
        """

        :param row:
        :param col:
        :param index: list,e.g.[(1,1),(1,2)],index of matrix
        :param value: list,e.g.[2,1],value of matrix
        """
        self.row_len=row
        self.col_len=col
        self.index=index
        self.value=value

    def __add__(self, other):
        res_index=[]
        res_value=[]
        for i in range(len(self.index)):
            res_index.append(self.index[i])
            res_value.append(self.value[i])
        for i in range(len(other.index)):
            if other.index[i] in res_index:
                res_value[res_index.index(other.index[i])]+=other.value[i]
                # print(res_index[i])
                # print(res_value[i])
            else:
                res_index.append(other.index[i])
                res_value.append(other.value[i])
        for i in range(len(res_value)):
            if res_value[i]==0:
                res_value.pop(i)
                res_index.pop(i)
        res_matrix=SparseMatrix(self.row_len,self.col_len,res_index,res_value)
        return res_matrix


    def __sub__(self, other):
        res_index=[]
        res_value=[]
        for i in range(len(self.index)):
            res_index.append(self.index[i])
            res_value.append(self.value[i])
        for i in range(len(other.index)):
            if other.index[i] in res_index:
                res_value[res_index.index(other.index[i])]-=other.value[i]
            else:
                res_index.append(other.index[i])
                res_value.append(-other.value[i])
        for i in range(len(res_value)):
            if res_value[i]==0:
                res_value.pop(i)
                res_index.pop(i)
        res_matrix=SparseMatrix(self.row_len,self.col_len,res_index,res_value)
        return res_matrix


    def __mul__(self, other):
        res_index = []
        res_value = []
        for i,index_i in enumerate(self.index):
            for j,index_j in enumerate(other.index):
                if index_i[1]==index_j[0]:
                    value=self.value[i]*other.value[j]
                    if (index_i[0],index_j[1]) in res_index:
                        res_value[res_index.index(index_i[0],index_j[1])]+=value
                    else:
                        res_index.append((index_i[0],index_j[1]))
                        res_value.append(value)
        res_matrix=SparseMatrix(self.row_len,other.col_len,res_index,res_value)
        return res_matrix


    def sum(self,is_abs=True):
        """

        :param is_abs:
        :return: sum of all the elements
        """
        res=0
        if is_abs:
            for i in self.value:
                res+=abs(i)
        else:
            for i in self.value:
                res+=i
        return sum

    def print(self):
        out_matrix=np.zeros([self.row_len,self.col_len])
        for i in range(len(self.index)):
            loc=self.index[i]
            row=loc[0]
            col=loc[1]
            value=self.value[i]
            out_matrix[row-1][col-1]=value
        print(out_matrix)