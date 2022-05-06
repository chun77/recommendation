import pickle
import sys


def get_matrixb(i0, j0):
    with open('DataReadWrite/matrixBlocks/block' + str(i0) + '_' + str(j0) + '.pkl', 'rb') as ff:
        mb = pickle.load(ff)
    return mb


def get_vector(i):
    with open('DataReadWrite/vectorBlocks/oldVector' + str(i) + '.pkl', 'rb') as ff:
        vb = pickle.load(ff)
    return vb


def set_vector(i, vb):
    with open('DataReadWrite/vectorBlocks/oldVector' + str(i) + '.pkl', 'wb') as ff:
        pickle.dump(ff, vb)
    return


def get_out():
    return sys.argv[1]
