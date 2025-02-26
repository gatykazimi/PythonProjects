import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#BCs
Uinitial = 0
Uright = 1 #m/s

#r values
dr = 0.2
(r0,rend) = (0,1)
n = int((rend-r0)/dr+1)
r_val = np.linspace(r0,rend,n)

#z values
(z0, zend) = (0, 1.0)  
dz = 0.01  

#Constants
lam = 1/(2*dr)
beta = [0]
for c in range (1,n-1):
    bet1 = 1/(r_val[c]*(dr**2))
    beta.append(bet1)

def dUdz(z,U):
    
    U_all=np.hstack([U,Uright])
    
    U_0= (4*U_all[0]-U_all[1])/3 
        
    U_all_new=np.hstack([U_0,U_all])
    dU=np.zeros(n)
    
    for i in range (1,n-1):
        dU[i]=U_all_new[i+1]*(lam+beta[i])-2*U_all_new[i]*(beta[i])+U_all_new[i-1]*(-lam+beta[i])
        
    return dU

#use solve_ivp to solve
sol=solve_ivp(dUdz,[z0,zend],Uinitial*np.ones(n),z_eval=np.linspace(z0,zend,int(zend/dz)+1))


U_begin= (4*sol.y[0,:]-sol.y[1,:])/3
sol_full=np.vstack([U_begin,
              sol.y,
              Uright*np.ones(sol.t.size)])

print(sol_full)
#plt.plot(r_val,sol_full[:,1],label='z='+str(sol.t[1])+'s')
