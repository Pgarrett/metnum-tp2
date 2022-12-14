import matrixBuilder as mBuilder
import config as cfg
import plotter as plot
import executor as exec
import tpio
import numpy as np
from pathlib import Path
from scipy import stats
import os
import sanitizer


def adjacencyByU(similarity, u):
    n = len(similarity)
    result = []
    for i in range(0, n):
        rowResult = []
        for j in range(0, n):
            if similarity[i,j] < u or abs(similarity[i,j] - u) < cfg.compareToleranceEpsilon or i == j:
                rowResult.append(0)
            else:
                rowResult.append(1)
        result.append(rowResult)
    return result

def writeMatrixToFile(adj, outputFilename):
    np.set_printoptions(suppress=True)
    np.savetxt('./examples/' + outputFilename + '.txt', adj, fmt='%i')
    return outputFilename

def flattenCompare(adjacencyMatrix, transformedFacebookEdgesFile):
    flatAdj = np.concatenate(adjacencyMatrix).ravel()
    flatFb = np.concatenate(transformedFacebookEdgesFile).ravel()
    return correlation(flatAdj, flatFb)

def eigenValueCompare(adjacencyMatrix, fbEdgesEigenValues, outputAdjFilename):
    adjFile = writeMatrixToFile(adjacencyMatrix, outputAdjFilename)
    exec.runTpFor(adjFile)
    adjEigenValues = tpio.readEigenValues("/results/" + adjFile + "_eigenValues.csv")
    return correlation(np.real(adjEigenValues), np.real(fbEdgesEigenValues))

def calculateFbEigenValues():
    inputPath = 'ego-facebook-adj'
    if not Path('/results/' + inputPath + '_eigenValues.csv').is_file():
        exec.runTpFor(inputPath)
    return tpio.readEigenValues('/results/' + inputPath + '_eigenValues.csv')

def correlation(v1, v2):
    return np.corrcoef(v1, v2)[0,1]

def originalFbEigen():
    print("Building adjacency matrix from edges")
    fbAdj = mBuilder.transformFacebookEdgesToAdjacencyMatrix()
    print("Calculating adjacency matrix from edges eigenvalues")
    plot.similarityPlot(fbAdj, "Matrix de adyacencia Facebook Edges")

    exec.runTpFor("ego-facebook-adj")
    eigenList = tpio.readEigenValues('/results/ego-facebook-adj_eigenValues.csv')
    return fbAdj, eigenList

def run3_1_2_3():
    print("Building similarity matrix")
    similarity = mBuilder.buildSimilarityMatrix()
    np.set_printoptions(suppress=True)
    np.savetxt('./examples/fb_similarity_v2.txt', similarity, fmt='%i')
    fbAdj, fbEigenValues = originalFbEigen()

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
        evCorrelation = eigenValueCompare(adj, fbEigenValues, 'ego-facebook-adj_' + str(u))
        eigenValueCorrelations.append(evCorrelation)
        if evCorrelation > maxEVCorrelationVal:
            maxEVCorrelationVal = evCorrelation
            maxEVCorrelation = u
        if u == cfg.startUpUValue:
            plot.similarityPlot(adj, "Matrix de adyacencia valor u inicial")
            print("StartupCorrelation values. Eigen: " + str(evCorrelation) + ". Flatten: " + str(flatCorrelation))
        if u == cfg.optimumUValue:
            plot.similarityPlot(adj, "Matrix de adyacencia valor u ??ptimo")

    print("Max Flatten Correlation. U: " + str(maxFlattenCorrelation) + ". Value: " + str(maxFlattenCorrelationVal))
    print("Max EV Correlation. U: " + str(maxEVCorrelation) + ". Value: " + str(maxEVCorrelationVal))
    print("Flatten correlations: " + str(flattenCorrelations))
    print("Eigenvalues correlations: " + str(eigenValueCorrelations))
    plot.generateUCutsForFlatten(flattenCorrelations)
    plot.generateUCutsForEigenValues(eigenValueCorrelations)
    plot.compareUCuts(flattenCorrelations, eigenValueCorrelations)

def featureCovarianceMatrix(featureMatrix):
    featureMatrixT = np.transpose(featureMatrix)
    return (featureMatrixT @ featureMatrix) / (len(featureMatrix) - 1)

def substractMeanColumnFromEachColumn(m):
    for i in range(0, len(m[0])):
        columnI = np.squeeze(np.asarray(m[:,i]))
        averageOfColumnI = sum(columnI) / len(m)
        m[:, i] = m[:,i] - averageOfColumnI

def doPCA():
    if not Path(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt').is_file():
        sanitizer.sanitizeFeat()

    egoM = np.asmatrix(tpio.readMatrixFile(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt'))
    substractMeanColumnFromEachColumn(egoM)
    covFeatAdjust = featureCovarianceMatrix(egoM)
    _, fbEigenValues = originalFbEigen()
    covFeatAdjustFilename = "ego-facebook-cov-feat-adjust"
    writeMatrixToFile(covFeatAdjust, covFeatAdjustFilename)
    exec.runTpFor(covFeatAdjustFilename)
    l, V = tpio.readOutputFile(covFeatAdjustFilename)
    V = np.transpose(V)
    n = len(l)
    i = 0
    correlationsByUZoomIn = np.zeros(shape=(8, cfg.maxU))
    for k in cfg.kValuesZoomIn:
        vK = V[:, range(n-k, n)]
        kData = np.transpose(vK) @ np.transpose(egoM)
        kSimilarity = np.transpose(kData) @ kData
        for u in cfg.uPca:
            print("calculating k u: " + str(k) + " " + str(u))
            adjByU = adjacencyByU(kSimilarity, u)
            evCorrelation = eigenValueCompare(adjByU, fbEigenValues, 'ego-facebook-adj_k_' + str(k) + "_" + str(u))
            correlationsByUZoomIn[i,u] = evCorrelation
        i += 1
    plot.compareKUCutsZoomIn(correlationsByUZoomIn)

    correlationsByUZoomOut = np.zeros(shape=(8, cfg.maxU))
    i=0
    for k in cfg.kValuesZoomOut:
        vK = V[:, range(n-k, n)]
        kData = np.transpose(vK) @ np.transpose(egoM)
        kSimilarity = np.transpose(kData) @ kData
        for u in cfg.uPca:
            print("calculating k u: " + str(k) + " " + str(u))
            adjByU = adjacencyByU(kSimilarity, u)
            evCorrelation = eigenValueCompare(adjByU, fbEigenValues)
            correlationsByUZoomOut[i,u] = evCorrelation
        i += 1
    plot.compareKUCutsZoomOut(correlationsByUZoomOut)

def run3_4():
    doPCA()

def run():
    print("### Start Exercise 3 ###")
    run3_1_2_3()
    run3_4()