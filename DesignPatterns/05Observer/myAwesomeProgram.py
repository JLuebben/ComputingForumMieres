import factory


def main(fileHandle):

    for data in fileHandle:
        print(data)


if __name__ == '__main__':
    fileHandleFactory = factory.FileHandleFactory('config.txt')
    fileHandle = fileHandleFactory('dummy.txt')
    main(fileHandle)