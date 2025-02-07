class Factorial:
    def init(self):
        pass

    def compute(self, nums):
        o = 0
        width = len(nums[0])
        height = len(nums)

        for wSub in range(1, min(width+1, height+1)):
            for r in range(height - wSub + 1):
                for c in range(width - wSub + 1):
                    o += sumArray(getSub(nums, r, c, wSub))

        return o


def getSub(whole, sr, sc, lSide):
    output = [[0] * lSide for i in range(lSide)]

    for r in range(sr, sr + lSide):
        for c in range(sc, sc + lSide):
            output[r - sr][c - sc] = whole[r][c]

    return output


def sumArray(nums):
    count = 0
    for r in range(len(nums)):
        for c in range(len(nums[r])):
            count += nums[r][c]
    return count


def zeroArray(len):
    a = []
    for i in range(len):
        a.append(0)
    return a
