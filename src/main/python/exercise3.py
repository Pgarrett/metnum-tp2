import matrixBuilder as mBuilder
import config as cfg
import plotter as plot
import executor as exec
import tpio
import numpy as np
from pathlib import Path
from scipy import stats
import cheater as ch
import pca

def adjacencyByU(similarity, u):
    n = len(similarity)
    result = []
    for i in range(0, n):
        rowResult = []
        for j in range(0, n):
            if similarity[i][j] <= u:
                rowResult.append(0)
            else:
                rowResult.append(1)
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
    # adjFile = writeAdjacencyToFile(adjacencyMatrix, u)
    # exec.runTpFor(adjFile)
    # ch.simulateCppFor(adjFile)
    adjEigenValues = ch.superSimulateCppFor(adjacencyMatrix)
    # adjEigenValues = tpio.readEigenValues("/results/" + adjFile + "_eigenValues.csv")
    return correlation(np.real(adjEigenValues), np.real(fbEdgesEigenValues))

# def chooseOptimumUValue():

def calculateFbEigenValues():
    inputPath = 'ego-facebook-adj'
    if not Path('/results/' + inputPath + '_eigenValues.csv').is_file():
        # exec.runTpFor(inputPath)
        ch.simulateCppFor(inputPath)
    return tpio.readEigenValues('/results/' + inputPath + '_eigenValues.csv')

def correlation(v1, v2):
    return np.corrcoef(v1, v2)[0,1]

def run3_1_2_3():
    print("Building similarity matrix")
    similarity = mBuilder.buildSimilarityMatrix()
    np.set_printoptions(suppress=True)
    np.savetxt('./examples/fb_similarity_v2.txt', similarity, fmt='%i')
    print("Building adjacency matrix from edges")
    fbAdj = mBuilder.transformFacebookEdgesToAdjacencyMatrix()
    print("Calculating adjacency matrix from edges eigenvalues")
    plot.similarityPlot(fbAdj, "Matrix de adyacencia Facebook Edges")
    fbEigenValues = ch.superSimulateCppFor(fbAdj)

    flattenCorrelations = []
    eigenValueCorrelations = []
    maxFlattenCorrelation = -1
    maxFlattenCorrelationVal = -1
    maxEVCorrelation = -1
    maxEVCorrelationVal = -1
    for u in cfg.uValues:
        print("Calculating adjacency matrix from similarity for u: " + str(u))
        adj = adjacencyByU(similarity, u)
        print("Flatten compare")
        flatCorrelation = flattenCompare(adj, fbAdj)
        if flatCorrelation > maxFlattenCorrelationVal:
            maxFlattenCorrelationVal = flatCorrelation
            maxFlattenCorrelation = u
        flattenCorrelations.append(flatCorrelation)
        print("Eigenvalue compare")
        evCorrelation = eigenValueCompare(adj, u, fbEigenValues)
        eigenValueCorrelations.append(evCorrelation)
        if evCorrelation > maxEVCorrelationVal:
            maxEVCorrelationVal = evCorrelation
            maxEVCorrelation = u
        if u == cfg.startUpUValue:
            plot.similarityPlot(adj, "Matrix de adyacencia valor u inicial")
            print("StartupCorrelation values. Eigen: " + str(evCorrelation) + ". Flatten: " + str(flatCorrelation))
        if u == cfg.optimumUValue:
            plot.similarityPlot(adj, "Matrix de adyacencia valor u óptimo")

    print("Max Flatten Correlation. U: " + str(maxFlattenCorrelation) + ". Value: " + str(maxFlattenCorrelationVal))
    print("Max EV Correlation. U: " + str(maxEVCorrelation) + ". Value: " + str(maxEVCorrelationVal))
    print("Flatten correlations: " + str(flattenCorrelations))
    print("Eigenvalues correlations: " + str(eigenValueCorrelations))
    plot.generateUCutsForFlatten(flattenCorrelations)
    plot.generateUCutsForEigenValues(eigenValueCorrelations)
    plot.compareUCuts(flattenCorrelations, eigenValueCorrelations)

def run3_4():
    pca.doPCA()

def run():
    #run3_1_2_3()
    run3_4()

run()