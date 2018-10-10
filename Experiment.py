def getSetup(names):

    n = 10**5
    lown = int(n/10)
    range = 10**5
    k =10
    
    setup = {}

    switcher = {
        "distinct": {"various numbers of distinct elements":
                         [[n, 100, k], [n, 200, k], [n, 500, k],[n, 1000, k], [n, 10000, k], [n, 20000, k], [n, 30000, k], [n, 40000, k], [n, 50000, k],
                           [n, 60000, k],[n, 70000, k], [n, 80000, k], [n, 90000, k]]},
        "buckets": {"number of buckets":
                        [[n, range, 1], [n, range, 2], [n, range, 3], [n, range, 4], [n, range, 5],
                         [range, 6], [n, range, 7], [n, range, 8], [n, range, 9],[range, k]]},
        "memory": {"required memory":
                       [[10**3, range, k], [lown, range, k], [lown*2, range, k], [lown*3, range, k], [lown*4, range, k], [lown*5, range, k], [lown*6, range, k],
                        [lown*7, range, k],[lown*8, range, k], [lown*9, range, k], [n,range, k], [lown*11,range, k], [lown*12,range, k]]}
    }

    for name in names:
        setup.update(switcher.get(name))

    return setup