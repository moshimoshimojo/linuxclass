#!/usr/bin/python3

import numpy as np
import argparse

parser = argparse.ArgumentParser(description= 'prints out nxn table')
parser.add_argument('--row' ,'-x' ,default=10)
parser.add_argument('--column' ,'-y' ,default=10)
args = parser.parse_args()


x = int(args.row)
y = int(args.column)

table = np.random.rand(x,y)

for i in range(x):
    for j in range(y):
        print("%.6f" %table[i][j], end="\t")
    print(end="\n")
