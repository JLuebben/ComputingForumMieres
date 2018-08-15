fileHandle = open('myFile.txt', 'w')
for i in range(10):
    fileHandle.write('I:   {:4.2f}\n'.format(i))
fileHandle.close()

fileHandle = open('myFile.txt', 'r')
for line in fileHandle.readlines():
    # line = line.strip()
    # line = line.split()
    print(line)
    # value = float(line[1])
    # print(value)
fileHandle.close()