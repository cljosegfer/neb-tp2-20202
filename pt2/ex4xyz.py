import numpy as np
from pertinencia import trimf, gaussmf
from sugeno import Sugeno
import matplotlib.pyplot as plt

def tnormT(U, V):
    #min
    mesh = np.array(np.meshgrid(U, V))
    combinations = mesh.T.reshape(-1, 2)
    # return np.amin(combinations, axis = 1).reshape(U.size, V.size)
    return np.amin(combinations, axis = 1)

# x1, x2: food / service, y : tip
x1 = np.linspace(start = 0, stop = 1, num = 100)
x2 = np.linspace(start = 0, stop = 1, num = 100)

#antecedentes
#x1
lim = 0.35      #ajuste manual
# ma = trimf(x = x1, a = 0 - lim, b = 0, c = 0 + lim)
ma = gaussmf(x = x1, c = 0, sigma = lim)
# boa = trimf(x = x1, a = 0.5 - lim, b = 0.5, c = 0.5 + lim)
boa = gaussmf(x = x1, c = 0.5, sigma = lim)
# deliciosa = trimf(x = x1, a = 1 - lim, b = 1, c = 1 + lim)
deliciosa = gaussmf(x = x1, c = 1, sigma = lim)

#x2
lim = 0.35      #ajuste manual
# ruim = trimf(x = x2, a = 0 - lim, b = 0, c = 0 + lim)
ruim = gaussmf(x = x2, c = 0, sigma = lim)
# bom = trimf(x = x2, a = 0.5 - lim, b = 0.5, c = 0.5 + lim)
bom = gaussmf(x = x2, c = 0.5, sigma = lim)
# excelente = trimf(x = x2, a = 1 - lim, b = 1, c = 1 + lim)
excelente = gaussmf(x = x2, c = 1, sigma = lim)

#consequentes
grid = np.array([(orde, absc) for orde in x1 for absc in x2])

p1 = (0.15 - 0.05) / 0.25
q1 = 0.05
y1 = p1 * (grid[:, 0] + grid[:, 1]) + q1

p2 = 0
q2 = 0.15
y2 = p2 * grid[:, 1] + q2

p3 = (0.25 - 0.15) / 0.25
q3 = - 0.15
y3 = p3 * (grid[:, 0] + grid[:, 1]) + q3

#sugeno
ant = list([tnormT(ruim, ma), 
            tnormT(bom, np.zeros(shape = deliciosa.shape)), 
            tnormT(excelente, deliciosa)])
con = list([y1, y2, y3])

model = Sugeno(consequents = con, antecedents = ant)
yhat = model.inferbycurve()    #como to aplicando antes n importa o argumento

#plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(grid[:, 0], grid[:, 1], yhat)