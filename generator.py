import numpy
import random

def bitstring(size,amount):
    bitArrays = []
    for i in range(0,amount,1):
        nparray = numpy.random.randint(2,size=(size,))
        bitArrays.append(nparray)
    return bitArrays

# generating a long sequence of random 32-bit long integers
# they will look like 32-bit long hashes of distinct objects)
def generateBitIntegers(amount, bit=32):
    print("\nGenerating " + str(bit) + " bit integers...")
    numbers = []
    for i in range(amount):
        # generate 32-bit integer
        number = random.getrandbits(bit)
        numbers.append(number)

    print("Number of distinct numbers: " + str(len(numpy.unique(numbers))))
    print()

    return numpy.array(numbers)

def generateRandomIntegers(size, startRange = 0, endRange=1000):
    print("\nGenerating random " + str(size) + " integers between " + str(startRange) + " and " + str(endRange) + "...")
    numpy.random.seed(123)
    return numpy.random.randint(startRange, endRange, size=size)

def getBinaries(numbers):
    binaries = []
    for index, number in enumerate(numbers):
        binary = bin(number)
        binaries.append(binary)

    return numpy.array(binaries)

def getHashBinaries(numbers, hashFunction):
    binaries = []
    for index, number in enumerate(numbers):
        hash = hashFunction(str(number).encode())
        hexadecimal = hash.hexdigest()
        asInt = int(hexadecimal, 16)
        binary = bin(asInt)[2:]
        #print(binary)
        binaries.append(binary)

    return numpy.array(binaries)

def partitionIntoGroups(hashFunctions, sampleSize = 2, combinations = 1):
    hashFunctions = sorted(list(hashFunctions))
    random.seed(123)
    random.shuffle(hashFunctions)

    hashGroups = []
    for i in range(combinations):
        random.seed(123)
        random.shuffle(hashFunctions)
        hashGroups += [hashFunctions[i:sampleSize + i] for i in range(0, len(hashFunctions), sampleSize)]

    return hashGroups
