import random
import math
import time

from OmegaSum.Mapmaker import Mapmaker
from OmegaSum.CaseTester import CaseTester


def randArray(len):
    a = []
    for i in range(len):
        a.append(random.randint(0, 10))
    return a


def formatArr(arr):
    output = ''
    for i in range(len(arr)):
        output += f"{arr[i]}\n"
    return output


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def test(algorithm, num_cases):
    timer = CaseTester()
    initTime = time.time()

    for a in range(num_cases):
        arr = []
        for i in range(a + 1):
            arr.append(randArray(a + 1))

        timer.start((a + 1) * (a + 1))
        algorithm.compute(arr)
        timer.stop()

    print(f"Total time taken: {time.time() - initTime} seconds")
    timer.showTC()


mapmaker = Mapmaker()
print("Testing time complexity of Mapmaker.")
test(mapmaker, 100)
