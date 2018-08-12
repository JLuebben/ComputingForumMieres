import networkInterface
from adapter import Adapter
import alternativeLibrary

class FileHandleFactory(object):
    def __init__(self, confFileName):
        self._factoryFunction = self._openLocalFile
        self._serverName = 'None'
        self._useLegacy = False
        with open(confFileName,'r') as fp:
            for line in fp.readlines():
                if line.startswith('USE_LEGACY'):
                    self._useLegacy = int(line.split('=')[-1].strip())
                if line.startswith('SERVER_NAME'):
                    self._serverName = line.split('=')[-1].strip()
        if not self._serverName == 'None':
            self._factoryFunction = self._openRemoteFile

    def _openLocalFile(self, resourceName):
        print('FACTORY: using local file.')
        return open(resourceName, 'r')

    def _openRemoteFile(self, resourceName):
        print('FACTORY: using remote file.')
        return networkInterface.NetworkFile(resourceName, serverAdress=self._serverName, port=8080)

    def __call__(self, resourceName):
        handle = self._factoryFunction(resourceName)
        if self._useLegacy:
            print('using legacy library.')
            return Adapter(handle)
        else:
            return alternativeLibrary.FileObject(handle)
