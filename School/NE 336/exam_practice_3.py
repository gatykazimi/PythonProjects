import numpy as np
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt

R1 = 5E-2
R2 = 10E-2

Q =1E3
k = 14

T_R1 = 120 + 273


n = 5
r = np.linspace(R1, R2, n)
dx = (R2-R1)/n
lam = dx/(2*r)

A = np.diag(-2*np.ones(n-1))

for i in range(n-2):
    A[i,i+1] = 1+lam[i]
    A[i+1,i] = 1-lam[i+1]

A[-1,-3] = 1
A[-1,-2] = -4
A[-1,-1] =3

b = np.zeros(n-1)
b[0] = -T_R1*(1-lam[0])
b[-1] = -dx*Q/(k*np.pi*R2)


lu, piv = lu_factor(A)
T = np.zeros(n)
T[0] = T_R1
T[1:n] = lu_solve((lu,piv),b)
print(T)

plt.plot(r,T)


