# Generic linked list.
list()
myList = []
myList = [1, 2, 3]
myList = [1, 'a', ['x', 2, 3]]
myList.append(4)
myList.extend([1, 2, 3])
myList.pop()
myList.pop(0)
1 in myList
myList.append(5)
myList.remove(5)
del myList[-1]
myList[0]

myList[1:3]
myList[:-1]
myList[:]

# Immutable lists. Use for constants. Make understanding code easier.
tuple()
myTuple = (1, 2, 3)
1 in myTuple

# Unordered collections. Provide optimized set algebra.
set()
mySet = {1, 2, 3}
mySet2 = {2, 3, 4}
1 in mySet
mySet2.add(5)
mySet2.difference(5)

print(mySet.union(mySet2))
print(mySet.intersection(mySet2))
print(mySet.difference(mySet2))
print(mySet2.difference(mySet))

# The go-to Python container type. Very high performance even with many entries
dict()
myDict = {'age': 1,
          'name': 'John Doe',
          'favorite programming language': 'Python'}
myDict['age'] = 2
myDict['favorite city'] = 'mieres'
'age' in myDict
for key, value in myDict.items():
    print(key, value)

for key in myDict.keys():
    print(key, value)

listOfKeys = [1, 2, 3, 4, 5]
listOfValues = [1, 2, 3, 4, 5]
mySquares = {key: value ** 2 for key, value in zip(listOfKeys, listOfValues)}
