import numpy as np
from op import composition

A = np.array([[1  , 0.5, 0.4, 0.2]])

R = np.array([[1  , 0.8, 0  , 0  ],
              [0.8, 1  , 0.8, 0  ],
              [0  , 0.8, 1  , 0.8],
              [0  , 0  , 0.8, 1  ]])

B = composition(A, R)
