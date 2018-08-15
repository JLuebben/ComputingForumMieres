import json

class MyObject(object):
    def __init__(self, value):
        self.a = value
        self.b = self.a ** 2
        self.c = self.b ** 2
        self.d = self.c ** 2
        self.e = self.d ** 2

    def __call__(self):
        print(self.e)

    def serialize(self):
        return json.dumps({'a': self.a})

    def save(self, fileName):
        with open(fileName, 'w') as fp:
            fp.write(self.serialize())

    @classmethod
    def load(cls, fileName):
        with open(fileName, 'r') as fp:
            data = json.loads(fp.read())
        return cls(data['a'])

def doSave():
    myInstance = MyObject(2)
    myInstance()
    myInstance.save('myInstance.dat')

def doLoad():
    myInstance = MyObject.load('myInstance.dat')
    myInstance()


if __name__ == '__main__':
    doSave()
    doLoad()

