import comparator as cmp

def testPowerMethod(s):
	testResult = cmp.comparePowerMethod("../../../examples/" + s + ".txt", "../../../results/" + s + ".txt")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("Testing Power Method..." + stringTestResult)

def testDeflationMethod(s):
	print("Testing Deflation Method...NOT OK")

def testSimilarityMatrix(s):
	testResult = cmp.compareSimilarityMethod("../../../examples/" + s + ".txt", "../../../results/" + s + "_similarityMatrix.txt")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("Testing Similarity Matrix..." + stringTestResult)

def runTestsForExercise1b():
	print("Runing tests for Exercise 1b:")
	testPowerMethod("exercise1b")
	testDeflationMethod("exercise1b")
	testSimilarityMatrix("exercise1b")

runTestsForExercise1b()


