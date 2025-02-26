import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp,solve_bvp
from scipy.optimize import fsolve

k = 10 #cm^3/mol s
DA = 10**-3 #cm^2/s
C0 = 10**-3 #mol/cm^3
L = 1 #cm

#Define ODE function
def dfdx (_, f):
    # f is the vector [CA, u]
    # where u id dCA/dx
    # so dfdx is [u, k/DA CA^2]
    
    CA = f[0]
    u = f[1]
    df = [u, k/DA*CA**2]
    
    return df
#Define boundary conditions
def BCs (fa, fb):
    bc1 = fa[0]- C0
    bc2 = fb[1] - 0
    return [bc1,bc2]
#For IVP method
def forsolver(y_val):
    sol = solve_ivp(dfdx,(0,L),[C0,y_val[0]])
    return sol.y[1,-1]
#Solve for boundary conditions, use ivp to solve
C_A = fsolve(forsolver, [-0.001])
sol1 = solve_ivp(dfdx,(0,L),[C0, C_A[0]])

C = np.linspace(0,L)
x = np.zeros((2,C.size))

sol2 = solve_bvp(dfdx,BCs,C,x)

plt.figure()
plt.plot(sol2.x,sol2.y[0],label = 'solve_bvp')
plt.scatter(sol1.t,sol1.y[0],label = 'solve_ivp', marker='x',color = 'r')
plt.title("Solution to ordinary differential equation")
plt.legend()
plt.xlabel('x')
plt.ylabel('C')

