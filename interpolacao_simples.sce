x_pontos=[1;2;9;6]
y_pontos=[3;67;7;19]
n=length(x_pontos)

//
//      | 1⁰  1¹  1²  1³ |
//  V = | 2⁰  2¹  2²  2³ |
//      | 9⁰  9¹  9²  9³ |
//      | 6⁰  6¹  6²  6³ |
//
for i=1:n
    for j=1:n
        V(i,j)=x_pontos(i).^(j-1)
    end
end

//
//  | 1⁰  1¹  1²  1³ | |a(0)|   |y(0)|
//  | 2⁰  2¹  2²  2³ | |a(1)| = |y(1)|
//  | 9⁰  9¹  9²  9³ | |a(0)|   |y(2)|
//  | 6⁰  6¹  6²  6³ | |a(1)|   |y(3)|
//
a=V\y_pontos      
x=(linspace(0,10))' //vetor linearmente espaçado com 100 valores [de zero a 10]
for i=1:length(x)
    y(i)=a(1)+a(2)*x(i)+a(3)*x(i)^2+a(4)*x(i)^3 
end
plot(x,y)
plot(x_pontos,y_pontos,'o')


//Trabalho em aula
//
//  | 1  x(0)  x(0)²   0   0      0   | |a(0)|   |y(0)|
//  | 1  x(1)  x(1)²   0   0      0   | |a(1)| = |y(1)|
//  | 0   0     0      1  x(1)  x(1)² | |1(2)|   |y(1)|
//  | 0   0     0      1  x(2)  x(2)² | |b(0)|   |y(2)|
//  | 0   1    2x(1)   0   -1  -2x(1) | |b(1)|   | 0  |
//  | 0   0     0      0   1    2x(2) | |b(2)|   | 0  | 
//
//Sistema linear:
// 1- a(0) + a(1) x(0) + a(2) x(0)² = y(0)
// 2- a(0) + a(1) x(1) + a(2) x(1)² = y(1)
// 3- b(0) + b(1) x(1) + b(2) x(1)² = y(1)
// 4- b(0) + b(1) x(2) + b(2) x(2)² = y(2)
//TODO: RESOLVER O SISTEMA LINEAR ACIMA E SUBSTITUIR NAS FUNÇÕES P'(X) E Q'(x)
// 5- P(x) = a(1) + 2 a(2) x 
//    Q(x) = b(1) + 2 b(2) x
//    a(1) + 2 a(2) x(1) - (b(1)+2 b(2) x(1)) = 0 //suavizar a curva
// P(x) é de x0 a x1 e Q(x) é de x1 a x2
