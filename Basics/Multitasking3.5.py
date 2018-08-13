import time
import threading
import timeit

def timeConsumingFunction():
    # return [a**b for a,b in zip(list(range(2000)), list(range(2000)))]
    time.sleep(.5)


class FakeWorker(threading.Thread):
    def run(self):
        for _ in range(3):
            print('   - Doing some Work')
            a = timeConsumingFunction()


def processEvents():
    print('processing events.')

def mainFunction():
    for i in range(10):
        a = timeConsumingFunction()
        processEvents()
        if not i % 2:
            FakeWorker().start()

def sequentialMainFunction():
    for i in range(10):
        a = timeConsumingFunction()
    for i in range(15):
        a = timeConsumingFunction()



if __name__ == '__main__':
    t = timeit.Timer(mainFunction)
    print(t.timeit(1))

    t1 = t.timeit(1)
    t = timeit.Timer(sequentialMainFunction)
    t2 = t.timeit(1)
    print('Parallel execution:   {:4.2f}\nSequential execution: {:4.2f}'.format(t1, t2))
