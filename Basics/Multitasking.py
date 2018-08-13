import time


def fakeWorkFunction(callback):
    for _ in range(3):
        print('   - Doing some Work')
        time.sleep(1)
        callback()


def processEvents():
    print('processing events.')


def mainFunction():
    for i in range(100):
        time.sleep(.1)
        processEvents()
        if not i % 10:
            fakeWorkFunction(processEvents)


if __name__ == '__main__':
    mainFunction()