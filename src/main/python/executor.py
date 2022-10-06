import subprocess as sub
import config as cfg

def runTpFor(input):
    print("Running TP for file: %s", input)
    sub.run("../../../tp2 %s %s %s", input, str(cfg.iterations), str(cfg.powerMethodEpsilon))