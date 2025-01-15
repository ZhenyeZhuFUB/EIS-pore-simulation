# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:15:20 2024

@author: zhez95
"""

import matplotlib.pyplot as plt

from numpy import pi, conj, logspace
#parameters
l = 27*10**(-6)
kappa = 1
r = 9.96*10**(-6)
C_dl = 2.5*10**(-3)/2/pi/r/l/200


omega = logspace(6,0,30)
r_i = [5.15,5.35,5.55,5.825,6.175,6.525,6.875,7.225,7.6,8.075,8.625,9.15,9.525,
       9.775,10.05,10.375,10.725,11.1,11.6,12.2,12.825,13.325,13.675,14.05,14.55,
       15.15,15.775]
g_i = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0
while i <=26:
    g_i[i]=r_i[i]*10**(-6)/r
    i = i+1
#Value of Z_27*
Z = 1/27/(g_i[0]**2) + 1/(1j*omega*20*10**(-6)/(l/kappa/pi/r**2))
n = 1
#recursion to get Z_1*
for n in range (1,27):
    Z = 1/27/(g_i[n]**2) + 1/((1j/54*4*omega*C_dl*l**2/kappa/r*g_i[n-1])+1/Z)
    n = n+1
#Z_0*
Z = 1/((1j/54*4*omega*C_dl*l**2/kappa/r*g_i[26])+1/Z)
Z_real = (Z+conj(Z))/2
Z_imaginary = -(Z-conj(Z))/2/(1j)
plt.plot(Z_real,Z_imaginary)