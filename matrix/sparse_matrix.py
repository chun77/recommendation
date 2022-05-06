import numpy as np

block_size = 1000


class SparseVector:
    """
    vector class ,row_len*1 matrix
    only save row and value
    """

    def __init__(self, value, row):
        """

        # :param value:{1:3,2:1,5:1...}
        :param row:
        """
        self.value = value
        self.row_len = row

    def __add__(self, other):
        """
        if other is a number:every value add this num
        if other is a vector:add vector
        :param other:
        :return:
        """
        if isinstance(other, SparseVector):
            if self.row_len != other.row_len:
                raise IndexError
            res = self.value.copy()
            for i in other.value:
                if i in res.keys():
                    res[i] += other.value[i]
            for i in other.value:
                if i not in res.keys():
                    res[i] = other.value[i]
        else:
            res = self.value.copy()
            for i in other.value:
                res[i] += other
        res_vector = SparseVector(res, self.row_len)
        return res_vector

    def __sub__(self, other):
        """
        if other is a number:every value sub this num
        if other is a vector:add vector
        :param other:
        :return:
        """
        if isinstance(other, SparseVector):
            if self.row_len != other.row_len:
                raise IndexError
            res = self.value.copy()
            for i in other.value:
                if i in res.keys():
                    res[i] -= other.value[i]
            for i in other.value:
                if i not in res.keys():
                    res[i] = -other.value[i]
        else:
            res = self.value.copy()
            for i in other.value:
                res[i] -= other
        res_vector = SparseVector(res, self.row_len)
        return res_vector

    def __mul__(self, other):
        """
        only for vector*number
        :param other:
        :return:
        """
        res = self.value.copy()
        for i in res:
            res[i] *= other
        res_vector = SparseVector(res, self.row_len)
        return res_vector

    def print(self):
        out_matrix = np.zeros([self.row_len, 1])
        for i in self.value:
            out_matrix[i - 1][0] = self.value[i]
        print(out_matrix)

    def sum(self, is_abs=True):
        """
        calculate L1 normal form
        :param is_abs:
        :return:
        """
        res = 0
        if is_abs:
            for i in self.value:
                res += abs(self.value[i])
        else:
            for i in self.value:
                res += self.value[i]
        return res

    def set(self, i, value):
        self.value[i] = value

    def get(self, i):
        return self.value[i]


class SparseMatrix:
    """
    Sparse matrix class
    """

    def __init__(self,
                 row=block_size,
                 col=block_size,
                 index={i: list() for i in range(1, block_size + 1)},
                 value={i: dict() for i in range(1, block_size + 1)}):
        """

        :param row:
        :param col:
        :param index: dict,e.g.[1:[1,2,3],2:[2,3]],index of matrix row and col which value isn't 0
        :param value: dict,e.g.[1:{1:1,2:1,3:1},2:{2:3,3:1}],value of matrix
        """
        self.row_len = row
        self.col_len = col
        self.index = index
        self.value = value

    def __add__(self, other):
        # if self.col_len!=other.col_len or self.row_len!=other.row_len:
        #     raise(IndexError)
        res_index = self.index.copy()
        res_value = self.value.copy()
        for i in other.index:  # row
            for j in other.index[i]:  # col
                if j in res_index[i]:  # value in res not 0
                    res_value[i][j] += other.value[i][j]
                else:
                    res_index[i].append(j)
                    res_value[i][j] = other.value[i][j]
        for i in res_index:
            for j in res_index[i]:
                if res_value[i][j] == 0:
                    # delete 0
                    res_index[i].remove(j)  # list delete value
                    res_value[i].pop(j)  # dict delete key
        res_matrix = SparseMatrix(self.row_len, self.col_len, res_index, res_value)
        return res_matrix

    def __sub__(self, other):
        if self.col_len != other.col_len or self.row_len != other.row_len:
            raise (IndexError)
        res_index = self.index.copy()
        res_value = self.value.copy()
        for i in other.index:  # row
            for j in other.index[i]:  # col
                if j in res_index[i]:  # value in res not 0
                    res_value[i][j] -= other.value[i][j]
                else:
                    res_index[i].append(j)
                    res_value[i][j] = -other.value[i][j]
        for i in res_index:
            for j in res_index[i]:
                if res_value[i][j] == 0:
                    # delete 0
                    res_index[i].remove(j)  # list delete value
                    res_value[i].pop(j)  # dict delete key
        res_matrix = SparseMatrix(self.row_len, self.col_len, res_index, res_value)
        return res_matrix

    def __mul__(self, other):
        """

        :param other:
        :return:
        """
        if isinstance(other, SparseMatrix):
            res_index = {i: list() for i in range(1, self.row_len + 1)}
            res_value = {i: dict() for i in range(1, self.row_len + 1)}
            for i in self.index:
                for j in self.index[i]:
                    for other_i in other.index:
                        for other_j in other.index[other_i]:
                            if j == other_i:
                                value = self.value[i][j] * other.value[other_i][other_j]
                                if other_j in res_index[i]:
                                    res_value[i][other_j] += value
                                else:
                                    res_index[i].append(other_j)
                                    res_value[i][other_j] = value
            res_matrix = SparseMatrix(self.row_len, other.col_len, res_index, res_value)
            return res_matrix
        elif isinstance(other, SparseVector):
            if self.col_len != other.row_len:
                raise IndexError
            res = dict()
            for i in self.index:
                for j in self.index[i]:
                    for other_i in other.value:
                        if j == other_i:
                            value = self.value[i][j] * other.value[other_i]
                            if i in res:
                                res[i] += value
                            else:
                                res[i] = value
            res_vector = SparseVector(res, self.row_len)
            return res_vector
        else:
            res_index = self.index.copy()
            res_value = self.value.copy()
            for i in res_value:
                for j in res_value[i]:
                    res_value[i][j] *= other
            res_matrix = SparseMatrix(self.row_len, self.col_len, res_index, res_value)
            return res_matrix

    def sum(self, is_abs=True):
        """

        :param is_abs:
        :return: sum of all the elements
        """
        res = 0
        if is_abs:
            for i in self.index:
                for j in self.index[i]:
                    res += abs(self.value[i][j])
        else:
            for i in self.index:
                for j in self.index[i]:
                    res += self.value[i][j]
        return sum

    def print(self):
        out_matrix = np.zeros([self.row_len, self.col_len])
        for i in self.index:
            row = i
            for j in self.index[i]:
                col = j
                value = self.value[i][j]
                out_matrix[row - 1][col - 1] = value
        print(out_matrix)

    def set(self, i, j, value):
        if j in self.index[i]:
            self.value[i][j] = value
        else:
            self.index[i].append(j)
            self.value[i][j] = value

    def get(self, i, j):
        if j in self.index[i]:
            return self.value[i][j]
        else:
            raise IndexError
