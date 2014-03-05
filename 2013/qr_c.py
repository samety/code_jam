import sys


def findFairSqNum(a, b):
    return 0


if __name__ == '__main__':
    sys.exit(0)
    inFile = sys.stdin
    T = int(inFile.readline())
    for i in range(T):
        a, b = map(int, inFile.readline().strip().split(' '))
        print "Case #%s: %s" % (i+1, findFairSqNum(a, b))
