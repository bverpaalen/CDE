import numpy

def bitstring(size,amount):
    bitArrays = []
    for i in range(0,amount,1):
        nparray = numpy.random.randint(2,size=(size,))
        bitArrays.append(nparray)
    return bitArrays