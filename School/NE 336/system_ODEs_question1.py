
from scipy.integrate import solve_ivp
import time

# Gear's Chemistry Problem
def dxdt(_,j):
    [x1, x2, x3] = j
    dx1dt = -0.013*x1 - 1000*x1*x3
    dx2dt = -2500*x2*x3
    dx3dt = -0.013*x1 - 1000*x1*x3 - 2500*x2*x3
    
    return [dx1dt, dx2dt, dx3dt]

x_init = (1,1,0)
t_range = [0,50]

start=time.perf_counter()#start timer
# Solve using RK45 method (default)
sol1 = solve_ivp(dxdt, t_range, x_init, method = 'RK45')
end=time.perf_counter()
print(f"Time to run: {end-start}s")
#Return:
# Time to run: 11.524605099926703s    

start=time.perf_counter()#start timer
# Solve using RK25 method
sol2 = solve_ivp(dxdt, t_range, x_init, method = 'RK23')
end=time.perf_counter()
print(f"Time to run: {end-start}s")
#Return:
# Time to run: 7.369775000028312s
    
start=time.perf_counter()#start timer
# Solve using DOP853 method
sol3 = solve_ivp(dxdt, t_range, x_init, method = 'DOP853')
end=time.perf_counter()
print(f"Time to run: {end-start}s")
#Return:
# Time to run: 7.628612900036387s
#Note: there was an overflow error

start=time.perf_counter()#start timer
# Solve using Radau method
sol4 = solve_ivp(dxdt, t_range, x_init, method = 'Radau')
end=time.perf_counter()
print(f"Time to run: {end-start}s")
#Return:
# Time to run: 0.021153699955902994s

start=time.perf_counter()#start timer
# Solve using BDF method
sol5 = solve_ivp(dxdt, t_range, x_init, method = 'BDF')
end=time.perf_counter()
print(f"Time to run: {end-start}s")
#Return:
# Time to run: 0.0061836999375373125s

start=time.perf_counter()#start timer
# Solve using LSODA method
sol6 = solve_ivp(dxdt, t_range, x_init, method = 'LSODA')
end=time.perf_counter()
print(f"Time to run: {end-start}s")
#Return:
# Time to run: 0.008854800020344555s