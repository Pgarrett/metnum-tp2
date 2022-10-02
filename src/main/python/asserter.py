import numpy as np

def assertAllClose(cppEighenVec, npEighenVec):
    if np.allclose(cppEighenVec, npEighenVec):
        print("Hurray cowboy! Your implementation rocks")
    else:
        print("Better check your impl my friend, results are not close enough")