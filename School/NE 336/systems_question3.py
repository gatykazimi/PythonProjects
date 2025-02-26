# Gaty Kazimi
# 20956021

import numpy as np
from scipy import linalg

#define variables
A= np.array([[0.2425,0,-0.9701],[0,0.2425,-0.9701],[-0.2357,-0.2357,-0.9428]])
b= np.array([[247,248,239]]).T

#Gauss-Seidel Method
x = [10, 10, 10] #initial guess
tol = 1e-6 #tolerance
err = [1,1,1] #error

#while max(err) > tol:
for i in range(0,5):
    #Gauss-Seidel Calculation
    x0=(b[0]-A[0,1]*x[1]-A[0,2]*x[2])/A[0,0]
    x1=(b[1]-A[1,0]*x[0]-A[1,2]*x[2])/A[1,1]
    x2=(b[2]-A[2,0]*x[0]-A[2,1]*x[1])/A[2,2]
    #Calculate error
    err[0]=abs((x0[0]-x[0])/x0[0])
    err[1]=abs((x1[0]-x[1])/x1[0])
    err[2]=abs((x2[0]-x[2])/x2[0])
    #redefine x list with new values
    x[0]=x0[0]
    x[1]=x1[0]
    x[2]=x2[0]
    
#print(x)

#first, I used a while loop for calculating the result, but the code wouldn't
#converge. So I used a for loop to see the values that it calculates. For x0,
#the result was:
#[1058.56082474]
#[-15.55074553]
#[-2117.01272959]
#[31.43187726]
#[4234.78913651]
#This shows that the results are oscillating by large amounts, and this means
#that GS can't ensure convergence.
p, L, U =linalg.lu(A) 
d=linalg.solve(L,b) 
x=linalg.solve(U,d)  
#this yields the result
#[[ 1.09052458e-01]
# [ 4.23276380e+00]
# [-2.54585666e+02]]
#Showing that solutions are possible using other methods, and the diagonal
#dominance wasn't an issue since I didn't use P (L instead of P@L)


