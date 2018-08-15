def myFunction(value, cache=None):
    if not cache:
        cache = []
    cache.append(value)
    print(cache)

myFunction(value=1)
myFunction(value=2)

