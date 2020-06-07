clear all 
close all
clc

Y = 20e9;
lam = sqrt(2)/(5.56*10^(-10));

M = 1.660539*10^(-27)*40.078;


max = (pi*lam)/1e9

k = -max:0.01:max;

w = sqrt(Y/(M*lam)) * abs(sin(1e9*k/(2*lam))) / 10e12;

plot(k,w, 'black')
grid();
title('Dispersion Realtion for Calcium')
ylabel('\omega / ps^{-1}','fontweight','bold','fontsize',12)
xlabel('k / nm^{-1}','fontweight','bold','fontsize',12)

w(end)