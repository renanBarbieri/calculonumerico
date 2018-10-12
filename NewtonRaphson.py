# coding=utf-8
import sys

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
            # try:
            nextGuess = guess - fx(guess)/dfdx(guess)
            print "Next guess: ", nextGuess
            # except ZeroDivisionError:
            #     print "Error! - derivative zero for x = ", guess
            #     sys.exit(1) # Aborta com um erro

            currentPrecision = abs(guess-nextGuess) # Necessário para calcular a precisão -> | x_k+1 - x_k |
            guess = nextGuess
            iteration_counter += 1

        print "Num of iterations ", iteration_counter
        return guess