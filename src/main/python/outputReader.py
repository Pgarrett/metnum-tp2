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

def addLinks(input, dotFile):
    wd = str(os.getcwd())
    # get links
    links = []
    with open(wd  + "/examples/" + input + ".txt", "r") as f:
        graph_links = f.readlines()
        for line in graph_links:
            curr = []
            for v in line:
                if v == '0' or v == '1':
                    curr.append(v)
            links.append(curr)
    
    with open(wd + "/graphs/" + dotFile + ".dot", "r") as f:
        lines = f.readlines
        for line in lines:
            print(line)
            
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

