import numpy as np
import matplotlib.pyplot as plt
from pertinencia import trapmf, trimf
from op import tnormT, snorm, tnorm

#espaco
start = 2
stop = 8
step = 0.05
num = int(stop / step + 1)
x = np.linspace(start, stop, num)

#antcd
A1 = trapmf(x = x, a = 3, b = 4, c = 5, d = 6).reshape(1, -1)
A2 = trapmf(x = x, a = 6, b = 6.5, c = 7, d = 7.5).reshape(1, -1)
#consq
C1 = trimf(x = x, a = 3, b = 4, c = 5).reshape(1, -1)
C2 = trimf(x = x, a = 4, b = 5, c = 6).reshape(1, -1)

#fato
Alinha = trimf(x = x, a = 5, b = 6, c = 7).reshape(1, -1)

#w
w1 = np.amax(tnorm(Alinha, A1))
w2 = np.amax(tnorm(Alinha, A2))

#inferencia
Clinha = snorm(tnormT(w1, C1), tnormT(w2, C2))

#plot
plt.plot(x, np.squeeze(Clinha))
plt.show()
