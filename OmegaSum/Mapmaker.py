def zeroArray(len): #O(n^2)
    return [0 for i in range(len)]

def getSide(length, l):
    bar = zeroArray(length)
    max = min((length - l + 1), l)

    for i in range(max):
        bar[i] = i + 1
        bar[len(bar) - 1 - i] = i + 1

    for i in range(len(bar) - 2 * max):
        bar[i + max] = max
    return bar

def computeMap(verticalBars, horizontalBars):
        # initialize empty 2d array with correct dimensions
        map = []
        for i in range(len(verticalBars[0])):
            map.append(zeroArray(len(horizontalBars[0])))

        # set horizontal bar
        horizontalBar = zeroArray(len(horizontalBars[0]))
        for arr in horizontalBars:
            for i in range(len(arr)):
                horizontalBar[i] += arr[i]
        map[0] = horizontalBar

        # set vertical bar
        verticalBar = zeroArray(len(verticalBars[0]))
        for a in range(len(verticalBars)):
            for b in range(len(verticalBars[a])):
                verticalBar[b] += verticalBars[a][b]

        for i in range(len(verticalBar)):
            map[i][0] = verticalBar[i]

        # traverse and set values
        for r in range(len(map) - 1):
            for c in range(len(map[r]) - 1):

                for i in range(len(horizontalBars)):
                    map[r + 1][c + 1] += verticalBars[i][r + 1] * horizontalBars[i][c + 1]
        return map

class Mapmaker:
    def init(self):
        pass

    def compute(self, arr):
        L = min(len(arr), len(arr[0]))

        vertBars = []
        horzBars = []

        for i in range(L):
            vertBars.append(getSide(len(arr), i + 1))
            horzBars.append(getSide(len(arr[0]), i + 1))
        map = computeMap(vertBars, horzBars)

        sum = 0
        for r in range(len(vertBars[0])):
            for c in range(len(horzBars[0])):
                sum += arr[r][c] * map[r][c]

        return sum