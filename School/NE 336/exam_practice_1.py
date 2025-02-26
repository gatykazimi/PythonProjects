from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

M_init = 1000
S_init = 200

def dxdt (t,x):
    S,M = x[0],x[1]
    #dMdt, dSdt
    return (10, 10*0.2-M/S)

sol = solve_ivp(dxdt, [0,120], [S_init , M_init])


plt.plot(sol.y[0],sol.t)