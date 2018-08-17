print('MAIN: Importing modules.')
import subModule
print('MAIN: Modules imported.')


def mainFunction():
    print('Executing mainFunction.')
    subModule.subFunction()



print('MAIN: Module fully loaded.')

# Problem
print('MAIN: Module fully loaded. Starting code execution.')
mainFunction()


# Solution 1
# if __name__ == '__main__':
#     print('MAIN: Starting code execution.')
#     mainFunction()

