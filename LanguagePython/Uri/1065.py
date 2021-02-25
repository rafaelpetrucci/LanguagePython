count = 0
for i in range(5):
    value = int(input())
    if value % 2 == 0:
        count += 1
print("{} valores pares".format(count))