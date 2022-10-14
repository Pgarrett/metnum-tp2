import config as cfg
import numpy as np

def readOutputFile(file):
    if cfg.debug:
        print("Reading output file ", file)

    outputEighenVectors = readEigenVectors(file + "_eigenVectors.csv")
    outputEighenValues = readEigenValues(file + "_eigenValues.csv")
    if cfg.debug:
        print("\nread matrix")
        print(outputEighenVectors)
        print("\nread outputEighenValues")
        print(outputEighenValues)
    return outputEighenValues, np.transpose(toNumpyMatrix(outputEighenVectors))

def toNumpyMatrix(matrix):
    np_arrays = []
    for arr in matrix:
        np_arrays.append(np.array(arr))
    return np_arrays

def readOutputMatrixFile(filename):
    with open(filename, "r") as file:
        m = [[float(num) for num in line.split(", ")] for line in file]
    return m

def readEigenValues(filename):
    with open(filename, "r") as file:
        l = [line for line in file]
        l.pop(0)
        l = [float(line[:-2]) for line in l]
    return l 

def readEigenVectors(filename):
    with open(filename, "r") as file:
        l = [line for line in file]
        vectorList = []
        for i in range(1, len(l)):
            vectorI = list(map(lambda x: float(x), l[i][:-3].split(", ")))
            vectorList.append(vectorI)
    return vectorList













