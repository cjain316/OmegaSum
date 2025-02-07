import random
import math
import numpy as np
import time

from OmegaSum.Algorithm2 import Algorithm2
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

alg2 = Algorithm2()

test(alg2, 100)