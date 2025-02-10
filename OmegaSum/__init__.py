import random
import math
import time

from OmegaSum.ChatGPT import ChatGPT
from OmegaSum.Factorial import Factorial
from OmegaSum.Mapmaker import Mapmaker
from OmegaSum.CaseTester import CaseTester


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
    #timer.showTC()


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

factorial = Factorial()
mapmaker = Mapmaker()
chatgpt = ChatGPT()


for i in range(44,50):
    print(f"Testing chatgpt range {i + 1}")
    test(chatgpt, i+1, "ChatGPT")

print("Done")
exit()