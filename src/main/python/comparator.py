import config as cfg
import numpy as np
import numpySolver as npt
import outputReader as outr
import asserter as asrt

def comparePowerMethod(inputCppFile):
    numpyEighVal, numpyEighVec = npt.solve("./examples/" + inputCppFile  + ".txt")
    cppEighValues, cppEighVectors = outr.readOutputFile("./results/" + inputCppFile)
    return assertMaxValuesAreClose(numpyEighVal, np.transpose(numpyEighVec), cppEighValues, cppEighVectors)

def assertMaxValuesAreClose(numpyEighVal, numpyEighVec, cppEighVal, cppEighVec):
    _, maxNumpyEighVec = getHighestEigh(numpyEighVal, numpyEighVec)
    _, maxCppEighVec = getHighestEigh(cppEighVal, cppEighVec)
    return vectorsAreClose(maxCppEighVec, maxNumpyEighVec)

def getHighestEigh(eighVal, eighVect):
    maxEighValIndex = np.argmax(eighVal)
    maxEighVal = eighVal[maxEighValIndex]
    maxEighVec = eighVect[maxEighValIndex]
    if cfg.debug:
        print("Max Eighenvalue:")
        print(maxEighVal)
        print("Max Eighenvector:")
        print(maxEighVec)
    return maxEighVal, maxEighVec

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
    npEigVal, numpyEighVec = npt.solve("./examples/autogen/" + inputCppFile  + ".txt")
    cppEigVal, cppEighVectors = outr.readOutputFile("./results/autogen/" + inputCppFile)
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
    results = []
    _, eigVec = outr.readOutputFile('./results/karateclub_laplacian')
    groupsVector = outr.readLabels('./examples/karateclub_labels.txt')
    for vector in eigVec:
        prediction = np.corrcoef(vector, groupsVector)[0][1]
        print(prediction)
        results.append(prediction)
    return results

