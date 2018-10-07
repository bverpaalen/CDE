import sys
import numpy as np
import hashlib
import random

import generator
import Parser as parser
from Algorithms import FlajoletMartin as FM

#Literatuur notes:
# n = stream size
# hx = hash function number x
# S = set
# m = key values

def main():
    ''''hashes, size, arraysPerStream = parser.parseInput(sys.argv)

    distinctCounts = []

    for i in range(0, hashes, 1):
        bitArrays = generator.bitstring(size, 100)
        distinctCount = FM.run(bitArrays)
        distinctCounts.append(distinctCount)
    averageDC = sum(distinctCounts) / hashes
    medianDC = np.median(distinctCounts)

    print("Mean: " + str(averageDC))
    print("Median: " + str(medianDC))'''

    print(hashlib.algorithms_guaranteed)
    print(hashlib.algorithms_available)

    hashGroups = generator.partitionIntoGroups(hashlib.algorithms_guaranteed)

    numbers = generator.generateRandomIntegers(100000)
    trueCount = len(np.unique(numbers))

    #numbers = np.random.choice(numbers, 100000) # take sample
    groupAvgs = []
    for i, hashGroup in enumerate(hashGroups):
        print("Hash group " + str(i + 1) + ": " + str(hashGroup))

        sumCounts = 0
        for hashName in hashGroup:
            print("\t Running: " + hashName)
            hashFunction = getattr(hashlib, hashName)
            binaries = generator.getHashBinaries(numbers, hashFunction)
            distinctCount = FM.ProbabilisticCounting(binaries)
            sumCounts += distinctCount

        groupAvg = sumCounts / len(hashGroup)
        groupAvgs.append(groupAvg)

    print("Distinct elements: " + str(trueCount))
    estimatedCount = np.median(groupAvgs)
    print("Median of averages: " + str(estimatedCount))

    # RAE = abs(true_count - estimated_count)/true_count
    RAE = abs(trueCount - estimatedCount) / trueCount
    print("Relative Approximation Error: " + str(RAE))

main()
