import numpy as np
import math

# prints formatted price
def formatPrice(n):
    return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))

# returns the vector containing stock data from a fixed file
def getStockDataVec(key):
    vec = []
    lines = open("data/" + key + ".txt", "r").read().splitlines()

    for line in lines[1:]:
        vec.append(float(line.split(",")[4]))

    return vec


# returns the vector containing stock data from a fixed file
def getStockVolVec(key):
    vol = []
    lines = open("data/" + key + ".txt", "r").read().splitlines()

    for line in lines[1:]:
        vol.append(float(line.split(",")[5]))

    return vol

# returns the sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

