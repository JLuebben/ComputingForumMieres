from adapter import Adapter
import alternativeLibrary
import networkInterface

def main(fileHandle, useLegacyLib=False):

    if useLegacyLib:
        print('using legacy library.')
        fileObject = Adapter(fileHandle)
    else:
        fileObject = alternativeLibrary.FileObject(fileHandle)
    for data in fileObject:
        print(data)

if __name__ == '__main__':
    fileHandle = networkInterface.NetworkFile('dummy.txt', serverAdress='127.0.0.1', port=8080)
    main(fileHandle, useLegacyLib=False)