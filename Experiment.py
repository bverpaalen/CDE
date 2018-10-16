def getSetup(names):

    n = 10**5
    lown = int(n/10)
    range = 10**5
    k =10
    distincts = 80000
    distProp = 0.8

    setup = {}

    switcher = {
        "distinct": {"various numbers of distinct elements":
                         [[n, 100, 5], [n, 200, 6], [n, 500, 7],[n, 1000, 8], [n, 10000, k], [n, 20000, k], [n, 30000, k], [n, 40000, k], [n, 50000, k],
                           [n, 60000, k],[n, 70000, k], [n, 80000, k], [n, 90000, k]]},
        "buckets": {"number of buckets":
                        [[n, distincts, 1], [n, distincts, 2], [n, distincts, 3], [n, distincts, 4], [n, distincts, 5],
                         [n, distincts, 6], [n, distincts, 7], [n, distincts, 8], [n, distincts, 9],[n, distincts, k]]},
        "memory": {"required memory":
                       [[10**3, int(10**3*distProp), k], [lown, int(lown*distProp), k], [lown*2, int(lown*2**distProp), k], [lown*3, int(lown*3*distProp), k], [lown*4, int(lown*4*distProp), k], [lown*5, int(lown*5*distProp), k], [lown*6, int(lown*6*distProp), k],
                        [lown*7, int(lown*7*distProp), k],[lown*8, int(lown*8*distProp), k], [lown*9, int(lown*9*distProp), k], [n, int(n*distProp), k], [lown*11, int(lown*11*distProp), k], [lown*12, int(lown*12*distProp), k]]},
        "hashes": {"number of hashes": [1, 2, 3, 4, 5, 6]}
    }

    for name in names:
        setup.update(switcher.get(name))

    return setup