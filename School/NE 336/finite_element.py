import numpy as np

A = np.diag((0.8)*np.ones(5))+\
    np.diag(-0.4*np.ones(4),1)+\
    np.diag(-0.4*np.ones(4),-1)

A[1,0]=0
A[-1,-1]=-1
A[-2,-1]=0
A[0,0]=1


b = np.array([[-11.25],[67.5],[37.5],[97.5],[-41.25]])

T = np.linalg.solve(A,b)
print(T)