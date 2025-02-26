import numpy as np
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt

#BCs
Uinitial = 0
Uright = 1 #m/s

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

beta = [0]
#Constants
lam = (dr**2)/dz
for c in range (total_nodes_r-1):
    bet1 = dr/(4*r_val[c+1])
    beta.append(bet1)

#Initial matrix
u = np.zeros((total_nodes_z,total_nodes_r))

#Add BCs
u[0,1:-1]=Uinitial
u[:,-1]=Uright

#Create A matrix for solving
A=np.diag((1+lam)*np.ones(total_nodes_r-1))+\
  np.diag(-0.5*np.ones(total_nodes_r-2),1)+\
  np.diag(-0.5*np.ones(total_nodes_r-2),-1)

for c in range (total_nodes_r-2):
    A[c+1,c]+=beta[c+1]
    if c<3:
        A[c+1,c+2]+=-beta[c+1]

A[0,0]=3
A[0,1]=-4
A[0,2]=1

#Create b vector for solving
b = np.zeros((total_nodes_r-1))
b[-1]=0.5+beta[-1]

#solve matrix
lu, piv = lu_factor(A)

for l in range (0,total_nodes_z-1):
    
    for i in range (0,total_nodes_r-2):
        b[i+1]=(0.5-beta[i+1])*u[l,i]+(lam-1)*u[l,i+1]+(0.5+beta[i+1])*u[l,i+2]
    #Account for BCs
    b[0]=-3*u[l,0]+4*u[l,1]-u[l,2]
    b[-1]+=0.5+beta[-1]
    u[l+1,:-1]= lu_solve((lu, piv), b)

plt.figure()
snap1=20
snap2,snap3,snap4=2*snap1,3*snap1,4*snap1

plt.plot(r_val,u[snap1,:], label = f"when z={round(z_val[snap1],2)}")
plt.plot(r_val,u[snap2,:], label = f"when z={round(z_val[snap2],2)}")
plt.plot(r_val,u[snap3,:], label = f"when z={round(z_val[snap3],2)}")
plt.plot(r_val,u[snap4,:], label = f"when z={round(z_val[snap4],2)}")

plt.xlabel("r")
plt.ylabel("U")
plt.title("U as a function of radius")
plt.legend(title="Height")

snap1=1
snap2,snap3,snap4=2*snap1,3*snap1,4*snap1
plt.figure()
plt.plot(z_val,u[:,snap1], label = f"when r={r_val[snap1]}")
plt.plot(z_val,u[:,snap2], label = f"when r={r_val[snap2]}")
plt.plot(z_val,u[:,snap3], label = f"when r={round(r_val[snap3],2)}")
plt.plot(z_val,u[:,snap4], label = f"when r={r_val[snap4]}")

plt.xlabel("z")
plt.ylabel("U")
plt.title("U as a function of height")
plt.legend(title="Radius")


