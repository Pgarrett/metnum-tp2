import matrixBuilder as mBuilder
import config as cfg
import plotter as plot
import executor as exec
import tpio
import numpy as np

from scipy import stats

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
    outputMatrixFile = 'ego-facebook-adj_' + u
    np.set_printoptions(suppress=True)
    np.savetxt('./examples/' + outputMatrixFile + '.txt', adj, fmt='%i')
    return outputMatrixFile

def flattenCompare(adjacencyMatrix, transformedFacebookEdgesFile):
    flatAdj = np.concatenate(adjacencyMatrix).ravel()
    flatFb = np.concatenate(transformedFacebookEdgesFile).ravel()
    return correlation(flatAdj, flatFb)

def eigenValueCompare(adjacencyMatrix, u, fbEdgesEigenValues):
    adjFile = writeAdjacencyToFile(adjacencyMatrix, u)
    exec.runTpFor(adjFile)
    adjEigenValues = tpio.readEigenValues(adjFile)
    return correlation(adjEigenValues, fbEdgesEigenValues)

# def chooseOptimumUValue():

def calculateFbEdgesEigenValues(fbEdges):
    exec.runTpFor(fbEdges)
    return tpio.readEigenValues(fbEdges)

def correlation(v1, v2):
    return stats.pearsonr(v1, v2).pvalue

def run():
    similarity = mBuilder.buildSimilarityMatrix()
    fbEdgesFile = mBuilder.transformFacebookEdgesToAdjacencyMatrix()
    fbEdges = tpio.toNumpyMatrix(tpio.readOutputMatrixFile(fbEdgesFile))
    fbEigenValues = calculateFbEdgesEigenValues(fbEdgesFile)
    flattenCorrelations = []
    eigenValueCorrelations = []

    for u in cfg.uValues:
        adj = adjacencyByU(similarity, u)
        flattenCorrelations.append(flattenCompare(adj, fbEdges))
        eigenValueCorrelations.append(eigenValueCompare(adj, u, fbEigenValues))

    plot.generateUCutsForFlatten(flattenCorrelations)
    plot.generateUCutsForFlatten(eigenValueCorrelations)
    plot.compareUCuts(flattenCorrelations, eigenValueCorrelations)


run()