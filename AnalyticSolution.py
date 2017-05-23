from math import *
from numpy import *
from matplotlib.pyplot import *

def GetMass(speed, beta, mu):
    mass = exp(-(1 - speed ** 2) * beta / (1 - mu))
    return mass

def IntegralExp(x):
    result = 0.577 + log(x)
    for n in range(1, 150):
        result += (x ** n) / (n * factorial(n))
    return result

def GetHeight(speed, alpha, beta):
    delta = IntegralExp(beta) - IntegralExp(beta * speed ** 2)
    height = log(2 * alpha) + beta - log(delta)
    return height

def GetHeightPoints():
    alpha = 7.24
    beta = 1.99
    speed = linspace(0.001, 1, 500)
    height = []
    for i in range(0, len(speed)):
        height.append(GetHeight(speed[i], alpha, beta))
    return [speed, height]

def Main():
    speed = linspace(0.000000000000001, 1, 200)
    beta = 1.70
    alpha = 8.25
    mu = 2 / 3
    height = []
    mass = []
    for i in range(0, len(speed)):
        height.append(GetHeight(speed[i], alpha, beta))
        mass.append(GetMass(speed[i], beta, mu))
    plot(speed, height)
    xlabel("Speed")
    ylabel("Height")
    show()
    plot(speed, mass)
    xlabel("Speed")
    ylabel("Mass")
    show()
    return
