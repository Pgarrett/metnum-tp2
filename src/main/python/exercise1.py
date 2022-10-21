import comparator as cmp
import executor as exec
import io as outr
import numpySolver as npt
import numpy as np
import config as cfg
import utils

def testNumpyCases(shouldExecute = False):
    for i in range(1,4):
        runTestsForHandExamples(i, shouldExecute)

def runTestsForHandExamples(n, shouldExecute):
    target = 'test_deflation_' + str(n)
    if shouldExecute:
        exec.runTpFor(target)
    print("Running test_deflation_ " + target + ": ")
    testPowerMethod(target)
    testDeflationMethod(target)

def testPowerMethod(s):
    testResult = comparePowerMethod(s)
    stringTestResult = "OK" if testResult else "NOT OK"
    print("\tTesting Power Method..." + stringTestResult)

def testDeflationMethod(s):
    testResult = compareDeflationMethod(s)
    stringTestResult = "OK" if testResult else "NOT OK"
    print("\tTesting Deflation Method..." + stringTestResult)

def comparePowerMethod(inputCppFile):
    numpyEighVal, numpyEighVec = npt.solve("./examples/" + inputCppFile  + ".txt")
    cppEighValues, cppEighVectors = outr.readOutputFile("./results/" + inputCppFile)
    return assertMaxValuesAreClose(numpyEighVal, np.transpose(numpyEighVec), cppEighValues, cppEighVectors)

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

def assertMaxValuesAreClose(numpyEighVal, numpyEighVec, cppEighVal, cppEighVec):
    _, maxNumpyEighVec = utils.getHighestEigh(numpyEighVal, numpyEighVec)
    _, maxCppEighVec = utils.getHighestEigh(cppEighVal, cppEighVec)
    return vectorsAreClose(maxCppEighVec, maxNumpyEighVec)

def vectorsAreClose(v1, v2):
    if len(v1) != len(v2):
        return False

    res = True
    for i in range(0,len(v1)):
        absDiff = abs(v1[i]) - abs(v2[i])
        epsilon = cfg.compareToleranceEpsilon
        if absDiff >= epsilon:
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