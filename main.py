import sys
import generator
import parser

amount = 100

def main():
    size,amount = parser.parseInput(sys.argv)
    bitArrays = generator.bitstring(size,amount)
    print(bitArrays)

main()
