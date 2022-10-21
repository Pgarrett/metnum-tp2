import config as cfg
import numpy as np
import os

def readOutputFile(file):
    if cfg.debug:
        print("Reading output file ", file)
    outputEigenVectors = readEigenVectors(file + "_eigenVectors.csv")
    outputEigenValues = readEigenValues(file + "_eigenValues.csv")
    if cfg.debug:
        print("\nread matrix")
        print(outputEigenVectors)
        print("\nread outputEigenValues")
        print(outputEigenValues)
    return outputEigenValues, np.transpose(toNumpyMatrix(outputEigenVectors))


def toNumpyMatrix(matrix):
    np_arrays = []
    for arr in matrix:
        np_arrays.append(np.array(arr))
    return np_arrays


def readOutputMatrixFile(filename):
    with open(filename, "r") as file:
        m = [[float(num) for num in line.split(", ")] for line in file]
    return m


def readLabels():
    labelsPath = str(os.getcwd()) + '/examples/karateclub_labels.txt'
    labels = []
    with open(labelsPath, "r") as f:
        input = f.read()
        for line in input:
            if line == '1' or line == '0':
                labels.append(float(line))
    return labels


def addLinks(input, dotFile):
    wd = str(os.getcwd())
    # get links
    links = []
    with open(wd + "/examples/" + input + ".txt", "r") as f:
        graph_links = f.readlines()
        for line in graph_links:
            curr = []
            for v in line:
                if v == '0' or v == '1':
                    curr.append(v)
            links.append(curr)

    with open(wd + "/graphs/" + dotFile + ".dot", "r") as f:
        lines = f.readlines
        for line in lines:
            print(line)


def readEigenValues(filename):
    with open(filename, "r") as file:
        l = [line for line in file]
        l.pop(0)
        l = [float(line[:-2]) for line in l]
    return l


def readEigenVectors(filename):
    with open(filename, "r") as file:
        l = [line for line in file]
        vectorList = []
        for i in range(1, len(l)):
            vectorI = list(map(lambda x: float(x), l[i][:-3].split(", ")))
            vectorList.append(vectorI)
    return vectorList


def readLabels(filename):
    labels = []
    with open(filename, "r") as file:
        l = [line for line in file]
        for i in range(0, len(l)):
            labels.append(float(l[i]))
    return labels


def writeOutProximity(file, results):
    path = str(os.getcwd()) + "/results/"
    name = file + "_proximity.txt"
    with open(path + name, "w") as output:
        output.write(", ".join([str(n) for n in results]))


def writeOutAdjacencyMatrix(file, matrix):
    path = str(os.getcwd()) + "/results/"
    with open(path + file, "w") as output:
        for row in matrix:
            output.write(", ".join([str(n) for n in row]))
            output.write("\n")


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
