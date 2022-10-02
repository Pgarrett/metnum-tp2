import config as cfg
import numpy as np
import numpySolver as npt
import outputReader as outr
import asserter as asrt

def compare(inputCppFile, outputCppFile):
    numpyEighVal, numpyEighVec = npt.solve(inputCppFile)
    cppEighVal, cppEighVec = outr.readOutputFile(outputCppFile)
    assertMaxValuesAreClose(numpyEighVal, numpyEighVec, cppEighVal, cppEighVec)

def assertMaxValuesAreClose(numpyEighVal, numpyEighVec, cppEighVal, cppEighVec):
    maxNumpyEighVal, maxNumpyEighVec = getHighestEigh(numpyEighVal, numpyEighVec)
    maxCppEighVal, maxCppEighVec = getHighestEigh(cppEighVal, cppEighVec)
    asrt.assertAllClose(maxCppEighVec, maxNumpyEighVec)

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