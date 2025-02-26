# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:33:22 2024

@author: gatyk
"""
import matplotlib.pyplot as plt
import numpy as np

c0 = 0.01
kap = 1/((3.04/np.sqrt(c0)*(10**-10)))

sol_lin = lambda x: 0.4*np.exp((-kap*x))

coeff = (2*(1.38E-23)*298)/(1.6022E-19)
y0 = (1.6022E-19*0.4)/(1.38E-23*298)
ey0 = np.exp(y0/2)

sol_exact = lambda x: coeff*np.log((ey0+1+(ey0-1)*np.exp(-kap*x))/(ey0+1-(ey0-1)*np.exp(-kap*x)))


x = np.linspace(0,10**-8, 50)
y_lin = []
y_exact = sol_exact(x)

#plt.plot(x,sol_lin(x), label = "Linear solution")
#plt.plot(x,sol_exact(x), label = "Exact solution")
#plt.legend(title = "Solution type")
#plt.xlabel("x")
#plt.ylabel("$\psi$")
#plt.title(f"$\psi$ vs x distance when conc. = {c0} M")

cat_conc_lin=c0*np.exp(-(1.6022E-19*sol_lin(x))/(1.38E-23*298))
cat_conc_exact=c0*np.exp(-(1.6022E-19*y_exact)/(1.38E-23*298))
#print((1.6022E-19*sol_lin(x[0]))/(1.38E-23*298))
#plt.yscale("log")
#plt.plot(x,cat_conc_lin, label = "Linear solution")
#plt.plot(x,cat_conc_exact, label = "Exact solution")
#plt.legend(title = "Solution type")
#plt.xlabel("x")
#plt.ylabel("Cations")
#plt.title(f"Cation conc. vs x distance when conc. = {c0} M")

an_conc_lin=c0*np.exp((1.6022E-19*sol_lin(x))/(1.38E-23*298))
an_conc_exact=c0*np.exp((1.6022E-19*y_exact)/(1.38E-23*298))
#plt.yscale("log")
#plt.plot(x,an_conc_lin, label = "Linear solution")
#plt.plot(x,an_conc_exact, label = "Exact solution")
#plt.legend(title = "Solution type")
#plt.xlabel("x")
#plt.ylabel("Anions")
#plt.title(f"Anion conc. vs x distance when conc. = {c0} M")

print(c0*np.exp((1.6022E-19*sol_lin(3E-10))/(1.38E-23*298))+c0*np.exp(-(1.6022E-19*sol_lin(3E-10))/(1.38E-23*298)))
print(c0*np.exp((1.6022E-19*sol_exact(3E-10))/(1.38E-23*298))+c0*np.exp(-(1.6022E-19*sol_exact(3E-10))/(1.38E-23*298)))

