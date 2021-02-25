while True:
    sequence = list(map(int, input().split()))
    if 0 in sequence or sequence[0] < 0 or sequence[1] < 0:
        break
    sequence.sort()
    total = 0
    for i in range(sequence[0], sequence[1] + 1):
        print("{}".format(i), end=" ")
        total += i
    print("Sum={}".format(total))