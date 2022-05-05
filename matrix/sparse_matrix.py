import numpy as np
class SparseVector:
    """
    vector class ,row_len*1 matrix
    only save row and value
    """
    def __init__(self,value,row):
        """

        :param value:{1:3,2:1,5:1...}
        :param row:
        """
        self.value=value
        self.row_len=row

    def __add__(self, other):
        """
        if other is a number:every value add this num
        if other is a vector:add vector
        :param other:
        :return:
        """
        if isinstance(other,SparseVector):
            if self.row_len!=other.row_len:
                raise IndexError
            res=self.value.copy()
            for i in other.value:
                if i in res.keys():
                    res[i]+=other.value[i]
                else:
                    res[i]=other.value[i]
        else:
            res = self.value.copy()
            for i in other.value:
                res[i] += other
        res_vector=SparseVector(res,self.row_len)
        return res_vector

    def __mul__(self, other):
        """
        only for vector*number
        :param other:
        :return:
        """
        res = self.value.copy()
        for i in res:
            res[i]*=other
        res_vector=SparseVector(res,self.row_len)
        return res_vector

    def print(self):
        out_matrix=np.zeros([self.row_len,1])
        for i in self.value:
            out_matrix[i-1][0]=self.value[i]
        print(out_matrix)


class SparseMatrix:
    """
    Sparse matrix class
    """
    def __init__(self,
                 row=1000,
                 col=1000,
                 index={i:list() for i in range(1,1001)},
                 value={i:list() for i in range(1,1001)}):
        """

        :param row:
        :param col:
        :param index: dict,e.g.[1:[1,2,3],2:[2,3]],index of matrix row and col which value isn't 0
        :param value: dict,e.g.[1:[1,1,1],2:[1,1]],value of matrix
        """
        self.row_len=row
        self.col_len=col
        self.index=index
        self.value=value

    def __add__(self, other):
        if self.col_len!=other.col_len or self.row_len!=other.row_len:
            raise(IndexError)
        res_index=self.index.copy()
        res_value=self.value.copy()
        for i in other.index:   # row
            for j,value_j in enumerate(other.index[i]):   # col
                if value_j in res_index[i]:   # value in res not 0
                    res_value[i][j]+=other.value[i][j]
                else:
                    res_index[i].append(value_j)
                    res_value[i].append(other.value[i][j])

        for i in res_index:
            for j in range(len(res_index[i])):
                if res_value[i][j]==0:
                    res_index[i][j].pop()
                    res_value[i][j].pop()
        res_matrix=SparseMatrix(self.row_len,self.col_len,res_index,res_value)
        return res_matrix


    def __sub__(self, other):
        if self.col_len!=other.col_len or self.row_len!=other.row_len:
            raise(IndexError)
        res_index=self.index.copy()
        res_value=self.value.copy()
        for i in other.index:   # row
            for j,value_j in enumerate(other.index[i]):   # col
                if value_j in res_index[i]:   # value in res not 0
                    res_value[i][j]-=other.value[i][j]
                else:
                    res_index[i].append(value_j)
                    res_value[i].append(-other.value[i][j])

        for i in res_index:
            for j in range(len(res_index[i])):
                if res_value[i][j]==0:
                    res_index[i][j].pop()
                    res_value[i][j].pop()
        res_matrix=SparseMatrix(self.row_len,self.col_len,res_index,res_value)
        return res_matrix


    def __mul__(self, other):
        """

        :param other:
        :return:
        """
        if isinstance(other,SparseMatrix):
            res_index = {i:list() for i in range(1,self.row_len+1)}
            res_value = {i:list() for i in range(1,self.row_len+1)}
            for i in self.index:
                for j,col in enumerate(self.index[i]):
                    for other_i in other.index:
                        for other_j,other_col in enumerate(other.index[other_i]):
                            if col==other_i:
                                value=self.value[i][j]*other.value[other_i][other_j]
                                if other_col in res_index[i]:
                                    new_index=res_index[i].index(other_col)
                                    res_value[i][new_index]+=value
                                else:
                                    res_index[i].append(other_col)
                                    res_value[i].append(value)
            res_matrix=SparseMatrix(self.row_len,other.col_len,res_index,res_value)
            return res_matrix
        elif isinstance(other,SparseVector):
            res = dict()
            for i in self.index:
                for j,col in enumerate(self.index[i]):
                    for other_i in other.value:
                        if col==other_i:
                            value=self.value[i][j]*other.value[other_i]
                            if i in res:
                                res[i] += value
                            else:
                                res[i]=value
            res_vector = SparseVector(res,self.row_len)
            return res_vector
        else:
            res_index = self.index.copy()
            res_value = self.value.copy()
            for i in res_value:
                for j in range(len(res_value[i])):
                    res_value[i][j]*=other
            res_matrix=SparseMatrix(self.row_len,self.col_len,res_index,res_value)
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
        for i in self.index:
            row=i
            for j,list_j in enumerate(self.index[i]):
                col=self.index[i][j-1]
                value=self.value[i][j-1]
                out_matrix[row-1][col-1]=value
        print(out_matrix)