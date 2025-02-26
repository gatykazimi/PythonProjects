# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:54:32 2024

@author: gatyk
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Define differential function
dydt = lambda t,y: (1+4*t)*math.sqrt(y)

#Define step value and t range
delt = 0.25
(t0,tend)= (0,1)

#number of points
n = int((tend-t0)/delt+1)
t_val = np.linspace(t0,tend,n)

# initial y value at t=0
y_init = 1

#Analytical Solution
ya = lambda t: (0.5*t+t**2+1)**2


#Euler's Method
y_vale = [y_init]
for i in range(1,n):
    ynew = y_vale[i-1]+dydt(t_val[i-1],y_vale[i-1])*delt
    y_vale.append(ynew)

#print(y_vale)
# Result:
# y_val=    
#[1, 1.25, 1.8090169943749475, 2.8177647623208832, 4.496384660427921]

#Heun's Methods
y_valh = [y_init]
for i in range(1,n):
    ynew = y_valh[i-1]+dydt(t_val[i-1],y_valh[i-1])*delt
    y_valh.append(ynew)
    y_valh[i]=y_valh[i-1]+0.5*(dydt(t_val[i-1],y_valh[i-1])+dydt(t_val[i],y_valh[i]))*delt

#print(y_val)
#Result:
# y_val = 6
#[1, 1.4045084971874737, 2.2051622844178462, 3.6013393147809536, 5.875491584530215, 1.25, 1.9970683037022832, 3.318896447037023, 5.499058818496124]

#Ralston's Method
y_valr = [y_init]
for i in range(1,n):
    k1 = dydt(t_val[i-1],y_valr[i-1])
    ynew = y_valr[i-1]+(0.25*dydt(t_val[i-1],y_valr[i-1])+0.75*dydt(t_val[i-1]+(2/3)*delt,y_valr[i-1]+(2/3)*k1*delt))*delt
    y_valr.append(ynew)
#print(y_valr)
#Result:
# y_val = 
#[1, 1.4045084971874737, 2.2051622844178462, 3.6013393147809536, 5.875491584530215, 1.25, 1.9970683037022832, 3.318896447037023, 5.499058818496124, 1.400038578042076, 2.223384680168961, 3.663945777923356, 6.006029037526694]

#Range-Kutta Fourth Order
y_valrk = [y_init]
for i in range(1,n):
    k1 = dydt(t_val[i-1],y_valr[i-1])
    k2 = dydt(t_val[i-1]+delt/2,y_valr[i-1]+k1*delt/2)
    k3 = dydt(t_val[i-1]+delt/2,y_valr[i-1]+k2*delt/2) 
    k4 =  dydt(t_val[i-1]+delt,y_valr[i-1]+k3*delt)
    phi = (k1+2*k2+2*k3+k4)/6
    
    ynew = y_valrk[i-1]+phi*delt
    y_valrk.append(ynew)
#print(y_valrk)
#Result:
# y_val = 
#[1, 1.410089427625476, 2.247135099509534, 3.7413731885520747, 6.215661086287936]


#solve_ivp method
sol1 = solve_ivp(dydt,[t0,tend],[y_init])
y_valso = np.ravel(sol1.y)
t_valso = sol1.t
print(y_valso)
#Result:
# y_val = 
#[[1.         1.08672221 4.28155399 6.25092437]]

ta = np.linspace(t0,tend,50)
plt.plot(ta,ya(ta), label = "Analytical")
plt.scatter(t_val,y_vale, label ="Euler's", marker = "x")
plt.scatter(t_val,y_valh, label ="Heun's", marker = "x")
plt.scatter(t_val,y_valr, label ="Ralston's", marker = "x")
plt.scatter(t_val,y_valrk, label ="Range-Kutta Fourth Order", marker = "x")
plt.scatter(t_valso,y_valso, label ="solve_ivp", marker = "x")
plt.legend(title = "Method")
plt.xlabel("t")
plt.ylabel("x")
plt.title("Solutions to dy/dt")