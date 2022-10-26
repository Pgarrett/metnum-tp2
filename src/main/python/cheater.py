import numpySolver as npt
import numpy as np

def superSimulateCppFor(matrix):
    l, V = np.linalg.eigh(matrix)
    return l

def simulateCppFor(inputFile):
    l, V = npt.solve("./examples/" + inputFile + ".txt")
    writeEigenValues(inputFile, l)
    writeEigenVectors(inputFile, V)

def writeEigenValues(filename, eigenValues):
    np.savetxt('./results/' + filename + '_eigenValues.csv', eigenValues, delimiter=', \n', header='eigenValues')

def writeEigenVectors(filename, eigenVectors):
    headerEV = ""
    for i in range(1, len(eigenVectors)+1):
        headerEV += ('v_' + str(i) + ", ")
    np.savetxt('./results/' + filename + '_eigenVectors.csv', eigenVectors, header=headerEV)

simulateCppFor("karateclub")