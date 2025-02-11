import random
import math
import time

from OmegaSum.ChatGPT import ChatGPT
from OmegaSum.Factorial import Factorial
from OmegaSum.Mapmaker import Mapmaker
from OmegaSum.CaseTester import CaseTester
from OmegaSum.ChatGPTO import ChatGPTO


def randArray(len):
    a = []
    for i in range(len):
        a.append(random.randint(0, 10))
    return a

def rand_2d_array(rows, columns):
    a = []
    for i in range(rows):
        a.append(randArray(columns))
    return a


def formatArr(arr):
    output = ''
    for i in range(len(arr)):
        output += f"{arr[i]}\n"
    return output


def test(algorithm, num_cases, name):
    timer = CaseTester(name)
    initTime = time.time()

    for a in range(num_cases):
        for b in range(num_cases):
            if ((a+1) * (b+1)) in timer.n:
                continue

            arr = []
            for i in range(a + 1):
                arr.append(randArray(b + 1))

            timer.start((a + 1) * (b + 1))
            algorithm.compute(arr)
            timer.stop()

    print(f"Total time taken: {time.time() - initTime} seconds")
    timer.sortData()
    timer.exportData()
    timer.showTC()

def compareTo(algorithm_base, algorithm_test):
    arr = []
    for i in range(10):
        arr.append(randArray(10))

    print("Testing comparison")
    val1 = algorithm_base.compute(arr)
    print(f"Base value {val1}")
    val2 = algorithm_test.compute(arr)
    print(f"Tested value {val2}")
    return val1 == val2

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

factorial = Factorial()
mapmaker = Mapmaker()
chatgpt = ChatGPT()
chatgpto = ChatGPTO()

test(mapmaker, 100, "Mapmaker")

exit()