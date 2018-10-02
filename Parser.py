def parseInput(argv):
    argvLen = len(argv)

    if(argvLen == 2):
        try:
            return int(argv[1]),32,100
        except ValueError:
            print("First input isn't int")
            print("Given input: "+str(argv[1]))
    elif (argvLen == 3):
        try:
            return int(argv[1]),int(argv[2]),100
        except ValueError:
            print("First or second input isn't int")
            print("Given input: "+str(argv[1])+" and "+str(argv[2]))
    elif (argvLen > 3):
        try:
            return int(argv[1]),int(argv[2]),int(argv[3])
        except ValueError:
            print("First,second or third input isn't int")
            print("Given input: "+str(argv[1])+","+str(argv[2])+" and "+str(argv[3]))
    print("Using default 10 streams,32 bit and 100 arrays")
    return 10,32,100