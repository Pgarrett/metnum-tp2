import config as cfg
import numpy as np
import numpySolver as npt
import outputReader as outr
import utils

def comparePowerMethod(inputCppFile):
    numpyEighVal, numpyEighVec = npt.solve("./examples/" + inputCppFile  + ".txt")
    cppEighValues, cppEighVectors = outr.readOutputFile("./results/" + inputCppFile)
    return assertMaxValuesAreClose(numpyEighVal, np.transpose(numpyEighVec), cppEighValues, cppEighVectors)

def assertMaxValuesAreClose(numpyEighVal, numpyEighVec, cppEighVal, cppEighVec):
    _, maxNumpyEighVec = utils.getHighestEigh(numpyEighVal, numpyEighVec)
    _, maxCppEighVec = utils.getHighestEigh(cppEighVal, cppEighVec)
    return vectorsAreClose(maxCppEighVec, maxNumpyEighVec)

def compareDeflationMethod(inputCppFile):
    numpyEighVal, numpyEighVec = npt.solve("./examples/" + inputCppFile  + ".txt")
    cppEighValues, cppEighVectors = outr.readOutputFile("./results/" + inputCppFile)
    eighenValuesAreClose = vectorsAreClose(numpyEighVal, cppEighValues)
    if not eighenValuesAreClose:
        print("Eighenvalue compare failed")
    eighenVectorsAreClose = vectorListsAreClose(np.transpose(numpyEighVec), cppEighVectors)
    if not eighenValuesAreClose:
        print("Eighenvectors compare failed")
    return eighenValuesAreClose and eighenVectorsAreClose


def compareSimilarityMethod(inputCppFile, outputCppFile):
    numpySimilarityMatrix = npt.solveSimilarityMatrix(inputCppFile)
    cppSimilarityMatrix = outr.readOutputMatrixFile(outputCppFile)
    return numpySimilarityMatrix == cppSimilarityMatrix

def compareProximityToNumpy(inputCppFile):
    _, numpyEighVec = npt.solve("./examples/autogen/" + inputCppFile  + ".txt")
    _, cppEighVectors = outr.readOutputFile("./results/autogen/" + inputCppFile)
    eigenVectorDifference(np.transpose(numpyEighVec), cppEighVectors, inputCppFile)

def vectorsAreClose(v1, v2):
    if len(v1) != len(v2):
        return False

    res = True
    for i in range(0,len(v1)):
        absDiff = abs(v1[i]) - abs(v2[i])
        epsilon = cfg.compareToleranceEpsilon
        if  absDiff >= epsilon:
            res = False

    return res

def vectorListsAreClose(l1, l2):
    if len(l1) != len(l2):
        return False

    res = True
    for i in range(0,len(l1)):
        if not vectorsAreClose(l1[i], l2[i]):
            res = False

    return res

def eigenVectorDifference(npVectors, cppVectors, inputCppFile):
    result = []
    for npv, cpv in zip(npVectors, cppVectors):
        result.append(np.linalg.norm(npv-cpv))
    outr.writeOutProximity(inputCppFile, result)

def bestPrediction():
    result = []
    _, eigVec = outr.readOutputFile('./results/karateclub_laplacian')
    groupsVector = outr.readLabels('./examples/karateclub_labels.txt')
    best = 0
    for i, vector in enumerate(eigVec):
        prediction = abs(np.corrcoef(vector, groupsVector)[0][1])
        if prediction > best:
            best = prediction
            result = [i+1, prediction, vector]
    print('Autovector más cercano: V_' + str(result[0]) + ', con correlación: ' + str(result[1]))
    return result[2]
