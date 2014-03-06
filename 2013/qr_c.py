import sys
import math


def findFairSqNum(A, B):
    a = int(math.sqrt(A))
    b = int(math.sqrt(B))
    return a < b


if __name__ == '__main__':
    inFile = sys.stdin
    T = int(inFile.readline())
    for i in range(T):
        A, B = map(int, inFile.readline().strip().split(' '))
        print "Case #%s: %s" % (i+1, findFairSqNum(A, B))
