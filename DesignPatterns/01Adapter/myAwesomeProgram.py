from adapter import Adapter
import alternativeLibrary

def main(fileHandle, useLegacyLib=False):
    if useLegacyLib:
        print('using legacy library.')
        fileObject = Adapter(fileHandle)
    else:
        fileObject = alternativeLibrary.FileObject(fileHandle)
    for data in fileObject:
        print(data)

if __name__ == '__main__':
    fileHandle = open('dummy.txt', 'r')
    main(fileHandle, useLegacyLib=False)