from plotter import plotErrorMedian
import executor as exec
import tpio
import numpySolver as npt
import numpy as np
import config as cfg
import utils

def testExampleCases(shouldExecute = True):
    for i in range(1,4):
        runTestsForExamples(i, shouldExecute)

def runTestsForExamples(n, shouldExecute):
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
    cppEighValues, cppEighVectors = tpio.readOutputFile(inputCppFile)
    return assertMaxValuesAreClose(numpyEighVal, np.transpose(numpyEighVec), cppEighValues, cppEighVectors)

def compareDeflationMethod(inputCppFile):
    numpyEighVal, numpyEighVec = npt.solve("./examples/" + inputCppFile  + ".txt")
    cppEighValues, cppEighVectors = tpio.readOutputFile(inputCppFile)
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
        
def testParams():
    target = 'karateclub'
    iterations = ['1e3', '1e4', '1e5']
    tolerance = ['1e-4', '1e-6', '1e-7', '1e-8']
    testIterations(iterations, target)
    testTolerance(tolerance, target)

def testIterations(iterations, target):
    results = []
    labels = []
    for it in iterations:
        labels.append('#iter.: ' + it)
        exec.runTpFor(target, iterations=float(it))
        err = errorMedian(target)
        results.append(err)
    plotErrorMedian(results, labels)

def testTolerance(tolerance, target):
    results = []
    labels = []
    for eps in tolerance:
        labels.append('tolerancia: ' + eps)
        exec.runTpFor(target, epsilon=float(eps))
        err = errorMedian(target)
        results.append(err)
    plotErrorMedian(results, labels)


def errorMedian(input):
    numpyEighVal, numpyEighVec = npt.solve("./examples/" + input  + ".txt")
    cppEighValues, cppEighVectors = tpio.readOutputFile(input)
    result = [calculateErrorMedian(numpyEighVal, cppEighValues)]
    for npVec, cppVec in zip(np.transpose(numpyEighVec), cppEighVectors):
        result.append(calculateErrorMedian(npVec, cppVec))
    return result

def calculateErrorMedian(v1, v2):
    diff = []
    for i in range(0,len(v1)):
        diff.append(abs(v1[i]) - abs(v2[i]))
    return abs(np.median(diff))

def run():
    testExampleCases()
    testParams()

run()
