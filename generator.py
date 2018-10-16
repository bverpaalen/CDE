import numpy
import random

genCounter = 1

def bitstring(size,amount):
    bitArrays = []
    for i in range(0,amount,1):
        nparray = numpy.random.randint(2,size=(size,))
        bitArrays.append(nparray)
    return bitArrays

# generating a long sequence of random 32-bit long integers
# they will look like 32-bit long hashes of distinct objects)
def generateRandomBitIntegers(size, numDistincts, bit=32):
    global genCounter
    random.seed(123 * genCounter)
    genCounter += 1

    print("\n\tGenerating " + str(size) + " of " + str(bit) + " bit random integers with " + str(numDistincts) + " dinstincts...")
    distincts = random.sample(range(1, 2**bit), numDistincts)
    numbers = distincts[:]
    replications = size - len(numbers)
    if replications > 0:
        numbers = numbers + [random.choice(distincts) for i in range(replications)]

    random.shuffle(numbers)
    return numpy.array(numbers)

def generateRandomIntegers(size, startRange = 0, endRange=1000, printInfo = False):
    if printInfo: print("\n\tGenerating random " + str(size) + " integers between " + str(startRange) + " and " + str(endRange) + "...")
    global genCounter
    numpy.random.seed(123 * genCounter)
    genCounter += 1
    return numpy.random.randint(startRange, endRange, size=size)

def getBinaries(numbers):
    binaries = []
    for index, number in enumerate(numbers):
        binary = bin(number)
        binaries.append(binary)

    return numpy.array(binaries)

def getHashBinaries(numbers, hashFunction):
    binaries = []
    #print(numbers)
    for index, number in enumerate(numbers):
        hash = hashFunction(str(number).encode())
        hexadecimal = hash.hexdigest()
        asInt = int(hexadecimal, 16)
        binary = bin(asInt)[2:]
        #print(binary)
        binaries.append(binary)

    return numpy.array(binaries)

def partitionIntoGroups(hashFunctions, sampleSize = 2, combinations = 1):
    global genCounter
    hashFunctions = sorted(list(hashFunctions))
    random.seed(123* genCounter)
    genCounter += 1
    random.shuffle(hashFunctions)

    hashGroups = []
    for i in range(combinations):
        random.seed(123)
        random.shuffle(hashFunctions)
        hashGroups += [hashFunctions[i:sampleSize + i] for i in range(0, len(hashFunctions), sampleSize)]

    return hashGroups

def resetGenCounter():
    global genCounter
    genCounter = 1
