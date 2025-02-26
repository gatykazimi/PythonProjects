from scipy.integrate import solve_ivp, solve_bvp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

D = 1.2E-9
k=0.001
CA_init = 0.2
L=0.001

def dfdx (x, f):
    [CA, u] = f
    return [u,k/D*CA]

def BCs (fa, fb):
    return [fa[0]-CA_init, fb[1]]

def forsolver(y_val):
    sol = solve_ivp(dfdx, [0,L], [CA_init,y_val[0]])
    return sol.y[1,-1] 

y_correct = fsolve(forsolver,-1)


sol1 = solve_ivp(dfdx, [0,L], [CA_init, y_correct[0]], t_eval=np.linspace(0,L,1000))

plt.plot(sol1.t,sol1.y[0])

x = np.linspace(0,L,1000)
CA = np.zeros([2,x.size])
sol2 = solve_bvp(dfdx, BCs, x, CA)

plt.plot(sol2.x,sol2.y[0])