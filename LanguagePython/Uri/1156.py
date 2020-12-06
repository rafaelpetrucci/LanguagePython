S = 1
a = 3
b = 2
while True:
    S += a/b
    if a == 39:
        break
    a += 2
    b *= 2
print('{:.2f}'.format(S))