def myFunction(value, cache=[]):
    cache.append(value)
    print(cache)

myFunction(value=1)
myFunction(value=2)



def fibunacci(nth, cache=[1,1]):
    if len(cache) >= nth:
        return cache[nth-1]
    cache.append(sum(cache[-2:]))
    return fibunacci(nth)

print(fibunacci(20))


