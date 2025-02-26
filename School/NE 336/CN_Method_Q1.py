import numpy as np
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt

#r values
dr = 0.2
(r0,rend) = (0,1)
total_nodes_r = int((rend-r0)/dr+1)
r_val = np.linspace(r0,rend,total_nodes_r)

#z values
dz = 0.01
(z0,zend) = (0,1)
total_nodes_z = int((zend-z0)/dz)
z_val = np.linspace(z0,zend,total_nodes_z)

#Constants
lam = (dr**2)/dz

#Initial matrix
u = np.zeros((total_nodes_z,total_nodes_r))

#Add BCs
u[:,-1] = 1

#Create A matrix for solving
A = [[3,-4,1,0,0],
     [dr/(4*r_val[1])-0.5, lam+1, -dr/(4*r_val[1])-0.5,0,0],
     [0,dr/(4*r_val[2])-0.5, lam+1, -dr/(4*r_val[2])-0.5,0],
     [0,0,dr/(4*r_val[3])-0.5, lam+1, -dr/(4*r_val[3])-0.5],
     [0,0,0,dr/(4*r_val[4])-0.5, lam+1],]


#Create b vector for solving
b = np.zeros((total_nodes_r-1))
b[-1] = 0.5+(dr/(4*r_val[-1]))

#solve matrix
lu, piv = lu_factor(A)

for l in range (0,total_nodes_z-1):
    
    for i in range (0,total_nodes_r-2):
        
        beta = (dr/(4*r_val[i+1]))
        b[i+1]=(0.5-beta)*u[l,i]+(lam-1)*u[l,i+1]+(0.5+beta)*u[l,i+2]
        
    #Account for BCs
    b[0]=-3*u[l,0]+4*u[l,1]-u[l,2]
    b[-1]+=0.5+(dr/(4*r_val[-1]))
    
    u[l+1,:-1]= lu_solve((lu, piv), b)

plt.figure()


plt.plot(r_val,u[20,:], label = "z=0.2")
plt.plot(r_val,u[40,:], label = "z=0.4")
plt.plot(r_val,u[60,:], label = "z=0.6")
plt.plot(r_val,u[80,:], label = "z=0.8")

plt.xlabel("r")
plt.ylabel("U")
plt.title("U(r)")
plt.legend(title="Time")


