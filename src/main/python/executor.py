import subprocess as sub
import config as cfg
import os

def runTpFor(input):
    print('Running TP for file: {input}'.format(input=input))
    tp2 = str(os.getcwd()) + "/tp2"
    cmd = [tp2, input, str(cfg.iterations), str(cfg.powerMethodEpsilon)]
    sub.run(cmd)

def buildLaplacianFor(input):
    print('Building Laplacian matrix for file: {input}'.format(input=input))
    path = str(os.getcwd()) + "/examples/" + input
    laplacian = []
    with open(path + ".txt", "r") as f:
        rows = f.readlines()
        for i, row in enumerate(rows):
            new_row = []
            degree = 0
            for j in range(len(row)):
                if row[j] == '1' or row[j] == '0':
                    new_row.append(-int(row[j]))
                    degree += int(row[j])
            new_row[i] = degree
            laplacian.append(new_row)
        
    with open(path + "_laplacian.txt", "w") as output:
        for line in laplacian:
            output.write(" ".join([str(n) for n in line]) + "\n")
