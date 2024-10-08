import pickle


def get_matrixb(i0, j0):
    with open('matrixBlocks/block' + str(i0) + '_' + str(j0) + '.pkl', 'rb') as ff:
        mb = pickle.load(ff)
    return mb


def get_old_vector(i):
    with open('vectorBlocks/oldVector' + str(i) + '.pkl', 'rb') as ff:
        vb = pickle.load(ff)
    return vb


def set_old_vector(i, vb):
    with open('vectorBlocks/oldVector' + str(i) + '.pkl', 'wb') as ff:
        pickle.dump(vb, ff)
    return


def get_new_vector(i):
    with open('vectorBlocks/newVector' + str(i) + '.pkl', 'rb') as ff:
        vb = pickle.load(ff)
    return vb


def set_new_vector(i, vb):
    with open('vectorBlocks/newVector' + str(i) + '.pkl', 'wb') as ff:
        pickle.dump(vb, ff)
    return


def get_func_vector(i):
    with open('vectorBlocks/funcVector' + str(i) + '.pkl', 'rb') as ff:
        vb = pickle.load(ff)
    return vb
