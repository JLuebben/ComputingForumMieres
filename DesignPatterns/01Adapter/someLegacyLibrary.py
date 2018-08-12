
def checkFile(file):
    # do some checks.
    return file


def readBlock(fileHandle):
    block = fileHandle.read(10)
    # do some processing
    return block

if __name__ == '__main__':
    f = checkFile(open('dummy.txt', 'r'))
    while True:
        data = readBlock(f)
        if not data:
            break
        print(data)