x = 2
y = 3

while x * y < 1000:
    print(x,y)
    x += 2 
    y += 2

i = 1

while True:
    print(i)
    i += 1
    if i == 10000:
        break


c = 1

while True:
    if c %2 == 0:
        c += 1
        continue
    print(c)
    c += 1
    if c == 1000:
        break
