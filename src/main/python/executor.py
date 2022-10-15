import subprocess as sub
import config as cfg
import os

def runTpFor(input):
    print("Running TP for file: %s", input)
    print(str(os.getcwd()))
    tp2 = str(os.getcwd()) + "/tp2"
    cmd = [tp2, input, str(cfg.iterations), str(cfg.powerMethodEpsilon)]
    sub.run(cmd)

runTpFor('karateclub')
