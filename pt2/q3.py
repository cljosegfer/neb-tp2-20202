import numpy as np
from numpy import polyfit
from sugeno import Sugeno
from matplotlib import pyplot as plt

plt.style.use("ggplot")

class Linear:

    def __init__(self, b=None, m=None, compute=False, data=None):

        self.b = b
        self.m = m

        if compute:
            self.m, self.b = np.polyfit(data[0], data[1], 1)

    def infer(self, x):
        return x*self.m + self.b

    def plot(self, b=0, e=1, show=False, c="red", legend=None):
        x = np.linspace(b, e, 500)
        y = [self.infer(_x) for _x in x]

        if legend is not None:
            plt.plot(x, y, c=c, label=legend)

        plt.plot(x, y, c=c)

        if show:
            plt.show()

class Gaussmf(Linear):

    def __init__(self, c, sigma):
        self.c = c
        self.sigma = sigma

    def infer(self, x):
        return np.exp(-np.power(x - self.c, 2.) / (2 * np.power(self.sigma, 2.)))

class Trimf(Linear):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def infer(self, x):

        if x <= self.a:
            return 0
        if x <= self.b:
            return (x-self.a)/(self.b-self.a)
        if x <= self.c:
            return (self.c-x)/(self.c-self.b)

        return 0

# define uso de triangular ou gaussiana

tri = False

# letra a e b

# Criando consequentes: 3 regras

# Define-se os pontos manualmente (ou por uma funcao como np.arange)
# e para cada par de pontos uma reta é criada

# letra a

p = 3.14

auto_point = False

if auto_point:
    n_points = 4
    px = np.linspace(0, 2*p, n_points)
    py = [np.sin(x) for x in px]
else:
    px = [0, p/2, 3*p/2, 2*p]
    py = [0, 1, -1, 0]

n_consequents = len(px) - 1
con = []

for i in range(n_consequents):
    l = Linear(compute=True, data=(px[i:i+2], py[i:i+2])) #consequentes de ordem 1
    con.append(l)

con[0].plot(px[0], px[1])
con[1].plot(px[1], px[2])
con[2].plot(px[2], px[3], legend="Consequentes")

# Criando antecedentes

if tri:

    t1 = Trimf(-p, 0, p)
    t2 = Trimf(0, p, 2*p)
    t3 = Trimf(p, 2*p, 3*p)

else:

    s = 1.2
    t1 = Gaussmf(0, s)
    t2 = Gaussmf(p, s)
    t3 = Gaussmf(p*2, s)

ant = [t1, t2, t3]

t1.plot(px[0], px[3]/2, c="blue")
t2.plot(px[0], px[3], c="blue")
t3.plot(px[3]/2, px[3], c="blue", legend="Antecedentes")

# inferindo

sugeno = Sugeno(ant, con)

x = np.linspace(px[0], px[3], 500)
y = [np.sin(_x) for _x in x]
y_hat = np.array([sugeno.infer(_x) for _x in x])

plt.plot(x, y, c="black", label="Função aproximada")
plt.plot(x, y_hat,"--", c="black", label="Aproximação")

# calculando erro

mse = np.sum((y - y_hat) ** 2)

plt.plot([], label = f"Erro: {mse:.3f}", c="white")

plt.legend()
plt.show()

# letra b: redefine antecedentes gaussianos apenas
