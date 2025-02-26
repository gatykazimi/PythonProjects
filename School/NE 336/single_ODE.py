#complete this file and submit for task 1
#name and student ID go here 
# Gaty Kazimi
# 20956021


#import solve_ivp here using a suitable statement
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

beta = -2
#-----------------------
#--define const at top--
#-----------------------
#this is the space to define values such as x(t=5)=10 etc that you will use in all of your code
x_init = [10]
(t0 ,tf) = (5, 15)

#---------------------
#-------Task 1.1------
#---------------------
 
#define your function (ode_fun_1) for the ODE dxdt=beta*x by entering the value for beta in the equation

#define ode_fun_1 here 
ode_fun_1 = lambda t, x: beta*x



#solve the ode and call the solution sol1
sol1 = solve_ivp(ode_fun_1,[t0,tf],x_init)
t_val = sol1.t
x_val = np.ravel(sol1.y)
#plot x vs t for all t values with a suitable label
plt.plot(t_val,x_val)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Solution 1 to dx/dt")

#---------------------
#-------Task 1.2------
#---------------------
#find the value of x at t=7 by using commands in code (not just reading from graph)
x_7 = solve_ivp(ode_fun_1,[t0,tf],x_init, t_eval = [7])

#write a print statement here to show the value of x at t=7 using the command you find
#print(float(np.ravel(x_7.y)))
# Returns: 0.18347146113945745

#---------------------
#-------Task 1.3------
#---------------------
#write your ode as a function that now takes three arguments with beta being the last one. 
#call this ode_fun_2
def ode_fun_2 (t,x,beta):
    return beta*x

#solve this ODE for beta= -2 by using the args optional argument in solve_ivp
sol2 = solve_ivp(ode_fun_2,[t0,tf],x_init, args=[-2])

#plot x vs t for all t values with a suitable label in a new figure
t_val2 = sol2.t
x_val2 = np.ravel(sol2.y)
#plot x vs t for all t values with a suitable label
plt.plot(t_val,x_val)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Solution 2 to dx/dt")


#---------------------
#-------Task 1.4------
#---------------------
#use the ode function you developed in the previous task to now solve for a range of beta values
#plot the results for all values of beta=[-2,-4,-6,-8] on the same figure. 
soli = [sol2]
t_val = [t_val2]
x_val= [x_val2]
sol3 = solve_ivp(ode_fun_2,[t0,tf],x_init, args=[-4])
t_val.append(sol3.t)
x_val.append(np.ravel(sol3.y))
sol4 = solve_ivp(ode_fun_2,[t0,tf],x_init, args=[-6])
t_val.append(sol4.t)
x_val.append(np.ravel(sol4.y))
sol5 = solve_ivp(ode_fun_2,[t0,tf],x_init, args=[-8])
t_val.append(sol5.t)
x_val.append(np.ravel(sol5.y))
for i in range(0,4):
    b =(i+1)*(-2)
    plt.plot(t_val[i],x_val[i], label = (str(b)))

plt.legend(title = "Beta")
#plt.legend.title("Beta")
plt.xlabel("t")
plt.ylabel("x")
plt.title("Solution 2 to dx/dt with various beta values")

#Bonus: include labels to show the value of beta for each solution being plotted