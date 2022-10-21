from tokenize import group
import executor as exec
import io as outr
import matplotlib.pyplot as plt
import numpy as np
import csv

from scipy import stats


def centrality(input, shouldExecute = False):
    if shouldExecute:
        exec.runTpFor(input)
    
    eigenval, eigenvec = outr.readOutputFile(input)
    eigenvalReader = csv.reader(eigenval)
    eigenvecReader = csv.reader(eigenvec)

    # Read csv files header
    next(eigenvalReader)
    next(eigenvecReader)

    maxEigenVector = []
    for row in eigenvecReader:
        # read first column of eigen vectors matrix
        maxEigenVector.append(float(row[0]))
    centralityGraph(maxEigenVector)

    eigenval.close()
    eigenvec.close()

def centralityGraph(eigenvec):
    x = list(range(1, len(eigenvec) + 1))
    plt.xticks(x)
    plt.xlabel("Nodos")
    plt.ylabel("Centralidad")
    plt.scatter(x, eigenvec, color="blue")
    plt.show()

def bestPrediction(input, shouldExecute = False):
    laplacian = input + '_laplacian'
    if shouldExecute:
        exec.buildLaplacianFor(input)
        exec.runTpFor(laplacian)
    eigenval, eigenvec = outr.readOutputFile(laplacian)
    groupsVector = outr.readLabels()
    eigenvecReader = csv.reader(eigenvec)
    header = np.array(next(eigenvecReader))

    correlations = []
    for i in range(len(header) - 1):
        currentVector = []
        # read i-th eigenvector
        for row in eigenvecReader:
            currentVector.append(float(row[i]))
        # reset reader
        eigenvec.seek(0)
        next(eigenvecReader)
        # calculate correlation
        corr = stats.pearsonr(currentVector, groupsVector).pvalue
        correlations.append(corr)

    correlationGraph(correlations)

    eigenval.close()
    eigenvec.close()

def correlationGraph(correlations):
    print(correlations)

# Execute
centrality('karateclub')
bestPrediction('karateclub')

        
