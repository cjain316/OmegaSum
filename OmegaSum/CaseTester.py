import matplotlib.pyplot as plt
import time

class CaseTester:
    def __init__(self, function_name):
        self.n = []
        self.time = []
        self.name = function_name

    def start(self, num):
        self.start_time = time.time()*1000
        self.n.append(num)

    def stop(self):
        self.time.append(time.time()*1000-self.start_time)

    def showTC(self):
        plt.subplot(2, 1, 2)
        plt.plot(self.n, self.time, linestyle='-', color='b')
        plt.title("Time Complexity of function")
        plt.xlabel("Num elements (rows*columns)")
        plt.ylabel("Time to run (ms)")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def exportData(self):
        filename = f"data/{self.name}/{self.name} {len(self.n)} cases.csv"
        csv = open(filename, "w")
        csv.write(f"N,Time (ms)\n")
        for i in range(len(self.n)):
            csv.write(f"{self.n[i]},{self.time[i]}\n")
        csv.close()


    def sortData(self):
        quickSort(self.n, self.time, 0, len(self.n) - 1)

# Function to find the partition position
def partition(array, parallel, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            (parallel[i], parallel[i]) = (parallel[j], parallel[j])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    (parallel[i + 1], parallel[high]) = (parallel[high], parallel[i + 1])
    return i + 1

def quickSort(array, parallel, low, high):
    if low < high:
        pi = partition(array, parallel, low, high)
        quickSort(array, parallel, low, pi - 1)
        quickSort(array, parallel, pi + 1, high)