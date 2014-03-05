import sys


class State(object):
    X_won = 'X won'
    O_won = 'O won'
    NotComplete = 'Game has not completed'
    Draw = 'Draw'

    def __init__(self, txtState):
        self.txtState = txtState

    def getResult(self):
        txtState1 = [s.replace('T', 'X') for s in self.txtState]
        result1 = self.getWinner(txtState1)
        txtState2 = [s.replace('T', 'O') for s in self.txtState]
        result2 = self.getWinner(txtState2)
        assert(result1 is None or result2 is None or result1 == result2)
        if result1:
            result = result1
        elif result2:
            result = result2
        else:
            result = None
        if result is None and self.isFinished():
            result = State.Draw
        if result is None:
            result = State.NotComplete
        return result

    def isFinished(self):
        for s in self.txtState:
            if '.' in s:
                return False
        return True

    def getWinner(self, initState):
        result = None
        fullState = initState + [''.join(t) for t in zip(*initState)] + self.getDiagonal(initState)
        for s in fullState:
            if 'XXXX' == s:
                assert(result is None or result == State.X_won)
                result = State.X_won
            elif 'OOOO' == s:
                assert(result is None or result == State.O_won)
                result = State.O_won
        return result

    def getDiagonal(self, initState):
        return [''.join([initState[i][i] for i in (0, 1, 2, 3)]),
                ''.join([initState[i][3-i] for i in (0, 1, 2, 3)])]


if __name__ == '__main__':
    aState = []
    states = []

    n = int(sys.stdin.readline())

    for line in sys.stdin:
        line = line.strip()
        if line:
            assert(len(line) == 4)
            aState.append(line)
        else:
            states.append(State(aState))
            aState = []

    assert(n == len(states))

    for i, s in enumerate(states):
        txtResult = s.getResult()
        sys.stdout.write("Case #%s: %s\n" % (i+1, txtResult))
