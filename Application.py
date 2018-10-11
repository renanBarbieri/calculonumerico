import numpy as np
from math import exp
from NewtonRaphson import NewtonRaphson

class Application(object):

    cs = 9 # mg/l
    c0 = 2 # mg/l
    ka = 0.88 # /dia

    def __init__(self):
        print("Iniciando a aplicação")
        x0 = 30
        newtonRaphson = NewtonRaphson()
        newtonRaphson.execute(self.f, self.dfdx, x0, 0.000001, 100)

    def f(self, x):
        print "Getting fx at "+x
        return self.cs - ((self.cs - self.c0) * exp(self.ka * x))

    def dfdx(self, x):
        print "Getting dfdx at "+x
        return exp(self.ka * x) * self.ka * (self.cs - self.c0)

Application()