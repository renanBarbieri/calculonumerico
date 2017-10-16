function [y]=g(x)
  y=cos(x)
endfunction

n=10 //número de iterações
x=zeros(n,1)
x(1)= 0 // chute
for k=2:n
    x(k)=g(x(k-1))
    disp(x(k))
end

xplot=[0:0.01:1.2]';
plot(xplot,cos(xplot))
plot(xplot,xplot)

for k=2:n
xsegs([x(k-1), x(k)],[g(x(k-1)), g(x(k-1))])
xsegs([x(k), x(k)],[g(x(k-1)), g(x(k))])
end
