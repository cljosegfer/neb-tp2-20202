import numpy as np

def tnorm(U, V):
    #min element wise
    return np.minimum(U, V)

def snorm(U, V):
    #max element wise
    return np.maximum(U, V)

def composition(U, V):
    #max-min
    return np.amax(np.minimum(U[:, :, None], V[None, :, :]), axis = 1)

def tnormT(U, V):
    #min
    mesh = np.array(np.meshgrid(U, V))
    combinations = mesh.T.reshape(-1, 2)
    return np.amin(combinations, axis = 1).reshape(U.size, V.size)
