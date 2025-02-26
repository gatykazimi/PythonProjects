# -*- coding: utf-8 -*-
"""
Gaty Kazimi
20956021
"""

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

sigma = 10
beta = 8/3
r = [14,15,28,96.98]

def dxdydz(_,j, rho):
    [x,y,z]=j
    dxdt = sigma*(y-x)
    dydt = rho*x-y-x*z
    dzdt = x*y-beta*z
    
    return [dxdt, dydt, dzdt]

xyz_init = (0,1,0)
t_range = [0,100]

for i in range(0,4):
    solb = solve_ivp(dxdydz,t_range,xyz_init, args=[r[i]])
    plt.subplots()
    xyz_val = solb.y
    t_val = solb.t
    plt.plot(t_val,xyz_val[0], label ="x", lw=0.5)
    plt.plot(t_val,xyz_val[1], label = "y", lw=0.5)
    plt.plot(t_val,xyz_val[2], label = 'z', lw=0.5)
    plt.legend (title = "variable")
    plt.title("Lorenz Attractor when rho = "+str(r[i]))
    plt.xlabel("t")
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(xyz_val[0], xyz_val[1],xyz_val[2], lw=0.5)
    ax.set_title("Lorentz Attractor when rho = " +str(r[i]))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

# part b)
solb = solve_ivp(dxdydz,t_range,xyz_init, args=[28])
xyz_val = solb.y
t_val = solb.t
ax = plt.figure().add_subplot(projection='3d')
ax.plot(xyz_val[0], xyz_val[1],xyz_val[2], lw=0.5)
ax.set_title("Lorenz Attractor when rho = "+str(28)+ " Before")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")


solb = solve_ivp(dxdydz,t_range,(0.001,1,0), args=[28])
xyz_val = solb.y
t_val = solb.t
ax = plt.figure().add_subplot(projection='3d')
ax.plot(xyz_val[0], xyz_val[1],xyz_val[2], lw=0.5)
ax.set_title("Lorenz Attractor when rho = "+str(28)+ " After")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

#When the x value is increased by a small amount, the hole closer
#to the y axis becomes smaller.