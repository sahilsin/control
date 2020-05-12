clear;
close;
clc;

loadmatfile("lm741.ngspice.tr","-ascii");
time = lm741(:,1);
Vi = lm741(:,2);
Vo = lm741(:,3);

plot(time,Vi,'g')
plot(time,Vo,'ro')
mtlb_grid