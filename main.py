import sys
import numpy as np
import hashlib
import random

import generator
import Parser as parser
from Algorithms import FlajoletMartin as FM
import Experiment

#Literatuur notes:
# n = stream size
# hx = hash function number x
# S = set
# m = key values

ranges = [10**2,10**3,10**4,10**5,2*10**5,3*10**5,4*10**5,5*10**5,6*10**5,7*10**5,8*10**5,9*10**5,10**6]
results = {}
for j in range(len(ranges)):
    ranger = ranges[j]
    results.update({ranger:{}})
    for i in range(1,7):
        results[ranger].update({i:[]})

def main(runPc = True, runLogLog = True,ranger=10000):
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

    #print(hashlib.algorithms_available)
    if(runPc):
        experimentCounting(ranger)

    if (runLogLog):
        logLog()

def experimentCounting(ranger):
    #print("Probabilistic Counting")
    #print("\nTo use hash functions:")

    hashes = list(hashlib.algorithms_guaranteed)

    for element in hashes:
        if element.lower().startswith("shake_"):
            hashes.remove(element)


    #print(hashlib.algorithms_guaranteed)
    #print(hashes)

    setups = Experiment.getSetup(["distinct","hashes"])

    distincts = setups.get("various numbers of distinct elements")
    numHashes = setups.get("number of hashes")

    #for i in range(len(distincts)):
    #    distinct = distincts[i][0]
    #    calcCounting(distinct,3,hashes)

    for i in range(len(numHashes)):
        numHash = numHashes[i]
        calcCounting(ranger,numHash,hashes)


def calcCounting(distinct,numHash,hashes):
    hashGroups = generator.partitionIntoGroups(hashes, numHash)

    numbers = generator.generateRandomIntegers(10 ** 4, 0, distinct)
    trueCount = len(np.unique(numbers))

    # numbers = np.random.choice(numbers, 100000) # take sample
    groupAvgs = []

    #print("\nDistinct: " + str(distinct) + "\nNumber of hashes per group: " + str(numHash))

    for i, hashGroup in enumerate(hashGroups):
        #print("Hash group " + str(i + 1) + ": " + str(hashGroup))

        sumCounts = 0
        for hashName in hashGroup:
            #print("\t Running: " + hashName)
            hashFunction = getattr(hashlib, hashName)
            binaries = generator.getHashBinaries(numbers, hashFunction)
            distinctCount = FM.probabilisticCounting(binaries)
            sumCounts += distinctCount

        groupAvg = sumCounts / len(hashGroup)
        groupAvgs.append(groupAvg)

    #print("Distinct elements: " + str(trueCount))
    estimatedCount = np.median(groupAvgs)
    #print("Median of averages: " + str(estimatedCount))

    RAE = printError(trueCount, estimatedCount)

    results[distinct][numHash].append(RAE)

def logLog():
    print("#########################################################")
    print("::                       LogLog                        ::")
    print("#########################################################")
    distincts = []
    estimates = []
    setups = Experiment.getSetup(["distinct", "buckets", "memory"])
    #test = [(name, setup) for name, setup in setups.items() if setup[0] == True]
    for i, (name, setup) in enumerate(setups.items()):
        whiteSpace = " " * int(((38 - len(name)) / 2))
        print("\n=========================================================")
        print("|"+ whiteSpace + "Running setup: " + name + "..." + whiteSpace + "|")
        print("=========================================================")
        for j in range(len(setup)):
            numRange = setup[j][0]
            # number of bits to use as a bucket number
            buckets = setup[j][1]
            print("Iteration " + str(j+1))
            print("Number of bits to use as a BUCKET number: " + str(buckets) + " => " + str(2**buckets) + " buckets")
            numbers = generator.generateRandomIntegers(10**5, 0, numRange)
            distinct = len(np.unique(numbers))
            distincts.append(distinct)
            estimate = FM.estimateCardinalityByLogLog(numbers,buckets)
            estimates.append(estimate)
            print("\nActual distinct values: " + str(distinct))
            print("Estimated distinct values: " + str(estimate))
            printError(distinct, estimate)
            print("_________________________________________________________")
        print("\n")


def printError(trueCount, estimatedCount):
    # RAE = abs(true_count - estimated_count)/true_count
    RAE = abs(trueCount - estimatedCount) / trueCount
    #print("Relative Approximation Error: " + str(round(RAE,4)))
    return RAE

for ranger in ranges:
    for i in range(10):
        main(True,False,ranger)

for ranger in ranges:
    print(ranger)
    for i in range(1,len(results[ranger])+1):
        RAE = sum(results[ranger][i]) / len(results[ranger][i])
        print(str(RAE))
    print()