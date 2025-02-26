from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

Vleft = 0.2 #m/s

rho = 994.6 #kg/m^3
mu = 0.8931 #kg/s
y_end = 0.1
dy = 0.025
n = int(y_end/dy)
rat = mu/(rho*dy**2)

def dvdt(y,v):
    dv = np.zeros(v.size)
    dv[0] = rat*(v[1]-2*v[0]+Vleft)
    dv[1:-1]= rat*(v[2:]-2*v[1:-1]+v[:-2])
    dv[-1] = rat*(-2*v[-1]+v[-2])
    return dv
    
sol = solve_ivp(dvdt,[0,12], Vleft*np.ones(n+1))

vx = np.vstack([Vleft*np.ones(sol.t.size),sol.y])

plt.plot(np.linspace(0,y_end, n+2),vx[:,5])
plt.plot(np.linspace(0,y_end, n+2),vx[:,10])
plt.plot(np.linspace(0,y_end, n+2),vx[:,15])
