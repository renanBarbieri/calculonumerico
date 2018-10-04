import sys

class NewtonRaphson(object):
    """
    Representa o método de NewtonRaphson
    """

    def execute(self, fx, dfdx, guess, precision, maxIterations):
        """
        Executa o método de NewtonRaphson usando a função passada
        """
        nextValue = fx(guess)
        currentPrecision = guess
        current = guess # Necessário para calcular a precisão -> | x_k+1 - x_k |
        iteration_counter = 0
        while currentPrecision > precision and iteration_counter < maxIterations:
            try:
                guess = guess - float(nextValue)/dfdx(guess)
            except ZeroDivisionError:
                print "Error! - derivative zero for x = ", guess
                sys.exit(1) # Aborta com um erro

            currentPrecision = abs(guess-current)
            nextValue = fx(guess)
            iteration_counter += 1

        return guess