# -*- coding: utf-8 -*-
"""
@author: Gaty Kazimi 20956021

Summation Function
This function takes in an x value, and optional error value, and checks if
the x satisfies the |x|<1 condition. Then, it calculates the sum of x^(2n-1).
"""

def summation (x, err = 10**(-5)):
    # check if x satisfies the condition
    if isinstance(x, float): #check if x is a decimal
        x = float(x) 
        if abs(x) <1: #check if |x| is less than 1
            f= lambda n: x**(2*n+1) #create a function for finding one term in the sum
            n=0 #create a counter
            #define variables that will be used in the loop
            newSum = 0 # sum at n
            preSum = 0 # sum at n-1
            diffSum = 1 #the difference between the n sum and n-1 sum
                        #will be used to calculate the relative error
            while diffSum > err: #compare the errors
                preSum = newSum #define previous sum
                newSum += f(n) #calculate new sum
                diffSum = newSum-preSum #find the difference
                n+=1 #add to the count
            return newSum #give answer to the user
        else:
            #print error statement if it doesn'/t satisfy the condition
            print(f"Error: {x} does not satisfy the condition |x|<1")
            return None
    else:
        #print error statement if it doesn'/t satisfy the condition
        print(f"Error: {x} does not satisfy the condition |x|<1")
        return None
        


print(summation(1))
# returns: Error: 1 does not satisfy the condition |x|<1
#          None
print(summation(1.1))
# returns: Error: 1 does not satisfy the condition |x|<1
#          None
print(summation(0.1))
# returns: 0.10101
print(summation(0.5))
# returns: 0.6666641235351562
print(summation(0.7642379007))
# returns: 1.8373600659976754
