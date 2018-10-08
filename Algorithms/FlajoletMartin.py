import MathTools as MT
import hashlib
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

def probabilisticCounting(binaries):
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


"""Counts the number of trailing 0 bits in binary."""
def trailingZeroes(binary):
    return len(binary) - len(binary.rstrip('0'))

"""Estimates the number of unique elements in the input set values.

  Arguments:
    values: An iterator of hashable elements to estimate the cardinality of.
    k: The number of bits of hash to use as a bucket number; there will be 2**k buckets.
  """
def estimateCardinalityByLogLog(values, k, alpha = 0.79402):
    numBuckets = 2 ** k
    maxZeroes = [0] * numBuckets
    for value in values:
        hash = hashlib.md5(str(value).encode())
        hexadecimal = hash.hexdigest()
        asInt = int(hexadecimal, 16)
        binary = bin(asInt)[2:]
        bucket = int(binary[-10:], 2) # Mask out the k least significant bits as bucket ID
        bucketBinary = binary[:-10]
        maxZeroes[bucket] = max(maxZeroes[bucket], trailingZeroes(bucketBinary))

    meanTrailingZeros = (float(sum(maxZeroes)) / numBuckets)
    estimate = 2 ** meanTrailingZeros * numBuckets * alpha
    return int(estimate)