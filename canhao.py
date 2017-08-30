#!/usr/bin/python3 
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import time

start = time.time()
g = 9.81
massa = 1.0
resistence = 0.1
n = 1000 # de intervalos
tempo = 1/(n+1) #Passo do algoritmo
x_passos = [] #Array de passos, eixo x do grafico
x_plot = [] #Array de resolucao eixo x
y_plot = [] #Array de resolucao do sistema linear, eixo y do grafoc
x_inicial = 0
x_final = 100
y_inicial = 0.0
y_final = 1.0
#Matriz x
A_x = np.zeros((n,n)) #Montando valores iniciais das matrizes
b_x = np.zeros(n)
#Matriz y
A_y = np.zeros((n,n)) #Montando valores iniciais das matrizes
b_y = np.zeros(n)
#Monta b de x
b_x[0] = -x_inicial
b_x[n-1] = -x_final


for i in range(0, n): #Monta diagonal principal de A
    A_x[i,i] = -2
    A_y[i,i] = -2

for i in range(0, n-1): #Monta adjacentes da diagonal de A
    A_x[i, i+1] = 1+(resistence*tempo)/(massa*2)
    A_x[i+1, i] = 1-(resistence*tempo)/(massa*2)
    b_x[i] = 0

    A_y[i, i+1] = 1
    A_y[i+1, i] = 1
    b_y[i] = -g*tempo*tempo

#Monta b de y
b_y[0] = b_y[0]-y_inicial #Monta b
b_y[n-1] = b_y[n-1]-y_final

#x_plot.append(0) #valor inicial de x, 0

x_plot = np.linalg.solve(A_x, b_x)
y_plot = np.linalg.solve(A_y, b_y)

end = time.time()

x_plot = np.append(x_plot, x_final)
x_plot = np.insert(x_plot, 0, x_inicial)

y_plot = np.append(y_plot, y_final)
y_plot = np.insert(y_plot, 0, y_inicial)


def velocidadeInicial():
    #x e x+h
    #y e y+h
    v_x = getXAtTime(1)/tempo
    v_y = getYAtTime(1)/tempo
    return [v_x, v_y]

def getYAtTime(t):
    return y_plot[t]

def getXAtTime(t):
    return x_plot[t]

def init():
    vZero = velocidadeInicial()
    print(vZero)
    print("Modulo de V0 = "+str(np.linalg.norm(vZero)))
    plot()

def plot():
    plt.title('Discretização com contorno para -y\'\' = -y\'+y')
    plt.xlabel('Posição x em metros')
    plt.ylabel('Posição y em metros')
    #plt.xlim([-100,100])  #limites dos eixos
    #plt.ylim([-100,100])

    plt.plot(x_plot, y_plot, 'o')
    plt.show()
    style.use('ggplot') #Estilo melhorzinho utilizado - comentar essa linha caso haja problemas na visualizacao

init()