import numpy as np

def trimf(x, a, b, c):
    mu = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] <= a:
            mu[i] = 0
        elif x[i] <= b:
            mu[i] = (x[i] - a) / (b - a)
        elif x[i] <= c:
            mu[i] = (c - x[i]) / (c - b)
        else:
            mu[i] = 0
    return mu

def trapmf(x, a, b, c, d):
    mu = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] <= a:
            mu[i] = 0
        elif x[i] <= b:
            mu[i] = (x[i] - a) / (b - a)
        elif x[i] <= c:
            mu[i] = 1
        elif x[i] <= d:
            mu[i] = (d - x[i]) / (d - c)
        else:
            mu[i] = 0
    return mu

def gaussmf(x, c, sigma):
    mu = np.exp(-1 / 2 * ((x - c) / sigma) ** 2)
    return mu

def gbellmf(x, a, b, c):
    mu = 1 / (1 + abs((x - c) / a) ** (2 * b))
    return mu

def sigmf(x, a, c):
    mu = 1 / (1 + np.exp(-a * (x - c)))
    return mu