from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

D = 1.5E-9 *1e6**2
k = 35
L = 50
C_0 = 0.03
n = 9
dx = L/(n+1)
t0 = 0.1

def dCdx(x,C):
    dC = np.zeros(C.size)
    dC[0] = D/(dx**2)*(C[1]-2*C[0]+C_0)-k*C[0]
    dC[1:-1] = D/(dx**2)*(C[2:]-2*C[1:-1]+C[:-2])-k*C[1:-1]
    dC[-1] = 2*D/(dx**2)*(C[-2]-C[-1])-k*C[-1]
    return dC


sol = solve_ivp(dCdx,[0,L], np.zeros(n+1))
conc = np.vstack([C_0*np.ones(sol.t.size),sol.y])

x=np.linspace(0,L,n+2)
plt.plot(x,conc[:,-1])