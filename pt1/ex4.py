import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sigma):
    b = - 1 / 2 / sigma / sigma
    arg = np.power(x - mu, 2)
    
    result = np.exp(b * arg)
    return result

li = 0
ls = 100
n = 100
x = np.linspace(start = li, stop = ls, num = n)
young = gaussian(x = x, mu = 0, sigma = 20)
old = gaussian(x = x, mu = 100, sigma = 30)
vyoung = np.power(young, 2)
vold = np.power(old, 2)

a = np.minimum(1 - vyoung, 1 - vold)
b = np.minimum(vyoung, vold)

plt.plot(x, a)
plt.plot(x, b)
plt.show()

plt.plot(x, vyoung)
plt.plot(x, vold)
plt.show()