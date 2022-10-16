import outputReader as outr
import comparator as cmp
import executor as exec
import numpy as np

def testPowerMethod(s):
	testResult = cmp.comparePowerMethod(s)
	stringTestResult = "OK" if testResult else "NOT OK"
	print("\tTesting Power Method..." + stringTestResult)

def testDeflationMethod(s):
	# testResult = cmp.compareDeflationMethod("./examples/" + s + ".txt", "./results/" + s + "_eigenValues.csv", "./results/" + s + "_eigenVectors.csv")
	testResult = cmp.compareDeflationMethod(s)
	stringTestResult = "OK" if testResult else "NOT OK"
	print("\tTesting Deflation Method..." + stringTestResult)

def testSimilarityMatrix(s):
	testResult = cmp.compareSimilarityMethod("./examples/" + s + ".txt", "./results/" + s + "_similarityMatrix.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("\tTesting Similarity Matrix..." + stringTestResult)

def testProximityToNumpy(s):
	proximity_array = []
	iterations = [1e3, 1e4, 5e4, 1e5, 2e5, 3e5]
	tolerance = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
	for iter in iterations:
		for eps in tolerance:
			exec.runTpFor(s, iter, eps)
			testResult = cmp.compareProximityToNumpy(s)
			result = [iter, eps] + testResult
			proximity_array.append(result)
	outr.writeOutProximity(proximity_array)

def runTestsFor(file, iterations = None, epsilon = None):
	exec.runTpFor(file, iterations, epsilon)
	print("\nRunning tests for: " + file)
	testPowerMethod(file)
	testDeflationMethod(file)
	testSimilarityMatrix(file)

def numpyGenerator(n):
	m = int((n*(n-1))/4)
	A = np.zeros((n,n))
	r,c = np.triu_indices(n,1)
	ix = np.random.choice(np.arange(len(r)), m, replace=False)
	r = r[ix]
	c = c[ix]
	A[r,c] = 1
	A = A + A.T
	print(A)
	np.set_printoptions(suppress=True)
	np.savetxt('./examples/autogen/matrix_' + str(n) + '.txt', A, fmt='%i')

def runTestsForNumpyGen(n):
	target = 'autogen/matrix_' + str(n)
	exec.runTpFor(target)
	print("\nRunning tests for " + target + ":")
	testPowerMethod(target)
	testDeflationMethod(target)
	testSimilarityMatrix(target)

def testNumpyCases():
	# for n in range(3, 4)
	n = 10
	# numpyGenerator(n)
	runTestsForNumpyGen(n)


# numpyGenerator()
# testNumpyCases()
# runTestsFor('karateclub')
# testProximityToNumpy('karateclub')
