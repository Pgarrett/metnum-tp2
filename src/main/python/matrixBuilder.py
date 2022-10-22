import numpy as np

import tpio
import os

# input: KarateKid
# output: KarateKid_laplacian.txt
#def buildLaplacianMatrix():

# input: facebook_filtered_sorted.feat, por ahora va a ser scratch.txt
# output: facebook_similarity.txt
def buildSimilarityMatrix():
    df = tpio.readMatrixFile(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt')
    transposedDf = np.transpose(df)
    similarity = df @ transposedDf
    return similarity

# input: facebook_similarity.txt, u
# output: facebook_$u_adj.txt
#def buildAdjacencyMatrix(u):

# input: facebook.edges
# output: facebook_edges_adj.txt
#def transformFacebookEdgesToAdjacencyMatrix():

# input: matrix, filename
# output: file written (no output)
#def writeToDisk():

buildSimilarityMatrix()