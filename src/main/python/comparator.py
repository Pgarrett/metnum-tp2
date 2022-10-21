
import numpy as np


def compareSimilarityMethod(inputCppFile, outputCppFile):
    numpySimilarityMatrix = npt.solveSimilarityMatrix(inputCppFile)
    cppSimilarityMatrix = outr.readOutputMatrixFile(outputCppFile)
    return numpySimilarityMatrix == cppSimilarityMatrix


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
