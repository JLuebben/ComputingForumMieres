import time
import timeit
import threading


class FakeWorker(threading.Thread):
    def run(self):
        for _ in range(3):
            print('   - Doing some Work')
            time.sleep(1)


def processEvents():
    print('processing events.')


def mainFunction():
    for i in range(100):
        time.sleep(.1)
        processEvents()
        if not i % 10:
            FakeWorker().start()


if __name__ == '__main__':
    t = timeit.Timer(mainFunction)
    print(t.timeit(1))