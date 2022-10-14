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

def runTestsForExercise1b():
	exec.runTpFor("resolverEnComputadora1")
	print("\nRunning tests for Exercise 1b:")
	testPowerMethod("resolverEnComputadora1")
	testDeflationMethod("resolverEnComputadora1")
	testSimilarityMatrix("resolverEnComputadora1")

def runTestsForKarate():
	exec.runTpFor("karateclub")
	print("\nRunning tests for Karate:")
	testPowerMethod("karateclub")
	testDeflationMethod("karateclub")
	testSimilarityMatrix("karateclub")

def runTestsFor3b1b():
	exec.runTpFor("3b1b")
	print("\nRunning tests for 3b1b:")
	testPowerMethod("3b1b")
	testDeflationMethod("3b1b")
	testSimilarityMatrix("3b1b")

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
	print("\nRunning tests for 3b1b:")
	testPowerMethod(target)
	testDeflationMethod(target)
	testSimilarityMatrix(target)

def testNumpyCases():
	# for n in range(3, 4)
	n = 3
	# numpyGenerator(n)
	runTestsForNumpyGen(n)

# numpyGenerator()
testNumpyCases()
# runTestsForKarate()
# runTestsForExercise1b()
# runTestsFor3b1b()

