count = 0
value = int(input())
while count < 6:
    if value % 2 == 1:
        print(value)
        count += 1
    value += 1