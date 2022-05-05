import sparse_matrix as mat
def read_matrix(data_path,size,block_size,temp_path):
    """
    read the big sparse matrix from source data
    save the small matrix in a temp directory (pkl)
    size of big matrix:10000*10000
    size of small matrix:1000*1000
    and we could divide the big matrix to 100 small matrices
    you should save state transition matrix and origin col vector
    add any method you need
    """
    pass

class BigMatrix:

    def __init__(self,data_path,size,block_size,temp_path):
        self.data_path=data_path
        self.size=size
        self.block_size=block_size
        self.temp_path=temp_path
        self.block_num=size/block_size
        read_matrix(data_path,size,block_size,temp_path)
