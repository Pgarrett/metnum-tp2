from pathlib import Path
import numpy as np
import cheater as ch
import config as cfg
import exercise3 as ex3
import sanitizer
import tpio
import os

def featureCovarianceMatrix(featureMatrix):
    featureMatrixT = np.transpose(featureMatrix)
    return (featureMatrixT @ featureMatrix) / (len(featureMatrix) - 1)

def substractMeanColumnFromEachColumn(m):
    for i in range(0, len(m)):
        columnI = np.squeeze(np.asarray(m[:,i]))
        averageOfColumnI = sum(columnI) / len(m)
        m[:, i] = m[:,i] - averageOfColumnI

def doPCA():
    if not Path(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt').is_file():
        sanitizer.sanitizeFeat()

    egoM = np.asmatrix(tpio.readMatrixFile(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt'))
    substractMeanColumnFromEachColumn(egoM)
    covFeatAdjust = featureCovarianceMatrix(egoM)
    correlationsByU = [[]] * cfg.uPca
    _, fbEigenValues = ex3.originalFbEigen()
    l, V = ch.superSimulateCppFor(covFeatAdjust)
    n = len(l)
    for k in cfg.kValues:
        vK = V[:, range(k, n)]
        kData = np.transpose(vK) @ np.transpose(egoM)
        kSimilarity = np.transpose(kData) @ kData
        for u in cfg.uPca:
            adjByU = ex3.adjacencyByU(kSimilarity, u)
            evCorrelation = ex3.eigenValueCompare(adjByU, fbEigenValues)
            correlationsByU[u].append(evCorrelation)

doPCA()
