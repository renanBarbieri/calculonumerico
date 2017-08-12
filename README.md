# Primeiro Trabalho
## Objetivo do projeto
Escolher uma Equação Diferencial Ordinária para aplicar os métodos de cálculo de uma EDO aprendidos em sala de aula e exibir os resultados comparando com o valor real da função.

## Descrição do Projeto
### Escolha da EDO
A equação escolhida foi a de crescimento exponencial de uma população. Esta equação pode ser descrita da seguinte forma:   
Seja P(t) a quantidade que aumenta com o tempo t e a taxa de crescimento é proporcional à mesma quantidade de P seguindo a seguinte fórmula:   
dP/dt=kP , onde dPdt é a primeira derivada de P, k > 0 e t é o tempo.   
A solução para a equação diferencial de primeiro grau acima é:   
P(t) = P0*e^(kt) , onde P0 é a população inicial.   

### Implementação
A partir da escolha da EDO, podemos modelar a sua equação de acordo com os métodos dados em aula.

#### Primeiro Método
Pelo primeiro método, temos: dP/dt = P(t+dt) - P(t)*dt   
Sendo assim, podemos chegar à conclusão que:   
(dP/dt)*dt + P(t) = P(t+dt)   
Sendo dt uma constante que determina o intervalo de análise ao redor do ponto.

#### Segundo Método
Pelo segundo método, temos: dp/dt = P(t+dt) - P(t-dt)2*dt   
Sendo assim, podemos chegar à conclusão que:   
(dp/dt)*2dt +P(t-dt) = P(t+dt)   
Sendo dt uma constante que determina o intervalo de análise ao redor do ponto.
