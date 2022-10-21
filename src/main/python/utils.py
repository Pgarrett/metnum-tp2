import config as cfg
import numpy as np
import outputReader as outr
import os

def buildLaplacianFor(input):
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

def getFacebookEdges():
    edges = []
    path = os.getcwd() + '/examples/ego-facebook.edges'
    with open(path, 'r') as file:
        for line in file:
            pair = [int(node.rstrip('\n')) for node in line.split(' ')]
            edges.append((pair[0], pair[1]))
    return edges

# Return dictionay with facebook nodes and their oredered positions
def sortFacebookNodes(edges):
    result = {}
    nodes = []
    for n1, n2 in edges:
        nodes.append(n1)
        nodes.append(n2)
    # remove duplicates
    nodes = list(dict.fromkeys(nodes))
    # sort nodes by label
    nodes.sort()

    for index, node in enumerate(nodes):
        result[node] = index
    return result

# Delete lines that don't belong to facebook nodes
def filterNodesFromFeatures():
    edges = getFacebookEdges()
    nodes = sortFacebookNodes(edges)
    outr.filterNodesFromFeatures(nodes)

def buildAdjacencyMatrixFromSimilarity(similarity, threshold):
    m = len(similarity)
    matrix = []
    for i in range(m):
        row = [0] * m
        for j in range(m):
            if similarity[i][j] > threshold:
                row[j] = 1
        matrix.append(row)
    return matrix

def buildAdjacencyMatrixFromFacebookEdges():
    edges = getFacebookEdges()
    nodes = sortFacebookNodes(edges)
    m = len(nodes.keys()) # cantidad de nodos

    matrix = [[0] * m for _ in range(m)]
    for n1, n2 in edges:
        row = nodes[n1]
        col = nodes[n2]
        matrix[row][col] = 1
        matrix[col][row] = 1

    outr.writeOutAdjacencyMatrix('facebook_adjacency.txt', matrix)
    return matrix
