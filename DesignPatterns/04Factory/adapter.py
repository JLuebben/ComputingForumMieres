import someLegacyLibrary

class Adapter(object):
    def __init__(self, file):
        self._file = someLegacyLibrary.checkFile(file)

    def __iter__(self):
        while True:
            data = someLegacyLibrary.readBlock(self._file)
            if not data:
                break
            yield data