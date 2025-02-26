import numpy as np
import mdtraj as md
from sys import argv
import matplotlib.pyplot as plt
# trajectory file
input_data = md.load("ar_liquid_traj600.h5")

##############################
# parameters
nbins=100
rmin=0.1
#rmax=2.0594033385430914/2.
rmax=input_data.unitcell_lengths[0,0]/2.
dr=(rmax-rmin)/float(nbins)
#volume=(rmax*2.)**3
volume=input_data.unitcell_lengths[0,0]*input_data.unitcell_lengths[0,1]*input_data.unitcell_lengths[0,2]

#############################

N = int(input_data.n_atoms)
Nsteps=input_data.n_frames
print('There are ', N, ' Argon atoms in the trajectory')
pairs = []
for i in range(N):
    for j in range(i+1,N):
        pairs.append([i,j])
print('There are ', len(pairs), ' Ar-Ar pairs')

distances = md.compute_distances(input_data,pairs)

print('There are ', len(distances), ' steps in the trajectory')

histo=np.zeros(nbins,float)
#accumulate histograms

n_count=0
for ArAr in distances:
    print(ArAr)
    for d in ArAr:
        index = int(np.floor((d - rmin) / dr))
        if index < nbins:
            histo[index] += 1.           
            
            
#normalize histogram and divide by jacobian
for i in range(nbins):
	r=rmin+i*dr
	histo[i]=histo[i]/(2.*np.pi*r*r*dr*N*N/volume)/float(Nsteps)

Ar_file=open('Ar_histo','w')
NN=0.


for i in range(nbins):
	r=rmin+i*dr
	Ar_file.write(str(rmin+i*dr)+' '+str(histo[i])+'\n')
	if (r<0.5):
		NN+=histo[i]*r*r
print('N = ', N,'V =',volume,'Delta r =',r)
print('Number of neighbours = ',dr*4.*np.pi*(N/volume)*NN)
Ar_file.close()


directory = "C:/Users/gatyk/OneDrive/Desktop/Python Pile/NE 334/Assignment 2/"
filename = "Ar_histo"
r = []
hist = []

with open(directory + filename,'r') as file:
    for line in file:
        v = line.strip()
        split_list = v.split()
        r.append(float(split_list[0]))
        hist.append(float(split_list[1]))
file.close()

ro = np.array(r)
h = np.array(hist)
gr = ro*h


plt.plot(r,gr)
plt.xlabel("r")
plt.ylabel("g(r)")
plt.title("Probability of finding an Ar atom at distance r from another Ar atom for N=600")