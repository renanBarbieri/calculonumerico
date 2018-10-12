# coding=utf-8
import numpy as np
from math import exp
from NewtonRaphson import NewtonRaphson

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
        print "Getting x = ",x
        fx = self.cs - ((self.cs - self.c0) * exp(self.ka * x))
        print "Getting fx = ",fx
        return fx

    def dfdx(self, x):
        dfdx = self.ka * (-(self.cs - self.c0)) * exp(self.ka * x)
        print "Getting dfdx = ",dfdx
        return dfdx

Application()