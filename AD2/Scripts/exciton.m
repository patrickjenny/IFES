clear all
close all
clc

me = 0.21
mh = 0.8

hbar = 1.054571e-34

mu = (me*mh)/(me+mh)
m0 =  9.109383e-31
ee = 1.602172e-19

eps0 = 8.854187e-12

epsR = 8.9
eps = 8.9*eps0

E = (mu*m0*ee^4)/(2*hbar^2*eps^2)

E = mu/epsR^2 * 13.605

aH = 0.529177e-10

Radus = (epsR*aH/mu)
