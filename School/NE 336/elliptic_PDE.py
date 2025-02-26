import numpy as np 

T_left = 50 #Degrees Celsius
T_bottom = 20 #Degrees Celsius

# number of internal nodes
m = 3
n=3
k=n*m

#Create Temperature matrix
T = np.zeros((m+1,n+1))
#Set boundary conditions
T[:,0] = T_left
T[-1,:] = T_bottom
#Create Center Difference matrix
A = np.diag(-4*np.ones(k))+np.diag(np.ones(k-1),1)+np.diag(np.ones(k-1),-1)+np.diag(np.ones(k-3),3)+np.diag(np.ones(k-3),-3)
A[2,1]=2
A[2,3]=0
A[3,2]=0
A[5,4]=2
A[5,6]=0
A[6,5]=0
A[6,3]=2
A[7,4]=2
A[8,5]=2
A[8,7]=2

b = np.array([[-70],[-50],[-50],[-20],[0],[0],[-20],[0],[0]])

#Solve CD matrix
T_solve=np.linalg.solve(A,b)

#Insert answers in correct places on the Temperature matrix
T[-2,1:4] = [T_solve[0,0],T_solve[3,0],T_solve[6,0]]
T[-3,1:4] = [T_solve[1,0],T_solve[4,0],T_solve[7,0]]
T[-4,1:4] = [T_solve[2,0],T_solve[5,0],T_solve[8,0]]
print(T)
#Output:
#[[50.         41.92307692 36.73076923 35.        ]
# [50.         40.48076923 35.         33.26923077]
# [50.         35.         29.51923077 28.07692308]
# [20.         20.         20.         20.        ]]