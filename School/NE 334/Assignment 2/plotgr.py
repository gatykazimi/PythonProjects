import matplotlib.pyplot as plt
import numpy as np
import mdtraj as md

input_data = md.load("h2o_liquid_traj.h5")

##############################
# parameters
nbins=100
rmin=0.1
rmax=input_data.unitcell_lengths[0,0]/2.
dr=(rmax-rmin)/float(nbins)
volume=input_data.unitcell_lengths[0,0]*input_data.unitcell_lengths[0,1]*input_data.unitcell_lengths[0,2]

#############################

N = int(input_data.n_atoms/3)
Nsteps=input_data.n_frames
directory = "C:/Users/gatyk/OneDrive/Desktop/Python Pile/NE 334/Assignment 2/"
filename = "OO_histo"
r = []
hist = []
NN=0.
with open(directory + filename,'r') as file:
    for line in file:
        v = line.strip()
        split_list = v.split()
        r.append(float(split_list[0]))
        hist.append(float(split_list[1]))
    ro = np.array(r)
    h = np.array(hist)
    r=0
    for i in range(nbins):
        r=rmin+i*dr
        if (r<0.5):
            NN+=h[i]*r*r
    print('N = ', N,'V =',volume,'Delta r =',r)
    print('Number of neighbours = ',dr*4.*np.pi*(N/volume)*NN)
file.close()


#gr = ro*h

plt.figure()
plt.plot(ro,h)
plt.xlabel("r")
plt.ylabel("g(r)")
plt.title("Probability of finding O atom at distance r from H atom")



