from networkInterface import Singleton


class Observable(object, metaclass=Singleton):
    _observers = {}
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        if self.name in self._observers:
            raise Exception('Observable with name {} already registered')
        self._observers[self.name] = []

        def wrappedFunc(newValue):
            for obs in self._observers[self.name]:
                obs.update(self.name, newValue)
            func(newValue)

        return wrappedFunc

    @staticmethod
    def registerObserver(name, obs):
        Observable._observers[name].append(obs)


class Observer(object):
    def update(self, name, value):
        print('Attribute {} is now'.format(name), value)


if __name__ == '__main__':

    @Observable('test')
    def test(v):
        pass
    obs = Observer()
    Observable.registerObserver('test', obs)

    test(1)
    test(2)
    test(3)
