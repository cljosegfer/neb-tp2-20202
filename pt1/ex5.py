import numpy as np
from op import relation, snorm, composition

#antcd
A1 = np.array([0.2, 0.4, 0.5]).reshape(1, -1)
A2 = np.array([1  , 1  , 0.3]).reshape(1, -1)

#consq
B1 = np.array([0.1, 0.3]).reshape(1, -1)
B2 = np.array([0.6, 0.2]).reshape(1, -1)

#fato
Alinha = np.array([0, 1, 0]).reshape(1, -1)

#relation
R1 = relation(A1, B1)
R2 = relation(A2, B2)

Blinha1 = composition(Alinha, R1)
Blinha2 = composition(Alinha, R2)

#inferencia
Blinha = snorm(composition(Alinha, R1), composition(Alinha, R2))
