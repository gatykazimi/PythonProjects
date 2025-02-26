import numpy as np
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt

#BCs
Vinitial = 0
Vleft = 0.2 #m/s



#y values
dy = 0.025
(y0,yend) = (0,0.1)
total_nodes_y = int((yend-y0)/dy+1)
y_val = np.linspace(y0,yend,total_nodes_y+1)

#t values
dt = 0.1
(t0,tend) = (0,12)
total_nodes_t = int((tend-t0)/dt)
t_val = np.linspace(t0,tend,total_nodes_t+1)


#Constants
rho = 994.6 #kg/m^3
mu = 0.8931 #kg/s
lam = (mu*dt)/(2*rho*dy**2)

#Initial matrix
vx = np.zeros((total_nodes_t+1,total_nodes_y+1))

#Add BCs
vx[0,1:-1]=Vinitial
vx[:,0]=Vleft
#vx[:,-1]=Vright
#Create A matrix for solving
A=np.diag((1+2*lam)*np.ones(total_nodes_y-1))+\
  np.diag(-lam*np.ones(total_nodes_y-2),1)+\
  np.diag(-lam*np.ones(total_nodes_y-2),-1)
A[-1,total_nodes_y-3]=A[-1,total_nodes_y-3]*2

#Create b vector for solving
b = np.zeros((total_nodes_y-1))

#solve matrix
lu, piv = lu_factor(A)
for l in range (0,total_nodes_t-1):
    
    for i in range (0,total_nodes_y-2):
        b[i]=lam*vx[l,i]+(1-2*lam)*vx[l,i+1]+lam*vx[l,i+2]
        if i == total_nodes_y-2:
            b[i]=2*lam*vx[l,i-1]+(1-2*lam)*vx[l,i]
    #Account for BCs
    b[0]+=lam*vx[0,0]
    
    vx[l+1,1:-1]= lu_solve((lu, piv), b)
    #if (l>0 and vx[l,2]==vx[l-1,2]):
    #    print(l)

print(vx)

check = lam*2
if check<0.5:
    print("Warning: oscillations may occurs")
    


plt.figure()
snap1=5
snap2,snap3=2*snap1,3*snap1

plt.plot(y_val,vx[snap1,:], label = f"when t={t_val[snap1]}")
plt.plot(y_val,vx[snap2,:], label = f"when t={t_val[snap2]}")
plt.plot(y_val,vx[snap3,:], label = f"when t={t_val[snap3]}")

plt.xlabel("y")
plt.ylabel("Vx")
plt.title("Vx as a function of position")
plt.legend(title="Time")

plt.figure()
snap1=1
snap2,snap3=2*snap1,3*snap1

plt.plot(t_val,vx[:,snap1], label = f"when y={y_val[snap1]}")
plt.plot(t_val,vx[:,snap2], label = f"when y={y_val[snap2]}")
plt.plot(t_val,vx[:,snap3], label = f"when y={y_val[snap3]}")

plt.xlabel("t")
plt.ylabel("Vx")
plt.title("Vx as a function of time")
plt.legend(title="Position")
