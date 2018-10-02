def run(bitArrays):
    print("Running Flajolet-Martin Algorithm using " + str(len(bitArrays)) + " arrays with " + str(len(bitArrays[0])) + " size bitarrays")

    maxTailLength = -1
    maxTailArray = None
    for i in range(0,len(bitArrays),1):
        bitArray = bitArrays[i]
        tailLength = counter(bitArray,0)

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


def counter(bitArray,toCount):
    counter = 0
    for i in range(0,len(bitArray),1):
        if bitArray[i] == toCount:
            counter += 1
        else:
            counter = 0
    return counter