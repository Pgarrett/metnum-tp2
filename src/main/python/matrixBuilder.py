# input: KarateKid
# output: KarateKid_laplacian.txt
def buildLaplacianMatrix():

# input: facebook_filtered_sorted.feat
# output: facebook_similarity.txt
def buildSimilarityMatrix():

# input: facebook_similarity.txt, u
# output: facebook_$u_adj.txt
def buildAdjacencyMatrix(u):

# input: facebook.edges
# output: facebook_edges_adj.txt
def transformFacebookEdgesToAdjacencyMatrix():

# input: matrix, filename
# output: file written (no output)
def writeToDisk():