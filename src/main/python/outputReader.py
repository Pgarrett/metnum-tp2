import config as cfg
import numpy as np
from numpy import genfromtxt

def readOutputFile(file):
    print("Reading output file ", file)
    outputEighenVectors = open(file + "_eighenvec", "r")
    outputEighenValues = genfromtxt(file + "_eighenval", delimiter=',')
    matrix = []
    matrix = [list(map(float, line.split())) for line in outputEighenVectors]
    if cfg.debug:
        print("\nread matrix")
        print(matrix)
        print("\nread outputEighenValues")
        print(outputEighenValues)
    return outputEighenValues, np.transpose(toNumpyMatrix(matrix))

def toNumpyMatrix(matrix):
    np_arrays = []
    for arr in matrix:
        np_arrays.append(np.array(arr))
    return np_arrays