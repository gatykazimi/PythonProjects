import numpy as np
import matplotlib.pyplot as plt

Do = [4.47813, 1.54238, 3.05414] #H2, I2, HI

M = [2*1.01E-3, 2*0.126904, 0.126904 + 1.01E-3]
    
kB = 0.695038 # cm-1 K-1
kBev = 8.6173303e-5 
R = 8.314

thetaRot= [60.853/kB, 0.0373/kB, 6.4264/kB]
thetaVib= [4401.21/kB, 214.50/kB, 2301.91/kB]


zVib_H2 = lambda T: 1/(1-np.exp(-thetaVib[0]/T))
zVib_I2 = lambda T: 1/(1-np.exp(-thetaVib[1]/T))
zVib_HI = lambda T: 1/(1-np.exp(-thetaVib[2]/T))


sig = 2
zoNo_H2 = lambda T:820.519*(M[0])**(3/2)*T**(5/2)*(T/(sig*thetaRot[0]))*(zVib_H2(T))
zoNo_I2 = lambda T:820.519*(M[1])**(3/2)*T**(5/2)*(T/(sig*thetaRot[1]))*(zVib_I2(T))

zoNo_HI = lambda T:820.519*(M[2])**(3/2)*T**(5/2)*(T/(thetaRot[2]))*(zVib_HI(T))

deltU = 2*Do[2] - (Do[0] + Do[1])

def Kp (T):
    Kp = ((zoNo_H2(T)*zoNo_I2(T))/(zoNo_HI(T))**2*np.exp(-deltU/(kBev*T)))
    return Kp

T = np.linspace(300,3000)

plt.figure()
plt.xlabel("T in K")
plt.ylabel("Kp(T)")
plt.plot(T,Kp(T))
plt.title("Equilibrium constant of the reaction 2HI -> $H^2 + I^2$")

plt.figure()
plt.xlabel("T in 1/K")
plt.ylabel("Kp(T)")
plt.plot(1/T,np.log10(Kp(T)))
plt.title("Equilibrium constant of the reaction 2HI -> $H^2 + I^2$")