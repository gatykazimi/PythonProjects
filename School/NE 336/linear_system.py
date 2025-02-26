
import numpy as np
from scipy import linalg
import time


def solve_system(A,b,method=None):
    '''
	(ndarray,ndarry,str)->(ndarray,float)

    This function will return the solution of [A][x] = [b], if one exists as 
    well as the time taken to find it otherwise None.
    
    A is a square matrix which is nXn
    b is a column vector so it is nX1
    
    method is optional and can be :
    	inv : for the inverse method
    	lu : for the lu decomposition 	
	
    '''
    start=time.perf_counter()#start timer
    #tests first 
    a_size = A.shape #get size of matrix A
    b_size = b.size #get size of b vector
    if  A.ndim==2 and a_size[0]==a_size[1]: #check if matrix A is a square matrix
        if b_size==a_size[0]: #check if size of b vector is the same as matrix A
            #make c=[A b]
            c=np.concatenate((A,b),axis=1)
            #check if there is a solution
            rank_A=np.linalg.matrix_rank(A)
            rank_Ab= np.linalg.matrix_rank(c)
            if rank_A == b_size and rank_Ab ==rank_A: #check is matrices are solvable
                if method == "inv": #inverse method
                    a=np.linalg.inv(A) #get inverse of matrix A
                    x = a@b #matrix multiplication
                    end=time.perf_counter() #calculate time it takes to find x
                    print(f"Time to run: {end-start}s")
                    return x #return x and c
                elif method == "lu": #PLU decomposition method
                    p, L, U =linalg.lu(A) #get p, L, and U
                    d=linalg.solve(p@L,b) #find d vector
                    x=linalg.solve(U,d)  #solve for x
                    end=time.perf_counter() #calculate time it takes to find x
                    print(f"Time to run: {end-start}s")
                    return x #return x and c     
                else: #if no method is given, then use builtin method
                    x=np.linalg.solve(A,b) #builtin method
                    end=time.perf_counter() #calculate time it takes to find x
                    print(f"Time to run: {end-start}s")
                    return x #return x and c
            else:
                return None
        else: #if the inputs fail the checks, return None
            return None
    else:
        return None
    
if __name__=="__main__":
    #please complete warmup tasks here 
    
    #define A and b to solve Ax=b
    
    
    #warmup task 1
    A=np.array([[-3, 2, -1], [6, -6, 7], [3, -4, 4]])
    b = np.array([[-1],[-7],[-6]])
    #np.linalg.solve(A,b)
    #linalg.solve(A,b)
    # both methods gave the same answer (a vector of [[2],[2],[-1]])
    # the difference is that they employ different python libraries. Also
    # in the documentation, each method use different methods to solve.
    
    #warmup task 2
    #a=np.linalg.inv(A)
    #a@b
    # Again, gave the same answer as before
    # a downside is that using the inverse of A may take longer to calculate,
    # and it can be more difficult to inverse larger matricies.
    
    #warmup task 3
    #p, L, U =linalg.lu(A)
    #d=linalg.solve(p@L,b) 
    #x=linalg.solve(U,d) 
    #print(x)
    # This method is superior to others because it takes up less memory.
    
    #warmup task 4
    # the condition number refers to how ill conditioned the system is, which
    # basically means how much the output will change when you slightly change 
    # the original matrix.
    
    #i think my code for the function is working -> test for A and b you defined before
    # all of the following lines of code return the same answer as before, but their times are different
    print(solve_system(A,b))
    # return: Time to run: 0.00047920001088641584s
    print(solve_system(A,b, "inv"))
    # return: Time to run: 0.00033900002017617226s
    print(solve_system(A,b, "lu"))
    # return: Time to run: 0.000916799996048212s
    
    # with the fastest code being the builtin method
    
    #other two tests and comments on results here
    
    #Test 1
    #A=np.array([[3, 18, 9], [2, 3, 3], [4, 1, 2]])
    #b = np.array([[18],[117],[283]])
    #All of the following lines of code produce the vector [[ 72.],[-13.],[  4.]]
    #print(solve_system(A,b))
    # return: Time to run: 0.0003274999908171594s
    #print(solve_system(A,b, "inv"))
    # return: Time to run: 0.0003992999845650047s
    #print(solve_system(A,b, "lu"))
	# return: Time to run: 0.006947499990928918s
    
    #Test 2
    #A=np.array([[20, 15, 10], [-3, -2.24999,7], [5, 1, 3]])
    #b = np.array([[45],[1.751],[9]])
    #All of the following lines of code produce the vector [[0.99992588],[1.00002118],[1.00011647]]
    #print(solve_system(A,b))
    # return: Time to run: 0.0004191999905742705s
    #print(solve_system(A,b, "inv"))
    # return: Time to run: 0.00042100000428035855s
    #print(solve_system(A,b, "lu"))
	# return: Time to run: 0.0015814999933354557s
    
    #Error testing
    #Check square matrix
    #A=np.array([[3, 18, 9], [2, 3, 3]])
    #b = np.array([[18],[117],[283]])
    #print(solve_system(A,b))
    # return: None
    
    #Check duplicate equation in matrix
    #A=np.array([[3, 18, 9], [2, 3, 3],[2, 3, 3]])
    #b = np.array([[18],[117],[177]])
    #print(solve_system(A,b))
    # return: None
    
    #Check size
    #A=np.array([[3, 18, 9], [2, 3, 3],[2, 3, 3]])
    #b = np.array([[18],[117],[177], [165]])
    #print(solve_system(A,b))
    # return: None
    