import MathTools as MT
import numpy as np
#Page 160 (142) book pdf

def run(bitArrays):
    print("Running Flajolet-Martin Algorithm using " + str(len(bitArrays)) + " arrays with " + str(len(bitArrays[0])) + " size bitarrays")

    maxTailLength = -1
    maxTailArray = None
    for i in range(0,len(bitArrays),1):
        bitArray = bitArrays[i]
        tailLength = MT.TailCounter(bitArray, 0)

        if tailLength > maxTailLength:
            maxTailLength = tailLength
            maxTailArray = bitArray

    distinctElements = 2**maxTailLength

    print("Max tail length: "+str(maxTailLength))
    print("From array: "+str(maxTailArray))
    print("Distinct Elements: "+str(distinctElements))
    print("Flajolet-Martin Algorithm done")
    print()

    return distinctElements

def ProbabilisticCounting(binaries):
    print("\t\tRunning Flajolet-Martin Algorithm using " + str(len(binaries)) + " stream elements")

    # length of the longest tail of 0’s
    maxTailLength = -1
    maxTailBinary = None
    for index, binary in enumerate(binaries):
        tailLength = len(binary) - len(binary.rstrip('0'))

        if tailLength > maxTailLength:
            maxTailLength = tailLength
            maxTailBinary = binary

    distinctElements = 2**maxTailLength

    print("\t\tMax tail length: "+str(maxTailLength))
    print("\t\tFrom element: "+str(maxTailBinary))
    print("\t\tDistinct Elements: "+str(distinctElements))
    print("\t\tFlajolet-Martin Algorithm done")
    print()

    return distinctElements