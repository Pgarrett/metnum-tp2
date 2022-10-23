import os
import numpy as np

def filterFeat():
    edges = getFacebookEdges()
    nodes = sortFacebookEdges(edges)
    return filterNodesFromFeatures(nodes)

def getFacebookEdges():
    edges = []
    path = os.getcwd() + '/examples/ego-facebook.edges'
    with open(path, 'r') as file:
        for line in file:
            pair = [int(node.rstrip('\n')) for node in line.split(' ')]
            edges.append((pair[0], pair[1]))
    return edges

# Return dictionay with facebook nodes and their ordered positions
def sortFacebookEdges(edges):
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
def filterNodesFromFeatures(nodes):
    read_path = str(os.getcwd()) + "/examples/ego-facebook.feat"
    with open(read_path, "r") as input:
        lines = input.readlines()

    write_path = str(os.getcwd()) + "/examples/ego-facebook-filtered.feat"
    with open(write_path, "w") as output:
        for line in lines:
            node = int(line.split(None, 1)[0])
            if node in nodes.keys():
                output.write(line)
    return write_path

def sortFeat(filteredFeat):
    matrixText = open(filteredFeat, "r")
    matrix = [list(map(int, line.split())) for line in matrixText]
    matrix.sort()
    np.set_printoptions(suppress=True)
    np.savetxt('./examples/ego-facebook-sorted.txt', matrix, fmt='%i')

def sanitizeFeat():
    filteredFeat = filterFeat()
    sortFeat(filteredFeat)

sanitizeFeat()