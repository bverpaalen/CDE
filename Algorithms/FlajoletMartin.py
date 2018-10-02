def run(bitArrays):
    print("Running Flajolet-Martin Algorithm using " + str(len(bitArrays)) + " arrays with " + str(len(bitArrays[0])) + " size bitarrays")

    for i in range(0,len(bitArrays),1):
        bitArray = bitArrays[i]
        count = counter(bitArray,0)
        print(count)
def counter(bitArray,toCount):
    counter = 0
    for i in range(0,len(bitArray),1):
        if bitArray[i] == toCount:
            counter += 1
        else:
            counter = 0
    return counter