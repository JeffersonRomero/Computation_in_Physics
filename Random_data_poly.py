import numpy as np
import matplotlib.pyplot as plt
import random as rd

n = 6               # Grado del polinomio
a=np.zeros((n+1,))

x = np.linspace(-1,1,101)
y = np.zeros_like(x)
sigma = (2*np.random.rand(len(x))-1)/50

for i in range(n+1):
    a[i] = rd.uniform(-1,1)
    y += a[i]*x**i

y += sigma

p = np.polyfit(x,y,n)
poly = np.poly1d(p)(x)

plt.plot(x,y)
plt.plot(x,poly)
plt.show()

print(a)
print(np.flip(p))

f = np.transpose([x,y])
np.savetxt('Polynomial_Data.dat',f)
