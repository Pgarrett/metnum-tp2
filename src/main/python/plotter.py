import config as cfg
import matplotlib.pyplot as plt
import networkx as nx

def generateNetworkPlot(v):
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
    f = plt.figure()
    nx.draw(G, node_color=color_map, font_color="whitesmoke", with_labels=True)
    f.savefig('prediccion.png')

def generatePlotFromEdges(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    f = plt.figure()
    nx.draw(G, pos=pos, node_size=0.5, node_color='blue', font_color="whitesmoke", with_labels=False)
    f.savefig('grafo.png')

# iterate u values to form a line plot
def generateUCutsForFlatten(flatCorrelations):
    plt.xlabel("Valor de corte (u)")
    plt.ylabel("Correlación")
    plt.title("Correlación por flatten")
    plt.plot(cfg.uValues, flatCorrelations, color="blue")
    plt.legend()
    plt.show()

# iterate u values to form a line plot
def generateUCutsForEigenValues(eigenValCorrelations):
    plt.xlabel("Valor de corte (u)")
    plt.ylabel("Correlación")
    plt.title("Correlación por autovalores")
    plt.plot(cfg.uValues, eigenValCorrelations, color="red")
    plt.legend()
    plt.show()

def compareUCuts(flatCorrelations, eigenValCorrelations):
    plt.xlabel("Valor de corte (u)")
    plt.ylabel("Correlación")
    plt.title("Comparación de correlación")
    plt.plot(cfg.uValues, flatCorrelations, color="blue", label="Flatten")
    plt.plot(cfg.uValues, eigenValCorrelations, color="red", label="Autovalores")
    plt.legend()
    plt.show()
