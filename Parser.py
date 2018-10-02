def parseInput(argv):
    if (len(argv) > 1):
        try:
            return int(argv[1]),100
        except ValueError:
            print("First input isn't int")
            print("Given input: "+str(argv[1]))
    elif (len(argv) > 2):
        try:
            return int(argv[1]),int(argv[2])
        except ValueError:
            print("First or second input isn't int")
            print("Given input: "+str(argv[1])+" and "+str(argv[2]))
    print("Using default 32 bit,100 arrays")
    return 32,100