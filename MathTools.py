import numpy as np

def TailCounter(bitArray, toCount):
    counter = 0
    for i in range(0,len(bitArray),1):
        if bitArray[i] == toCount:
            counter += 1
        else:
            counter = 0
    return counter

def HeadCounter(bitArray, toCount):
    return TailCounter(np.flip(bitArray), toCount)