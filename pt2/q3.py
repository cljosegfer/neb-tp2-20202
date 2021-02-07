import sys
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


def create_con(px=None, py=None, n_points=None):

    if px is not None: # caso onde px eh passado

        pass

    else:

        px = np.linspace(0, 2*p, n_points)
        py = [np.sin(x) for x in px]

    n_consequents = len(px) - 1
    con = []

    for i in range(n_consequents):
        l = Linear(compute=True, data=(px[i:i+2], py[i:i+2])) #consequentes de ordem 1
        con.append(l)

    return con, n_consequents

def create_ant(px, n_cons, gs=None, tri=True):

    centers = np.linspace(px[0], px[-1], n_consequents)

    s = (px[1] - px[0])*2

    if tri:

       ant = [Trimf(c-s, c, c+s) for c in centers]

    else:
        ant = [Gaussmf(c, gs) for c in centers]

    return ant, centers, s

def see_inference(px, con, ant, centers, s, mse):

# Plot de consequentes

    for cc, cons in enumerate(con[:-1]):
        cons.plot(px[cc], px[cc+1])

    con[-1].plot(px[n_consequents - 1], px[n_consequents], legend="Consequentes")

# plotta antecedentes
# antecentedes iniciais e finais sao clippados para o dominio de interesse

    first_c = centers[0]
    last_c = centers[len(centers)-1]

    ant[0].plot(first_c, first_c + s, c="blue")

    ant[len(ant) - 1].plot(last_c - s, last_c, c="blue", legend="Antecedentes")

    for (a, c) in zip(ant[1:n_consequents-1], centers[1:n_consequents-1]):
        a.plot(c - s, c + s, c="blue")
    plt.plot(x, y, c="black", label="Função aproximada")
    plt.plot(x, y_hat,"--", c="black", label="Aproximação")

    plt.plot([], label = f"Erro: {mse:.3f}", c="white")

    plt.legend()
    plt.show()

# define uso de triangular ou gaussiana

tri = int(sys.argv[1])

# letra a e b

# Criando consequentes: 3 regras

# Define-se os pontos manualmente (ou por uma funcao como np.arange)
# e para cada par de pontos uma reta é criada

# letra a

p = 3.14

auto_point = False

if auto_point:
    n_points = 10
    px = np.linspace(0, 2*p, n_points)
    py = [np.sin(x) for x in px]
else:
    px = [0, p/2, 3*p/2, 2*p]
    py = [np.sin(x) for x in px]

con, n_consequents = create_con(px, py) # cria consequentes

# Criando antecedentes

ant, centers, s = create_ant(px, n_consequents, tri=tri)

# inferindo

sugeno = Sugeno(ant, con)

x = np.linspace(px[0], px[n_consequents], 500)
y = [np.sin(_x) for _x in x]
y_hat = np.array([sugeno.infer(_x) for _x in x])

# calculando erro

mse = np.sum((y - y_hat) ** 2)


see_inference(px, con, ant, centers, s, mse)
