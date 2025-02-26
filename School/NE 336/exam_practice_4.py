from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
import numpy as np

T_init = 373
T_air = 293
L = 0.1
h = 20
k = 14

def dfdx (x,f):
    [T,u] = f
    r = lambda x: (0.02 - 0.1*x)
    rx = r(x)
    return [u, #2*h/(k*rx)*(T-Tair)+0.2*u/rx
            (2*h/(k*rx))*(T-T_air) ]

def BCs (fa,fb):
    return(fa[0] - T_init,
           h*(fb[0]-T_air) + k*fb[1])

x = np.linspace(0,L,100)
T = np.zeros((2,x.size))

sol = solve_bvp(dfdx,BCs,x,T)

plt.plot(sol.x,sol.y[0])