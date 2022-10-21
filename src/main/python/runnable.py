import tpio as outr
import comparator as cmp
import executor as exec
import numpy as np
import utils
import plotter
import config as cfg

def testSimilarityMatrix(s):
	testResult = cmp.compareSimilarityMethod("./examples/" + s + ".txt", "./results/" + s + "_similarityMatrix.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("\tTesting Similarity Matrix..." + stringTestResult)



def runTestsFor(file, shouldExecute = False, iterations = None, epsilon = None):
	if shouldExecute:
		if iterations and epsilon:
			exec.runTpFor(file, iterations, epsilon)
		else:
			exec.runTpFor(file)
	print("\nRunning tests for: " + file)
	testPowerMethod(file)
	testDeflationMethod(file)
	#testSimilarityMatrix(file)

def testPrediction(shouldExecute = False):
	if shouldExecute:
		exec.runTpFor('karateclub_laplacian')
	prediction = cmp.bestPrediction()
	cmp.generateNetworkGraph(prediction)


def Facebook():
	utils.buildAdjacencyMatrixFromFacebookEdges()
	utils.filterNodesFromFeatures()



def readInput(input):
	matrixText = open(input, "r")
	matrix = [list(map(int, line.split())) for line in matrixText]
	np_arrays = []
	for arr in matrix:
		np_arrays.append(np.array(arr[1:len(arr)]))
	return np_arrays

def calculateSimilarity(input):
	fbInput = readInput(input)
	if cfg.debug:
		print("Input:")
		print(fbInput)
	fbInputTranspose = np.transpose(fbInput)
	if cfg.debug:
		print("InputTranspose:")
		print(fbInputTranspose)
	similarity = fbInput @ fbInputTranspose
	if cfg.debug:
		print("Similarity:")
		print(similarity)
	return similarity

def buildTestSimilarity():
	calculateSimilarity("./examples/scratch.txt")

def buildFbSimilarity():
	similarity = calculateSimilarity("./examples/ego-facebook.feat")
	np.set_printoptions(suppress=True)
	np.savetxt('./examples/fb_similarity.txt', similarity, fmt='%i')

# numpyGenerator()
# testNumpyCases(True)
# runTestsFor('karateclub_laplacian')

# testPrediction()
# Facebook()
# buildTestSimilarity()
buildFbSimilarity()
