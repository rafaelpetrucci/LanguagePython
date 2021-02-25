number = int(input())
for i in range(number):
    value = list(map(int, input().split()))
    value.sort()
    total = 0
    for j in range(value[0] + 1, value[1]):
        if j % 2 == 1:
            total += j
    print(total)
