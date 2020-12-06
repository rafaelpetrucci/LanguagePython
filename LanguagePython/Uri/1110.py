while True:
    n = int(input())
    if n == 0:
        break
    array = list(range(n, 0, -1))
    indiceF = len(array) - 1
    print("Discarded cards:", end=" ")
    while (indiceF + 1) != 1:
        print("{}".format(array[indiceF]), end="")
        if (indiceF + 1) > 2:
            print(",", end=" ")
        array.pop()
        indiceF -= 1
        array.insert(0, array[indiceF])
        array.pop()
    print("\nRemaining card: {}".format(array[0]))