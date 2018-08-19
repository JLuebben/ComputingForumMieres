
l = []
for i in range(5):
    l.append(lambda: i**2)
for f in l:
    print(f())