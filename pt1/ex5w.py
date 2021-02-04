import numpy as np
from op import tnormT, snorm, tnorm

#antcd
A1 = np.array([0.2, 0.4, 0.5]).reshape(1, -1)
A2 = np.array([1  , 1  , 0.3]).reshape(1, -1)

#consq
B1 = np.array([0.1, 0.3]).reshape(1, -1)
B2 = np.array([0.6, 0.2]).reshape(1, -1)

#fato
Alinha = np.array([0, 1, 0]).reshape(1, -1)

#w
w1 = np.amax(tnorm(Alinha, A1))
w2 = np.amax(tnorm(Alinha, A2))

#inferencia
Blinha = snorm(tnormT(w1, B1), tnormT(w2, B2))