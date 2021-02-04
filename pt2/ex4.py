import numpy as np
from scipy.special import logit
from sugeno import Sugeno
import matplotlib.pyplot as plt

def gorjeta(x):
    #logistic-1 melhor funcao? logit = c + k * ln(x / ( 1 - x ) )
    k = 0.025
    c = 0.15
    return c + k * logit(x)

# def algumadistribuicao(centro, par):
#     #gauss, tri, trap
#     return mf

def derivada(x):
    k = 0.025
    return - k / x / (x - 1)

def linear(x, p, q):
    return p * x + q

#geracao
start = 0.01
stop = 0.99
num = 1000
x = np.linspace(start, stop, num)
y = gorjeta(x)
plt.plot(x, y)

#antecedentes, n = 3
mu = [start, (start + stop) / 2, stop]
# par = ['sd1', 'lim2', 'lim3']
# ant = algumadistribuicao(mu, par)

#consequentes
p = [derivada(mu[0]),
     derivada(mu[1]),
     derivada(mu[2])]
q = [gorjeta(mu[0]) - p[0] * mu[0],
     gorjeta(mu[1]) - p[1] * mu[1],
     gorjeta(mu[2]) - p[2] * mu[2]]
con = list()
for i in range(len(p)):
    consq = linear(x, p[i], q[i]).reshape(-1, 1)
    con.append(consq)

#retas
# plt.plot(x, con[0])
plt.plot(x, con[1])
# plt.plot(x, con[2])

#sugeno
# model = Sugeno(ant, con)

#erro
# yhat = Sugeno.infer(x)
# erro = y - yhat
# mse = np.sum(erro ** 2)

#plot
# plt.plot(x, yhat)
plt.show()
