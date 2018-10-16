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
    print("################################################################")
    print("::                          LogLog                            ::")
    print("################################################################")
    setups = Experiment.getSetup(["distinct"])
    #test = [(name, setup) for name, setup in setups.items() if setup[0] == True]
    for i, (name, setup) in enumerate(setups.items()):
        whiteSpace = " " * int(((44 - len(name)) / 2))
        print("\n================================================================")
        print("|"+ whiteSpace + "Running setup: " + name + "..." + whiteSpace + " |")
        print("================================================================")
        for j in range(len(setup)):
            print("EXPERIMENT " + str(j + 1) + "\n")
            sumError = 0
            sumMemory = 0
            distincts = []
            estimates = []
            for l in range(10):
                numDistincts = setup[j][1]
                # number of bits to use as a bucket number
                buckets = setup[j][2]
                print("\tIteration " + str(l+1))
                print("\tNumber of bits to use as a BUCKET number: " + str(buckets) + " => " + str(2**buckets) + " buckets")
                n = setup[j][0]
                #numbers = generator.generateRandomIntegers(n, 0, numRange, True)
                numbers = generator.generateRandomBitIntegers(n, numDistincts)
                distinct = len(np.unique(numbers))
                distincts.append(distinct)
                result = FM.estimateCardinalityByLogLog(numbers,buckets)
                estimate = result.get("estimate")
                sumMemory += result.get("memory")
                estimates.append(estimate)
                print("\n\tActual distinct values: " + str(distinct))
                print("\tEstimated distinct values: " + str(estimate))
                sumError += printError(distinct, estimate, True)
                print("________________________________________________________________")

            printReport(sumError, sumMemory, distincts, estimates, 10)
            generator.resetGenCounter()
            print("________________________________________________________________\n")

def printError(trueCount, estimatedCount, printInfo = False):
    # RAE = abs(true_count - estimated_count)/true_count
    RAE = abs(trueCount - estimatedCount) / trueCount
    if printInfo:
        print("\tRelative Approximation Error: " + str(round(RAE,4)))
    return RAE

def printReport(sumError, sumMemory, distincts, estimates, length):
    print("Mean Actual distinct values: " + str(int(round(np.mean(distincts)))))
    print("Mean Estimated distinct values: " + str(int(round(np.mean(estimates)))))
    meanError = sumError / length
    meanMemory = sumMemory / length
    print("Mean Relative Approximation Error: " + str(round(meanError,4)))
    print("Mean Memory Usage: " + str(meanMemory) + " bits | " + str(meanMemory / 8) + " Bytes | " + str(
        round(((meanMemory / 8) / 1024), 4)) + " kB")

'''for ranger in ranges:
    for i in range(10):
        main(True,False,ranger)

for ranger in ranges:
    print(ranger)
    for i in range(1,len(results[ranger])+1):
        RAE = sum(results[ranger][i]) / len(results[ranger][i])
        print(str(RAE))
    print()'''

main(False,True,None)