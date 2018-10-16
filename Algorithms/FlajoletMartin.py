import MathTools as MT
import hashlib
import numpy as np
import math
import scipy.integrate as integrate


# Page 160 (142) book pdf

def run(bitArrays):
    print("Running Flajolet-Martin Algorithm using " + str(len(bitArrays)) + " arrays with " + str(
        len(bitArrays[0])) + " size bitarrays")

    maxTailLength = -1
    maxTailArray = None
    for i in range(0, len(bitArrays), 1):
        bitArray = bitArrays[i]
        tailLength = MT.TailCounter(bitArray, 0)

        if tailLength > maxTailLength:
            maxTailLength = tailLength
            maxTailArray = bitArray

    distinctElements = 2 ** maxTailLength

    print("Max tail length: " + str(maxTailLength))
    print("From array: " + str(maxTailArray))
    print("Distinct Elements: " + str(distinctElements))
    print("Flajolet-Martin Algorithm done")
    print()

    return distinctElements


def probabilisticCounting(binaries):
    # print("\t\tRunning Flajolet-Martin Algorithm using " + str(len(binaries)) + " stream elements")

    # length of the longest tail of 0’s
    maxTailLength = -1
    maxTailBinary = None
    for index, binary in enumerate(binaries):
        tailLength = len(binary) - len(binary.rstrip('0'))

        if tailLength > maxTailLength:
            maxTailLength = tailLength
            maxTailBinary = binary

    distinctElements = 2 ** maxTailLength

    '''print("\t\tMax tail length: "+str(maxTailLength))
    print("\t\tFrom element: "+str(maxTailBinary))
    print("\t\tDistinct Elements: "+str(distinctElements))
    print("\t\tFlajolet-Martin Algorithm done")
    print()'''

    return distinctElements

def trailingZeroes(binary):
    return len(binary) - len(binary.rstrip('0'))

def estimateCardinalityByLogLog(values, k=4):
    numBuckets = 2 ** k
    alpha = getAlpha(numBuckets)
    maxZeroes = [0] * numBuckets
    for value in values:
        hash = hashlib.md5(str(value).encode())
        hexadecimal = hash.hexdigest()
        asInt = int(hexadecimal, 16)
        binary = bin(asInt)[2:]
        bucket = int(binary[-k:], 2)  # Mask out the k least significant bits as bucket ID
        bucketBinary = binary[:-k]
        maxZeroes[bucket] = max(maxZeroes[bucket], trailingZeroes(bucketBinary))

    maxZeroes = np.trim_zeros(maxZeroes)
    meanTrailingZeros = (float(sum(maxZeroes)) / numBuckets)

    memory = calculateMemory(maxZeroes)

    estimate = 2 ** meanTrailingZeros * numBuckets * alpha
    return {"estimate": int(estimate), "memory": memory}


# memory in bits, Bytes and kiloBytes
def calculateMemory(maxZeroes):
    memory = sum(maxZero.bit_length() for maxZero in maxZeroes)

    print("\n\tRequired memory = " + str(memory) + " bits | " + str(memory / 8) + " Bytes | " + str(
        round(((memory / 8) / 1024), 4)) + " kB")
    return memory


def getAlpha(m):
    gamma = getGamma(-1 / m)
    alpha_m = (gamma * ((2 ** (-1 / m) - 1) / math.log(2))) ** -m
    print("\t" + str(alpha_m))
    return alpha_m


def getGamma(s):
    return (1 / s) * integrate.quad(lambda x: (math.e ** -x) * x ** s, 0, math.inf)[0]
