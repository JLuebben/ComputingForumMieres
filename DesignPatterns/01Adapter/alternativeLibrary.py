

class FileObject(object):

    def __init__(self, file):
        # do some checking
        self._file = file

    def __iter__(self):
        while True:
            line = next(self._file)
            # process line
            yield line


if __name__ == '__main__':
    f = FileObject(open('dummy.txt', 'r'))
    for data in f:
        print(data)
