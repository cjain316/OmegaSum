import matplotlib.pyplot as plt
import time

class CaseTester:
    def __init__(self):
        self.n = []
        self.time = []

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