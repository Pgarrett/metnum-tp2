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
    maxNumpyEighVal, maxNumpyEighVec = getHighestEigh(numpyEighVal, numpyEighVec)
    maxCppEighVal, maxCppEighVec = getHighestEigh(cppEighVal, cppEighVec)
    # return asrt.assertAllClose(maxCppEighVec, maxNumpyEighVec)
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
    return vectorsAreClose(numpyEighVal, cppEighValues) and vectorListsAreClose(np.transpose(numpyEighVec), cppEighVectors)

def compareSimilarityMethod(inputCppFile, outputCppFile):
    numpySimilarityMatrix = npt.solveSimilarityMatrix(inputCppFile)
    cppSimilarityMatrix = outr.readOutputMatrixFile(outputCppFile)
    return numpySimilarityMatrix == cppSimilarityMatrix

def vectorsAreClose(v1, v2):
    if len(v1) != len(v2):
        return False

    for i in range(0,len(v1)):
        absDiff = abs(v1[i]) - abs(v2[i])
        epsilon = cfg.compareToleranceEpsilon
        if  absDiff >= epsilon:
            return False

    return True

def vectorListsAreClose(l1, l2):
    if len(l1) != len(l2):
        return False

    for i in range(0,len(l1)):
        if not vectorsAreClose(l1[i], l2[i]):
            return False

    return True





