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

# Criando consequentes

p = 3.14
px = [-p/2, 0, p, 3*p/2]
py = [0, 1, -1, 0]

l1 = Linear(compute=True, data=(px[:2], py[:2]))
l2 = Linear(compute=True, data=(px[1:3], py[1:3]))
l3 = Linear(compute=True, data=(px[2:], py[2:]))

con = [l1, l2, l3]

l1.plot(-p/2, 0)
l2.plot(0, p)
l3.plot(p, 3*p/2, legend="Consequentes")

# Criando antecedentes

t1 = Trimf(-3*p/2, -p/2, p/2)
t2 = Trimf(-p/2, p/2, 3*p/2)
t3 = Trimf(p/2, 3*p/2, 4*p/2)

ant = [t1, t2, t3]

t1.plot(-p/2, p/2, c="blue")
t2.plot(-p/2, 3*p/2, c="blue")
t3.plot(p/2, 3*p/2, c="blue", legend="Antecedentes")

# inferindo

sugeno = Sugeno(ant, con)

x = np.linspace(-p/2, 3*p/2)
y = [np.cos(_x) for _x in x]
y_hat = [sugeno.infer(_x) for _x in x]

plt.plot(x, y, c="black", label="Função aproximada")
plt.plot(x, y_hat,"--", c="black", label="Aproximação")

plt.legend()
plt.show()

