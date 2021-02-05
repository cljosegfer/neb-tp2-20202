import numpy as np
from pertinencia import trimf, gaussmf
from sugeno import Sugeno
import matplotlib.pyplot as plt

# x: food / service, y : tip, eh pra usar uma variavel so??
x = np.linspace(start = 0, stop = 1, num = 1000)

#antecedentes
lim = 0.35      #ajuste manual
# ruim = trimf(x = x, a = 0 - lim, b = 0, c = 0 + lim)
ruim = gaussmf(x = x, c = 0, sigma = lim)
# bom = trimf(x = x, a = 0.5 - lim, b = 0.5, c = 0.5 + lim)
bom = gaussmf(x = x, c = 0.5, sigma = lim)
# excelente = trimf(x = x, a = 1 - lim, b = 1, c = 1 + lim)
excelente = gaussmf(x = x, c = 1, sigma = lim)

#consequentes
p1 = (0.15 - 0.05) / 0.25
q1 = 0.05
y1 = p1 * x + q1

p2 = 0
q2 = 0.15
y2 = p2 * x + q2

p3 = (0.25 - 0.15) / 0.25
q3 = - 0.15
y3 = p3 * x + q3

#sugeno
ant = list([ruim, bom, excelente])
con = list([y1, y2, y3])

model = Sugeno(consequents = con, antecedents = ant)
yhat = model.infer(x)

plt.plot(x, yhat)