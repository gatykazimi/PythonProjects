
import numpy as np 
from scipy.optimize import newton #for comparison of results at the end

def myNR(func, x0, funcderiv = None):
    """
    Compute the Newton-Raphson method (or Secant method). 
    if funcderiv is supplied, will perform the Newton-Raphson method. 
    Otherwise, if funcderiv == None (default), then will perform Secant method.
    """
    #SECANT METHOD
    if funcderiv == None: #when the function derivative isn't given
        x = [x0] #create a list for the x values
        i=0 #initialize count variable
        err=1 #initialize error
        while err>10**-6: #execute loop when the error is less than tolerance
            #since the derivative isn't given, calculate our own derivative
            funcderiv = (func(x[i]+0.01)-func(x[i]))/(0.01)
            newx = x[i]-func(x[i])/funcderiv #NR formula
            x.append(newx) #add the new found value to the list
            err = abs(x[i+1]-x[i])/abs(x[i+1]) #calculate error
            i+=1 #add 1 to the count
        return x[i] 
    #NEWTON-RAPHSON METHOD
    else:
        x = [x0] #create a list for the x values
        i=0 #initialize count variable
        err=1 #initialize error
        while err>10**-6: #execute loop when the error is less than tolerance
            newx = x[i]-func(x[i])/funcderiv(x[i]) #NR formula
            x.append(newx)#add the new found value to the list
            err = abs(x[i+1]-x[i])/abs(x[i+1])#calculate error
            i+=1#add 1 to the count
        return x[i]

if __name__ == '__main__': 
    # test your function here
    f_test = lambda x: x**5 - 11*x**4 + 43*x**3 - 73*x**2 + 56*x - 16
    fderiv_test = lambda x: 5*x**4 - 44*x**3 +129*x**2 - 146*x + 56
    print(myNR(f_test,-2,fderiv_test))
    # return: 0.9999919927694815
    print(myNR(f_test,-2))
    # return: 1.0004846306305615
    print(newton(f_test,-2,fderiv_test)) #builtin function
    # return: 0.9999919927694815
    