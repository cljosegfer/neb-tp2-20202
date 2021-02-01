import numpy as np
from op import tnorm

def composition(U, V):
    #max-product
    return np.amax(np.multiply(U[:, :, None], V[None, :, :]), axis = 1)

Q = np.array([[0,    0.8,  0.6,  0.25], 
              [0.7,  0.98, 0.15, 0.5]])

R = np.array([[1,    0.4,  0.2], 
              [0.1,  0.4,  0.7],
              [0.4,  0.15, 0.05],
              [0.85, 0.3,  0.1]])

L = np.array([[1,    0.2,  0.6,  0.8],
              [0.85, 0.3,  0.8,  0.88]])

M = tnorm(Q, 1 - L)
P = composition(Q, R)
