#!/usr/bin/python3
# Crescimento Exponencial - População
# Seja P(t) a quantidade que aumenta com o tempo t e a taxa de crescimento é proporcional à mesma quantidade de P seguindo a seguinte fórmula:
# dP/dt = kP
# onde dp/dt é a primeira derivada de P, k > 0 e t é o tempo.
# A solução para a equação diferencial de primeiro grau acima é:
# P(t) = P0 e^(kt)
# onde P0 é a população inicial.

from __future__ import print_function
import math
import numpy as np
import plotly as plot
import plotly.graph_objs as graph

xPoints = np.linspace(0,10,1500) # de 0 a 10, com 1500 pontos
firstPoint = 100 # valor inicial da população
k = 0.4
dt = 0.2
yReal = [] 
yMethodOne = [] 
yMethodTwo = [] 

def population(time):
    """ p(t) = P0 e^(kt), onde P0 é a população inicial. -> float """
    return firstPoint*math.exp(k*time) 

def derivatePopulation(time):
    """ dP/dt = kP(t) """
    return k*population(time)

def firstMethod(time):
    """ dP/dt = ( P(t+dt)-P(t) )/dt . Assim, dP/dt * dt + P(t) = P(t+dt)"""
    # return population(time) + (derivatePopulation(time)*dt)
    return population(time - dt) + (derivatePopulation(time -dt)*dt)

def secondMethod(time):
    """ dP/dt = ( P(t+dt)-P(t-dt) )/2dt . Assim, dP/dt * 2dt + P(t-dt) = P(t+dt)"""
    # return (derivatePopulation(time) * 2 * dt) + population(time-dt)
    return (derivatePopulation(time -dt) * 2 * dt) + population(time-(2*dt))

def init():
    """ Função que inicializa o programa """
    for time in xPoints:
        yReal.append(population(time))
        yMethodOne.append(firstMethod(time))
        yMethodTwo.append(secondMethod(time))

    functions = [
        graph.Scatter(x = xPoints, y = yReal, name = "Analítica"),
        graph.Scatter(x = xPoints, y = yMethodOne, name = "Método 1"),
        graph.Scatter(x = xPoints, y = yMethodTwo, name = "Método 2")
    ]

    plot.offline.plot(functions, filename='crescimentoExponencial.html')

init()
