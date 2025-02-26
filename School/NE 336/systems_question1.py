# Gaty Kazimi
# 20956021

import numpy as np
from scipy import linalg

A= np.array([[2,-6,-1],[-3,-1,7],[-8,1,-2]])
b= np.array([[-38,-34,-20]]).T
# Solve by LU Decomposition
p, L, U =linalg.lu(A) #get p, L, and U
d=linalg.solve(p@L,b) #find d vector
x=linalg.solve(U,d)  #solve for x
#print (x)
#Return:
#  [[ 4.]
#   [ 8.]
#   [-2.]]
#Advantage: the p@L takes care of non diagonally dominant matrices, so it
# is less tedious than the Gaussian Elimation method
#Disadvantage: Takes up more memory than other methods

# Solve by builtin linalg.solve method
x=np.linalg.solve(A,b) 
#print (x)
#Return:
#  [[ 4.]
#   [ 8.]
#   [-2.]]
#Advantage: only one line of code! Does not take up much memory or time
#Disadvantage: can not be used to solve larger matrices

# Solve by inverse method
a=np.linalg.inv(A) #get inverse of matrix A
x = a@b #matrix multiplication
#print(x)
#Return:
#  [[ 4.]
#   [ 8.]
#   [-2.]]
#Advantage: calculation wise, is much more simple than the other methods
#Disadvantage: takes up more memory and computing time than linal.solve method
# Also, it can be difficult to obtain the inverse of a complex or large matrix 

#Gauss-Seidel Method Check
A= np.array([[-8,1,-2],[2,-6,-1],[-3,-1,7]])
b= np.array([[-20,-38,-34]]).T
x = [0, 0, 0]
err = [1,1,1]
for i in range(0,2):
    x0=(b[0]-A[0,1]*x[1]-A[0,2]*x[2])/A[0,0]
    x1=(b[1]-A[1,0]*x[0]-A[1,2]*x[2])/A[1,1]
    x2=(b[2]-A[2,0]*x[0]-A[2,1]*x[1])/A[2,2]
    
    err[0]=abs((x0[0]-x[0])/x0[0])
    err[1]=abs((x1[0]-x[1])/x1[0])
    err[2]=abs((x2[0]-x[2])/x2[0])
    x[0]=x0[0]
    x[1]=x1[0]
    x[2]=x2[0]
    print(x)
    
