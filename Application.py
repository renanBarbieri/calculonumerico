import numpy as np
from math import exp
from NewtonRaphson import NewtonRaphson

class Application(object):

    def __init__(self):
        print("Iniciando a aplicação")
        x0 = 30
        newtonRaphson = NewtonRaphson()
        newtonRaphson.execute(self.f, self.dfdx, x0, 0.000001, 100)

    def f(self, x):
        print "Getting fx at "+x
        cs = 0
        c0 = 0
        ka = 0
        return cs - ((cs - c0) * exp(ka * x))

    def dfdx(self, x):
        print "Getting dfdx"

Application()