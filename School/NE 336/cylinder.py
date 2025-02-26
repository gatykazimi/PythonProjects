# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:46:09 2024

@author: gatyk
"""
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def dgdx (r,x):
    [T,u]=x
    dxdr = [u,-u/r]
    return dxdr

def bcs (xa,xb):
    return [xa[0]-120,xb[0]-60]

x = np.linspace(5,10,100)
y = np.zeros([2,x.size])

solt = solve_bvp(dgdx,bcs,x,y)
plt.plot(solt.x,solt.y[0], lw=0.5)
plt.title("Temperature in a cylinder")
plt.xlabel("Radius")
plt.ylabel("Temperature")
