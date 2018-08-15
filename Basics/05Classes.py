
class MyClass(object):
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def foobar(self):
        return self.foo * self.bar


myInstance = MyClass(2, 'a')
print(myInstance.foo)
print(myInstance.bar)
print(myInstance.foobar())













class MyOtherclass(MyClass):
    def foobar(self):
        return self.foo **2 * self.bar

myOtherInstance = MyOtherclass(2, 'a')
print(myOtherInstance.foobar())



