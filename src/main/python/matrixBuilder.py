from tpio import readMatrixFile
import numpy as np
import os

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
    df = readMatrixFile(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt')
    transposedDf = np.transpose(df)
    similarity = df @ transposedDf
    return similarity

# input: facebook_similarity.txt, u
# output: facebook_$u_adj.txt
#def buildAdjacencyMatrix(u):

# input: facebook.edges
# output: facebook_edges_adj.txt
def transformFacebookEdgesToAdjacencyMatrix():
    return []

# input: matrix, filename
# output: file written (no output)
#def writeToDisk():

buildSimilarityMatrix()
