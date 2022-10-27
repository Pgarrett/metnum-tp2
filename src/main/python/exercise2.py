from executor import runTpFor
from tpio import readOutputFile, readKarateLabels
from plotter import centralityGraph, generateNetworkPlot, networkDotGraph
from matrixBuilder import buildLaplacianMatrix
import numpy as np

def centrality(shouldExecute = True):
    if shouldExecute:
        runTpFor('karateclub')
    # read eigenvalues and eigenvectors
    _, eigenvec = readOutputFile('karateclub')
    # Plot centrality vector
    maxEigenVector = np.absolute(eigenvec[33])
    centralityGraph(maxEigenVector)
    # Plot network with weights according to eigenvector
    networkDotGraph()

def prediction(shouldExecute = True):
    laplacian = 'karateclub_laplacian'
    if shouldExecute:
        buildLaplacianMatrix('karateclub')
        runTpFor(laplacian)
    v = bestPrediction(laplacian)
    # Plot original group separation
    generateNetworkPlot(readKarateLabels(), 'original_network')
    # Plot predicted group separation
    generateNetworkPlot(v, 'predicted_network')

# Calculates correlation between all eigenvectors and original group separation
# return the eigenvector which best predicts the separation
def bestPrediction(output):
    result = []
    _, eigVec = readOutputFile(output)
    groupsVector = readKarateLabels()
    best = 0
    for i, vector in enumerate(eigVec):
        # calculates correlation coefficient, which in module is between 0 and 1.
        prediction = abs(np.corrcoef(vector, groupsVector)[0][1])
        if prediction >= best:
            best = prediction
            result = [i+1, prediction, vector]
    print('Autovector más cercano: V_' + str(result[0]) + ', con correlación: ' + str(result[1]))
    return result[2]

def run():
    print("### Start Exercise 2 ###")
    centrality()
    prediction()
