import sys
import generator

amount = 100

def main():
    size = parseInput(sys.argv)
    bitArrays = generator.bitstring(size,amount)
    print(bitArrays)

def parseInput(argv):
    if (len(argv) > 1):
        try:
            return int(argv[1])
        except ValueError:
            print("First input isn't int")
            print("Given input: "+str(argv[1]))
    return 32
main()
