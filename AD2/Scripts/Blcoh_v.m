clear all
close all


k = -pi/2:0.01:pi/2

E_0 = 1

E = -E_0*(cos(k) + 1)
v = sin(k)
m = k./v

plot(k,E,'k')
hold on
plot(k,v,'--','color','k')
plot(k,m,':','color','k')

xlabel('$k_x$','interpreter','latex')

legend('$E$','$v\hbar$','$m^*\slash\hbar$','interpreter','latex')