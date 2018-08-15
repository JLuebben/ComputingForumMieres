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


class MyContainer(object):
    def __init__(self, values):
        self.objects = [MyObject(value) for value in values]

    def __call__(self):
        for obj in self.objects:
            obj()

    def serialize(self):
        return json.dumps([obj.serialize() for obj in self.objects])

    def save(self, fileName):
        with open(fileName, 'w') as fp:
            fp.write(self.serialize())

    @classmethod
    def load(cls, fileName):
        with open(fileName, 'r') as fp:
            data = json.loads(fp.read())
            data = [json.loads(datum) for datum in data]
        return cls([datum['a'] for datum in data])


def doSave():
    myContainerInstance = MyContainer((1,2,3,4))
    myContainerInstance.save('myContainerInstance.dat')

def doLoad():
    myContainerInstance = MyContainer.load('myContainerInstance.dat')
    myContainerInstance()


if __name__ == '__main__':
    doSave()
    doLoad()

