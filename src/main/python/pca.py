from pathlib import Path
import numpy as np
import cheater as ch
import config as cfg
import exercise3 as ex3
import sanitizer
import tpio
import os
import plotter as plt

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
    _, fbEigenValues = ex3.originalFbEigen()
    l, V = ch.superSimulateCppFor(covFeatAdjust)
    n = len(l)
    i = 0
    correlationsByUZoomIn = np.zeros(shape=(8, cfg.maxU))
    for k in cfg.kValuesZoomIn:
        vK = V[:, range(n-k, n)]
        kData = np.transpose(vK) @ np.transpose(egoM)
        kSimilarity = np.transpose(kData) @ kData
        for u in cfg.uPca:
            print("calculating k u: " + str(k) + " " + str(u))
            adjByU = ex3.adjacencyByU(kSimilarity, u)
            evCorrelation = ex3.eigenValueCompare(adjByU, fbEigenValues)
            correlationsByUZoomIn[i,u] = evCorrelation
        i += 1
    plt.compareKUCutsZoomIn(correlationsByUZoomIn)

    correlationsByUZoomOut = np.zeros(shape=(8, cfg.maxU))
    i=0
    for k in cfg.kValuesZoomOut:
        vK = V[:, range(n-k, n)]
        kData = np.transpose(vK) @ np.transpose(egoM)
        kSimilarity = np.transpose(kData) @ kData
        for u in cfg.uPca:
            print("calculating k u: " + str(k) + " " + str(u))
            adjByU = ex3.adjacencyByU(kSimilarity, u)
            evCorrelation = ex3.eigenValueCompare(adjByU, fbEigenValues)
            correlationsByUZoomOut[i,u] = evCorrelation
        i += 1
    plt.compareKUCutsZoomOut(correlationsByUZoomOut)

doPCA()
