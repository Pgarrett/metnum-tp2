import config as cfg
import numpy as np

def readInputFile(input):
    if cfg.debug:
        print("Reading input file ", input)
    
    matrixText = open(input, "r")
    matrix = []
    matrix = [list(map(int, line.split())) for line in matrixText]
    if cfg.debug:
        print(matrix)
    return matrix

def numpyCalculateEigh(matrix):
    np_arrays = []
    for arr in matrix:
        np_arrays.append(np.array(arr))
    l, V = np.linalg.eigh(np_arrays)
    if cfg.debug:
        print("\nEighenvalues:")
        print(l)
        print("\nEighenvectors:")
        print(V)
    return l, V

def numpySimilarityMatrix(matrix):
    similarityMatrix = [[] for i in range(len(matrix))]
    for i in range(0, len(matrix)):
        rowI = matrix[i]
        for j in range(0, len(matrix)):
            rowJ = matrix[j]
            similarityMatrix[i].append(float(np.dot(rowI, rowJ)))
    return similarityMatrix

def solve(inputFile):
    if cfg.debug:
        print("Calculate eigh using numpy:")

    matrix = readInputFile(inputFile)
    return numpyCalculateEigh(matrix)   

def solveSimilarityMatrix(inputFile):
    if cfg.debug:
        print("Calculating similarity matrix with numpy:")

    matrix = readInputFile(inputFile)
    return numpySimilarityMatrix(matrix)

def solveDeflationMethod(inputFile):
    if cfg.debug:
        print("Calculating deflation method witn numpy:")

    matrix = readInputFile(inputFile)
    return np.linalg.eig(matrix)





