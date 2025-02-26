import numpy as np
import statistics
sample_size=100000

x_uniform=np.random.random(sample_size)
f=open('x_uniform.dat','w')
for x in x_uniform:
	#print(x)
	f.write(str(x)+'\n')
    
f.close()
x_mean = statistics.mean(x_uniform)
print(x_mean)

x_uniform=np.random.uniform(-1,3,sample_size)
x_mean = statistics.mean(x_uniform)
print(x_mean)