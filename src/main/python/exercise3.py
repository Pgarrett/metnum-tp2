import matrixBuilder as mBuilder
import config as cfg
import plotter as plot
import executor as exec
import tpio
import numpy as np
from pathlib import Path
from scipy import stats
import cheater as ch

def adjacencyByU(similarity, u):
    result = []
    for row in similarity:
        rowResult = []
        for item in row:
            if item > u:
                rowResult.append(1)
            else:
                rowResult.append(0)
        result.append(rowResult)
    return result

def writeAdjacencyToFile(adj, u):
    outputMatrixFile = 'ego-facebook-adj_' + str(u)
    np.set_printoptions(suppress=True)
    np.savetxt('./examples/' + outputMatrixFile + '.txt', adj, fmt='%i')
    return outputMatrixFile

def flattenCompare(adjacencyMatrix, transformedFacebookEdgesFile):
    flatAdj = np.concatenate(adjacencyMatrix).ravel()
    flatFb = np.concatenate(transformedFacebookEdgesFile).ravel()
    return correlation(flatAdj, flatFb)

def eigenValueCompare(adjacencyMatrix, u, fbEdgesEigenValues):
    adjFile = writeAdjacencyToFile(adjacencyMatrix, u)
    # exec.runTpFor(adjFile)
    ch.simulateCppFor(adjFile)
    adjEigenValues = tpio.readEigenValues("/results/" + adjFile + "_eigenValues.csv")
    return correlation(adjEigenValues, fbEdgesEigenValues)

# def chooseOptimumUValue():

def calculateFbEigenValues():
    inputPath = 'ego-facebook-adj'
    if not Path('/results/' + inputPath + '_eigenValues.csv').is_file():
        # exec.runTpFor(inputPath)
        ch.simulateCppFor(inputPath)
    return tpio.readEigenValues('/results/' + inputPath + '_eigenValues.csv')

def correlation(v1, v2):
    return np.corrcoef(v1, v2)[0,1]

def run():
    print("Building similarity matrix")
    similarity = mBuilder.buildSimilarityMatrix()
    print("Building adjacency matrix from edges")
    fbAdj = mBuilder.transformFacebookEdgesToAdjacencyMatrix()
    print("Calculating adjacency matrix from edges eigenvalues")
    fbEigenValues = calculateFbEigenValues()

    flattenCorrelations = []
    eigenValueCorrelations = []
    for u in cfg.uValues:
        print("Calculating adjacency matrix from similarity for u: " + str(u))
        adj = adjacencyByU(similarity, u)
        print("Flatten compare")
        flattenCorrelations.append(flattenCompare(adj, fbAdj))
        print("Eigenvalue compare")
        eigenValueCorrelations.append(eigenValueCompare(adj, u, fbEigenValues))

    plot.generateUCutsForFlatten(flattenCorrelations)
    plot.generateUCutsForEigenValues(eigenValueCorrelations)
    plot.compareUCuts(flattenCorrelations, eigenValueCorrelations)


run()