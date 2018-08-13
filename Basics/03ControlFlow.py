# Decision making
def oddOrEven(i):
    if i % 2:
        print(i, 'is odd')
    else:
        print(i, 'is even')

oddOrEven(1)
oddOrEven(2)
oddOrEven(3)


def oddOrEvenAndNotZero(i):
    if i % 2:
        print(i, 'is odd')
    elif i is 0:
        print(i, 'is zero')
    else:
        print(i, 'is even')

# Ternary operator
i=2
print('odd' if i % 2 else 'even')


# Boolean algebra
print(True and True)
print(True and False)
print(True or False)
print(False or False)

print((True or False) or (False and False))

print(0 < 1 < 2)

# looping
for i in range(10):
    oddOrEven(i)

# Don't do this in Python. This is ugly.
i = 0
while i < 10:
    oddOrEven(i)
    i += 1

# The only 'good' reason to use 'while' statements is in a case like this:
veryRareCondition = True
while True:
    # loop endlessly until something very rare or very special happens.
    if veryRareCondition is True:
        break

# Controlling loops
for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    oddOrEven(i)


# Implicit loops
a = [i%2 for i in range(10)]
print(a)

a = [i%2 for i in range(10) if i > 5]
print(a)

a = [i%2 if i > 5 else None for i in range(10)]
print(a)