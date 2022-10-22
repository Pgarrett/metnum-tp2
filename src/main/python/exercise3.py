import config as cfg
import matrixBuilder as mBuilder

def adjacencyByU(similarity, u):
    result = []
    for row in similarity:
        rowResult = []
        for item in row:
            if item > u:
                rowResult.append(1)
            else:
                rowResult.append(0)
        result.append(rowResult)
    return result

# def flattenCompare(similarity, transformedFacebookEdgesFile):
#     for u in cfg.uValues:
#         adj = adjacencyByU(similarity, u)
        # doCompare
        # plotter.generateUCutsForFlatten

# def eigenValueCompare(transformedFacebookEdgesFile):
    # foreach u
        # adjacencyByU(u)
        # adjEigen = runTpFor(adj)
        # facebookEdgesEigen = runTpFor(transformedFacebookEdgesFile)
    # plotter.generateUCutsForEigenValues

# def chooseOptimumUValue():

def run():
    similarity = mBuilder.buildSimilarityMatrix()
    adj = adjacencyByU(similarity, 2)
    print(adj)


run()