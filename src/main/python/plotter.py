import config as cfg
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pydot
import os

def plotErrorMedian(arr, labels):
    x = np.array(list(range(len(arr[0]))))
    fig, ax = plt.subplots()
    plt.xticks(x)
    plt.xlabel("Vectores")
    plt.ylabel("Media del error")
    for vector, label in zip(arr, labels):
        ax.scatter(x, np.array(vector), label=label)
    ax.legend()
    plt.show()

def generateNetworkPlot(v, name):
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

    # guardar grafo
    path = os.getcwd() + '/graphs/'
    f = plt.figure()
    nx.draw(G, node_color=color_map, font_color="whitesmoke", with_labels=True)
    f.savefig(path + name + '.png')

def generatePlotFromEdges(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    f = plt.figure()
    nx.draw(G, pos=pos, node_size=0.5, node_color='blue', font_color="whitesmoke", with_labels=False)
    f.savefig('grafo.png')

def centralityGraph(eigenvec):
    x = list(range(1, len(eigenvec) + 1))
    plt.xticks(x)
    plt.xlabel("Nodos")
    plt.ylabel("Centralidad")
    plt.scatter(x, eigenvec, color="blue")
    plt.show()

def networkDotGraph():
    path = os.getcwd()
    graphs = pydot.graph_from_dot_file(path + "/graphs/centrality.dot")
    graph = graphs[0]
    links = []

    with open(path + "/examples/karateclub.txt", "r") as f:
        graph_links = f.readlines()
        for line in graph_links:
            curr = []
            for v in line:
                if v == '0' or v == '1':
                    curr.append(v)
            links.append(curr)

    for i, edges in enumerate(links):
        for j, edge in enumerate(edges):
            if edge == '1' and i < j:
                my_edge = pydot.Edge(str(i+1), str(j+1))
                graph.add_edge(my_edge)
            
    graph.write_png(path + "/graphs/centrality_graph.png")

# iterate u values to form a line plot
# def generateUCutsForFlatten():

# iterate u values to form a line plot
# def generateUCutsForEigenValues():
# iterate u values to form a line plot
def generateUCutsForFlatten(flatCorrelations):
    plt.xlabel("Valor de corte (u)")
    plt.ylabel("Correlaci??n")
    plt.title("Correlaci??n por flatten")
    plt.plot(cfg.uValues, flatCorrelations, color="blue")
    plt.legend()
    plt.show()

# iterate u values to form a line plot
def generateUCutsForEigenValues(eigenValCorrelations):
    plt.xlabel("Valor de corte (u)")
    plt.ylabel("Correlaci??n")
    plt.title("Correlaci??n por autovalores")
    plt.plot(cfg.uValues, eigenValCorrelations, color="red")
    plt.legend()
    plt.show()

def compareUCuts(flatCorrelations, eigenValCorrelations):
    plt.xlabel("Valor de corte (u)")
    plt.ylabel("Correlaci??n")
    plt.title("Comparaci??n de correlaci??n")
    plt.plot(cfg.uValues, flatCorrelations, color="blue", label="Flatten")
    plt.plot(cfg.uValues, eigenValCorrelations, color="red", label="Autovalores")
    plt.legend()
    plt.show()

def compareKUCutsZoomIn(kCorrelations):
    plt.xlabel("Umbral")
    plt.ylabel("Correlaci??n")
    plt.title("Umbral vs Correlaci??n")
    k = 1
    for kCorrelation in kCorrelations:
        plt.plot(cfg.uPca, kCorrelation, label="k="+str(k))
        k += cfg.stepKByZoomIn
    valuesOf1 = [1]*(kCorrelations.shape[1])
    plt.plot(cfg.uPca, valuesOf1, color='black', linestyle='dashed')
    plt.legend()
    plt.show()

def compareKUCutsZoomOut(kCorrelations):
    plt.xlabel("Umbral")
    plt.ylabel("Correlaci??n")
    plt.title("Umbral vs Correlaci??n")
    k = 1
    for kCorrelation in kCorrelations:
        plt.plot(cfg.uPca, kCorrelation, label="k="+str(k))
        k += cfg.stepKByZoomOut
    valuesOf1 = [1]*(kCorrelations.shape[1])
    plt.plot(cfg.uPca, valuesOf1, color='black', linestyle='dashed')
    plt.legend()
    plt.show()

def similarityPlot(matrix, plotTitle):
    plt.title(plotTitle)
    plt.xlabel("N??mero nodo")
    plt.ylabel("N??mero nodo")
    plt.imshow(matrix, interpolation="nearest")
    plt.show()