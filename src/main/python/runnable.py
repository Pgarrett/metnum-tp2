import comparator as cmp
import executor as exec

def testPowerMethod(s):
	testResult = cmp.comparePowerMethod("./examples/" + s + ".txt", "./results/" + s + "_eigenValues.csv", "./results/" + s + "_eigenVectors.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("\tTesting Power Method..." + stringTestResult)

def testDeflationMethod(s):
	testResult = cmp.compareDeflationMethod("./examples/" + s + ".txt", "./results/" + s + "_eigenValues.csv", "./results/" + s + "_eigenVectors.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("\tTesting Deflation Method..." + stringTestResult)

def testSimilarityMatrix(s):
	testResult = cmp.compareSimilarityMethod("./examples/" + s + ".txt", "./results/" + s + "_similarityMatrix.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("\tTesting Similarity Matrix..." + stringTestResult)

def runTestsForExercise1b():
	exec.runTpFor("exercise1b")
	print("\nRunning tests for Exercise 1b:")
	testPowerMethod("exercise1b")
	testDeflationMethod("exercise1b")
	testSimilarityMatrix("exercise1b")

def runTestsFor3b1b():
	exec.runTpFor("3b1b")
	print("\nRunning tests for 3b1b:")
	testPowerMethod("3b1b")
	testDeflationMethod("3b1b")
	testSimilarityMatrix("3b1b")

runTestsForExercise1b()
runTestsFor3b1b()

