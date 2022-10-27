from pathlib import Path
import numpy as np
import sanitizer
import tpio
import os

def substractMeanColumnFromEachColumn(m):
    for i in range(0, len(m)):
        columnI = np.squeeze(np.asarray(m[:,i]))
        averageOfColumnI = sum(columnI) / len(m)
        m[:, i] = m[:,i] - averageOfColumnI

def doPCA():
    if not Path(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt').is_file():
        sanitizer.sanitizeFeat()

    egoM = np.asmatrix(tpio.readMatrixFile(str(os.getcwd()) + '/examples/ego-facebook-sorted.txt'))
    substractMeanColumnFromEachColumn(egoM)



