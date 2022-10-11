import comparator as cmp
import subprocess as sub
import config as c

def testPowerMethod(s):
	testResult = cmp.comparePowerMethod("../../../examples/" + s + ".txt", "../../../results/" + s + "_eigenValues.csv", "../../../results/" + s + "_eigenVectors.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("Testing Power Method..." + stringTestResult)

def testDeflationMethod(s):
	testResult = cmp.compareDeflationMethod("../../../examples/" + s + ".txt", "../../../results/" + s + "_eigenValues.csv", "../../../results/" + s + "_eigenVectors.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("Testing Deflation Method..." + stringTestResult)

def testSimilarityMatrix(s):
	testResult = cmp.compareSimilarityMethod("../../../examples/" + s + ".txt", "../../../results/" + s + "_similarityMatrix.csv")
	stringTestResult = "OK" if testResult else "NOT OK"
	print("Testing Similarity Matrix..." + stringTestResult)

def runTestsForExercise1b():
	sub.run("../../../tp2 exercise1b " + str(c.iterations) + " " + str(c.powerMethodEpsilon), shell=True)
	print("Running tests for Exercise 1b:")
	testPowerMethod("exercise1b")
	testDeflationMethod("exercise1b")
	testSimilarityMatrix("exercise1b")

def runTestsFor3b1b():
	sub.run("../../../tp2 3b1b " + str(c.iterations) + " " + str(c.powerMethodEpsilon), shell=True)
	print("Running tests for 3b1b:")
	testPowerMethod("3b1b")
	testDeflationMethod("3b1b")
	testSimilarityMatrix("3b1b")

runTestsForExercise1b()
runTestsFor3b1b()

