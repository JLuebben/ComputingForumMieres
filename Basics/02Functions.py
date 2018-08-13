
# Defining a function
def myFunction():
    print('Function doing stuff')


myFunction()


# Defining a function with arguments
def myFunctionWithArguments(arg1, arg2, arg3=3):
    return arg1 + arg2 + arg3

print(myFunctionWithArguments(1, 2))
print(myFunctionWithArguments(1, 2, 4))
print(myFunctionWithArguments(1, 2, arg3=4))
print(myFunctionWithArguments(arg2=2, arg3=4, arg1=1))


# Python functions are first class objects
myVariableHoldingAFunction = myFunctionWithArguments
myVariableHoldingAFunction(1, 2, 3)