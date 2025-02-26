import numpy as np
import math
sample_size=10000
# x and y are random numbers
x=np.random.random(sample_size)
y=np.random.random(sample_size)
fin=open('xy.dat','w')
fout=open('xy_out.dat','w')
count_circle=0
count_miss = 0
for i in range(sample_size):
    r=x[i]**2+y[i]**2
    if r <= 1:
        fin.write(str(x[i])+' '+str(y[i])+' '+'\n')
        count_circle+=1
            
    else:
        fout.write(str(x[i])+' '+str(y[i])+' '+'\n')
        
fin.close()
fout.close()

approx_pi=(count_circle/float(sample_size))*4
print(approx_pi)
err = (approx_pi-math.pi)/np.sqrt(sample_size)
print(err)