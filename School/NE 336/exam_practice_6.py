from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

L = 20
dx = 2
alpha = 0.081
t_end = 1460
n = int(L/dx+1)

def dTdt (t, T):
    T_0 = 10-14*np.cos(2*np.pi/365*(t-37))
    dT = np.zeros(T.size)
    dT[0] = alpha/dx**2*(T[1]-2*T[0]+T_0)
    dT[1:-1]= alpha/dx**2*(T[2:]-2*T[1:-1]+T[:-2])
    dT[-1] = 0
    return dT

T0 = 10*np.ones(n)
sol = solve_ivp(dTdt,[0,t_end],T0)

T_0 = lambda t: 10-14*np.cos(2*np.pi/365*(t-37))

temp = np.vstack([T_0(sol.t),sol.y])

x = np.linspace(0,L,n+1)
plt.plot(x,temp[:,-1])
