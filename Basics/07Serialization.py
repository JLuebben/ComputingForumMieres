import pickle


class MyObject(object):
    def __init__(self, value):
        self.a = value
        self.b = self.a ** 2
        self.c = self.b ** 2
        self.d = self.c ** 2
        self.e = self.d ** 2

    def __call__(self):
        print(self.e)

def doSave():
    myInstance = MyObject(2)
    myInstance()
    with open('pickle.dat', 'wb') as fp:
        pickle.dump(myInstance, fp)

def doLoad():
    with open('pickle.dat', 'rb') as fp:
        myInstance = pickle.load(fp)
    myInstance()


if __name__ == '__main__':
    doSave()
    doLoad()

