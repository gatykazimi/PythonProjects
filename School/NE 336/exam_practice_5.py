from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

D = 1.5E-9 *1e6**2
k = 35
L = 50
C_0 = 0.03


def dCdx (x,f):
    [C,u] = f
    return [u,k/D*C]

def for_solver (u0):
    sol = solve_ivp(dCdx, [0, L],[C_0,u0[0]])
    return np.abs(sol.y[1,-1])

y_val = fsolve(for_solver, -10)

sol = solve_ivp(dCdx, [0,L], [C_0,y_val])

plt.plot(sol.t,sol.y[0])
