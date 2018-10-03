import sys
import numpy as np

import generator
import Parser as parser
from Algorithms import FlajoletMartin as FM

#Literatuur notes:
# n = stream size
# hx = hash function number x
# S = set
# m = key values

def main():
    hashes,size,arraysPerStream = parser.parseInput(sys.argv)

    distinctCounts = []

    for i in range(0,hashes,1):
        bitArrays = generator.bitstring(size,arraysPerStream)
        distinctCount = FM.run(bitArrays)
        distinctCounts.append(distinctCount)
    averageDC = sum(distinctCounts)/hashes
    medianDC = np.median(distinctCounts)

    print("Mean: "+str(averageDC))
    print("Median: "+str(medianDC))

main()
