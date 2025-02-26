import numpy as np
import statistics
import matplotlib.pyplot as plt
#imput parameters
x_mean=1.
standard_deviation=2.
sample_size=50000
# create varaibles for sum and average of the distribution
x_sum = 0
x_av = 0
x_diff = 0
# numpy function to sample the normal distribution
x_norm=np.random.normal(x_mean,standard_deviation,sample_size)

#
f=open('x_normal.dat','w')
for x in x_norm:
    f.write(str(x)+'\n')
    x_sum += x
f.close()
x_av = x_sum/sample_size
x_diff = (x_av-x_mean)**2
x_std = statistics.stdev(x_norm)
print(x_av)
print(x_diff)
print(x_std)
# histogram of x
nbins=1000
(h,x)=np.histogram(x_norm,nbins)
plt.hist(x_norm, nbins, alpha=0.5, color= "blue")
plt.xlabel("x")
plt.ylabel("Density")
plt.title("Histogram of x samples when nbins = "+ str(nbins))
plt.show()
fhisto=open('x_histo.dat','w')
for i in range(len(h)):
    fhisto.write(str(x[i])+' '+str(h[i])+' '+'\n')
fhisto.close()
