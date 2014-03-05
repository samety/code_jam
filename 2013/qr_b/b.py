import sys
import itertools


def isPossible(lawn):
    products = itertools.product(lawn, zip(*lawn))
    elements = itertools.chain(*lawn)
    for element, (row, col) in zip(elements, products):
        if max(row) > element and max(col) > element:
            return False
    return True


if __name__ == '__main__':
    inFile = sys.stdin
    #inFile = open('B-small-practice.in')
    T = int(inFile.readline())
    for i in range(T):
        n, m = map(int, inFile.readline().strip().split(' '))
        lawn = []
        for j in range(n):
            line = map(int, inFile.readline().strip().split(' '))
            assert(len(line) == m)
            lawn.append(tuple(line))
        assert(len(lawn) == n)
        print 'Case #%s: %s' % (i+1, ('YES' if isPossible(tuple(lawn)) else 'NO'))
