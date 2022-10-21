import subprocess as sub
import config as cfg
import os

def runTpFor(input, iterations = cfg.iterations, epsilon = cfg.powerMethodEpsilon):
    # print("Running TP for file: %s", input)
    # print(str(os.getcwd()))
    tp2 = str(os.getcwd()) + "/tp2"
    cmd = [tp2, input, str(iterations), str(epsilon)]
    sub.run(cmd)
