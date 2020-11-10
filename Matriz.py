from math import *
from math import pi
import sympy as sp 
import matplotlib as mat
from random import randint, uniform, random
import numpy as np
from scipy import linalg


def suma():
    matrizR = np.zeros(matrizA.shape, dtype = float)

    if(matrizA.shape == matrizB.shape):
        for i in range(matrizA.shape[0]):
            for j in range(matrizA.shape[1]):
                matrizR[i][j] = matrizA[i][j] + matrizB [i][j]
    return matrizR

def resta():
    matrizR = np.zeros(matrizA.shape, dtype = float)

    if(matrizA.shape == matrizB.shape):
        for i in range(matrizA.shape[0]):
            for j in range(matrizA.shape[1]):
                matrizR[i][j] = matrizA[i][j] - matrizB [i][j]
    return matrizR

def multiplicacion():
    matrizR = np.zeros((matrizA.shape[0],matrizB.shape[1]), dtype = float)

    if(matrizA.shape[1] == matrizB.shape[0]):
        for i in range(matrizA.shape[0]):
            for j in range(matrizB.shape[1]):
                for k in range(matrizB.shape[0]):
                    matrizR[i][j] += matrizA[i][k] * matrizB [k][j]
    return matrizR

def division():
    matrizR = np.zeros((matrizA.shape[0],matrizB.shape[1]), dtype = float)

    if(matrizA.shape[1] == matrizB.shape[0]):
        matrizC = inversa(matrizB)
        for i in range(matrizA.shape[0]):
            for j in range(matrizC.shape[1]):
                for k in range(matrizC.shape[0]):
                    matrizR[i][j] += matrizA[i][k] * matrizC [k][j]
    return matrizR

def det(Matriz):
    return round(np.linalg.det(Matriz))

def inversa(Matriz):
    return linalg.inv(Matriz)

def transpuesta(Matriz):
    MatrizR=np.zeros((Matriz.shape[0],Matriz.shape[1]), dtype = float)
    for i in range(Matriz.shape[0]):
        for j in range(Matriz.shape[1]):
            MatrizR[j][i]=Matriz[i][j]
    return MatrizR

def ecuaciones(Matriz, Resultados):
    R = np.array(Resultados, dtype = float)
    return np.linalg.solve(Matriz,R)

def menu(A,B,operacion):
    global matrizA, matrizB
    matrizA = np.array(A, dtype = float)
    matrizB = np.array(B, dtype = float)

    if(operacion == 1): #SUMA = 1
        return suma()
    elif(operacion == 2): #RESTA = 2
        return resta()
    elif(operacion == 3): #MULTIPLICACION = 3
        return multiplicacion()
    elif(operacion == 4): #DIVISION = 4
        return division()
    elif(operacion == 5): #DETERMINANTE = 5
        return det(matrizA)
    elif(operacion == 6): #INVERSA = 6
        return inversa(matrizA)
    elif(operacion == 7): #TRANSPUESTA = 7
        return transpuesta(matrizA)
    elif(operacion == 8): #SISTEMAS DE ECUACIONES = 8
        return ecuaciones(matrizA,matrizB)

print(menu(([5,3,4],[7,8,9],[2.5,7.2,3.9]),([2,-1,3]),8))
    