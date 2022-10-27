import numpy as np
import os
import tpio
from pathlib import Path
import sanitizer

# input: KarateKid
# output: KarateKid_laplacian.txt
def buildLaplacianMatrix(input):
    print('Building Laplacian matrix for file: {input}'.format(input=input))
    path = str(os.getcwd()) + "/examples/" + input
    laplacian = []
    with open(path + ".txt", "r") as f:
        rows = f.readlines()
        for i, row in enumerate(rows):
            new_row = []
            degree = 0
            for j in range(len(row)):
                if row[j] == '1' or row[j] == '0':
                    new_row.append(-int(row[j]))
                    degree += int(row[j])
            new_row[i] = degree
            laplacian.append(new_row)
        
    with open(path + "_laplacian.txt", "w") as output:
        for line in laplacian:
            output.write(" ".join([str(n) for n in line]) + "\n")
    return input + "_laplacian"

# input: facebook_filtered_sorted.feat, por ahora va a ser scratch.txt
# output: facebook_similarity.txt
def buildSimilarityMatrix():
    if not Path(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt').is_file():
        sanitizer.sanitizeFeat()

    egoM = tpio.readMatrixFile(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt')
    transposedEgoM = np.transpose(egoM)
    similarity = egoM @ transposedEgoM
    return similarity

# input: facebook.edges
# output: facebook_edges_adj.txt
def transformFacebookEdgesToAdjacencyMatrix():
    featureMatrix = tpio.readEdgesFile('/examples/ego-facebook-sorted.txt')
    adjacencyMatrix = [[0] * len(featureMatrix) for _ in range(len(featureMatrix))]
    edgesMatrix = tpio.readEdgesFile('/examples/ego-facebook.edges')

    for edge in edgesMatrix:
        indexNode1 = egoIndexByNodeNumber(edge[0], featureMatrix)
        indexNode2 = egoIndexByNodeNumber(edge[1], featureMatrix)
        adjacencyMatrix[indexNode1][indexNode2] = 1
        adjacencyMatrix[indexNode2][indexNode1] = 1

    tpio.writeOutMatrix('/examples/ego-facebook-adj.txt', adjacencyMatrix)
    return adjacencyMatrix

def egoIndexByNodeNumber(number, featureMatrix):
    nodeNumberList = [row[0] for row in featureMatrix]
    for i in range(0, len(nodeNumberList)):
        if nodeNumberList[i] == number:
            return i

    return -1   #if not present: we fail

