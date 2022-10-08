import config as cfg
import numpy as np
import os

def readOutputFile(file):
    if cfg.debug:
        print("Reading output file ", file)
    resultsPath = str(os.getcwd()) + '/results/'
    eigenVectors = open(resultsPath + file + "_eigenVectors.csv", "r")
    eigenValues = open(resultsPath + file + "_eigenValues.csv", "r")
    return eigenValues, eigenVectors

def toNumpyMatrix(matrix):
    np_arrays = []
    for arr in matrix:
        np_arrays.append(np.array(arr))
    return np_arrays

def readOutputMatrixFile(filename):
    with open(filename, "r") as file:
        m = [[float(num) for num in line.split(", ")] for line in file]
    return m

def readLabels():
    labelsPath = str(os.getcwd()) + '/examples/karateclub_labels.txt'
    labels = []
    with open(labelsPath, "r") as f:
        input = f.read()
        for line in input:
            if line == '1' or line == '0':
                labels.append(float(line))
    return labels
