# Método de Newton

## Implementação
A implementação do método de newton em python ficou desta maneira:
```python
class NewtonRaphson(object):
    """
    Representa o método de NewtonRaphson
    """

    def execute(self, fx, dfdx, guess, precision, maxIterations):
        """
        Executa o método de NewtonRaphson usando a função passada
        """
        currentPrecision = precision+1
        iteration_counter = 0
        while currentPrecision >= precision and iteration_counter < maxIterations:
            try:
                nextGuess = guess - fx(guess)/dfdx(guess)
                print "Next guess: ", nextGuess
            except ZeroDivisionError:
                print "Error! - derivative zero for x = ", guess
                sys.exit(1) # Aborta com um erro

            currentPrecision = abs(guess-nextGuess) # Necessário para calcular a precisão -> | x_k+1 - x_k |
            guess = nextGuess
            iteration_counter += 1

        print "Num of iterations ", iteration_counter
        return guess
```
Desta forma, pode-se utilizar qualquer função usando esta mesma classe.
Para rodar a aplicação e o problema apresentado, foi criada a classe Application:

```python
class Application(object):

    cs = 9 # mg/l
    c0 = 2 # mg/l
    ka = 0.88 # /dia

    def __init__(self):
        print("Initializing NewtonRaphson application")
        t0 = int(raw_input("Enter the initial guess:"))
        newtonRaphson = NewtonRaphson()
        result = newtonRaphson.execute(self.f, self.dfdx, t0, 0.000001, 100)
        print "f(",result,") ~= 0"

    def f(self, x):
        # print "Getting x = ",x
        fx = self.cs - ((self.cs - self.c0) * exp(self.ka * x))
        # print "Getting fx = ",fx
        return fx

    def dfdx(self, x):
        dfdx = self.ka * (-(self.cs - self.c0)) * exp(self.ka * x)
        # print "Getting dfdx = ",dfdx
        return dfdx

Application()
```
Este será o arquivo que deverá ser executado. É nele que é definida a função f(x) e sua derivada [dfdx(x)].

## Análise