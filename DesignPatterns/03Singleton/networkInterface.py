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


_SERVER = None


def FakeServer(adress, port):
    global _SERVER
    if not _SERVER:
        _SERVER = _FakeServer(adress, port)
    return _SERVER


class _FakeServer(object):
    def __init__(self, address, port):
        pass

    def httpGet(self, resourceName):
        return open(resourceName, 'r').read()


if __name__ == '__main__':
    srvr1 = FakeServer('localhost', 8080)
    srvr2 = FakeServer('localhost', 8080)
    print('Names point to the same instace? ', srvr1 is srvr2)


