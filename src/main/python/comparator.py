import config as cfg
import numpy as np
import numpySolver as npt
import outputReader as outr
import asserter as asrt
import matplotlib.pyplot as plt
import networkx as nx

def comparePowerMethod(inputCppFile):
    numpyEighVal, numpyEighVec = npt.solve("./examples/" + inputCppFile  + ".txt")
    cppEighValues, cppEighVectors = outr.readOutputFile("./results/" + inputCppFile)
    return assertMaxValuesAreClose(numpyEighVal, np.transpose(numpyEighVec), cppEighValues, cppEighVectors)

def assertMaxValuesAreClose(numpyEighVal, numpyEighVec, cppEighVal, cppEighVec):
    _, maxNumpyEighVec = getHighestEigh(numpyEighVal, numpyEighVec)
    _, maxCppEighVec = getHighestEigh(cppEighVal, cppEighVec)
    return vectorsAreClose(maxCppEighVec, maxNumpyEighVec)

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


def compareSimilarityMethod(inputCppFile, outputCppFile):
    numpySimilarityMatrix = npt.solveSimilarityMatrix(inputCppFile)
    cppSimilarityMatrix = outr.readOutputMatrixFile(outputCppFile)
    return numpySimilarityMatrix == cppSimilarityMatrix

def compareProximityToNumpy(inputCppFile):
    npEigVal, numpyEighVec = npt.solve("./examples/autogen/" + inputCppFile  + ".txt")
    cppEigVal, cppEighVectors = outr.readOutputFile("./results/autogen/" + inputCppFile)
    eigenVectorDifference(np.transpose(numpyEighVec), cppEighVectors, inputCppFile)

def vectorsAreClose(v1, v2):
    if len(v1) != len(v2):
        return False

    res = True
    for i in range(0,len(v1)):
        absDiff = abs(v1[i]) - abs(v2[i])
        epsilon = cfg.compareToleranceEpsilon
        if  absDiff >= epsilon:
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

def eigenVectorDifference(npVectors, cppVectors, inputCppFile):
    result = []
    for npv, cpv in zip(npVectors, cppVectors):
        result.append(np.linalg.norm(npv-cpv))
    outr.writeOutProximity(inputCppFile, result)

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

def generateNetworkGraph(v):
    G = nx.Graph()
    group_0 =  []
    group_1 = []
    for index, value in enumerate(v):
        if value <= 0:
            group_0.append(index + 1)
        else:
            group_1.append(index+1)
    for i in range(len(group_0) - 1):
        G.add_edge(group_0[i], group_0[i+1])
    G.add_edge(group_0[0], group_0[-1])
    for i in range(len(group_1) - 1):
        G.add_edge(group_1[i], group_1[i+1])
    G.add_edge(group_1[0], group_1[-1])

    color_map = []
    for node in G:
        if node in group_0:
            color_map.append('tab:blue')
        else: 
            color_map.append('tab:green')

    pos = nx.spring_layout(G)

    # guardar grafo
    f = plt.figure()
    nx.draw(G, node_color=color_map, font_color="whitesmoke", with_labels=True)
    f.savefig('prediccion.png')

