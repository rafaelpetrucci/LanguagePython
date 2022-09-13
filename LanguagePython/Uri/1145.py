valorXY = list(map(int, input().split()))
count = 0
for i in range(1, valorXY[1] + 1):
    print("{}".format(i), end='')
    count += 1
    if count < valorXY[0]:
        print(' ', end='')
    elif count >= valorXY[0]:
        count = 0
        print()
