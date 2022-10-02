import config as cfg
import numpy as np

def readInputFile(input):
    print("Reading input file ", input)
    matrixText = open(input, "r")
    matrix = []
    matrix = [list(map(int, line.split())) for line in matrixText]
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

def solve(inputFile):
    print("Calculate eigh using numpy:")
    matrix = readInputFile(inputFile)
    return numpyCalculateEigh(matrix)
