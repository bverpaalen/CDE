import sys
import generator
import Parser as parser
from Algorithms import FlajoletMartin as FM

def main():
    size,amount = parser.parseInput(sys.argv)
    bitArrays = generator.bitstring(size,amount)
    FM.run(bitArrays)

main()
