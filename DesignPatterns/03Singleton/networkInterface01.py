class NetworkFile(object):
    def __init__(self, resourceName, serverAdress='localhost', port=8080):
        self._serverConnection = FakeServer(serverAdress, port)
        self._fileContent = self._serverConnection.httpGet(resourceName)

    def read(self, blockSize):
        data = self._fileContent[0:blockSize]
        self._fileContent = self._fileContent[blockSize:]
        if not data:
            raise StopIteration
        return data

    def __next__(self):
        splittedContent = self._fileContent.split('\n')
        data = splittedContent.pop(0)
        self._fileContent = '\n'.join(splittedContent)
        if not data:
            raise StopIteration
        return data+'\n'


class Singleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls in Singleton.instances:
            return Singleton.instances[cls]
        else:
            instance = type(cls, *args, **kwargs)
            Singleton.instances[cls] = instance
            return instance

class FakeServer(object, metaclass=Singleton):
    def __init__(self, address, port):
        pass
    def httpGet(self, resourceName):
        return open(resourceName, 'r').read()


