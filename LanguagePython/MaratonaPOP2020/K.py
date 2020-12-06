n = int(input())
array = list(map(int, input().split()))
while len(array) != 1:
    if array[0] + array[1] == 0:
        array.pop(0)
        array = [0]
        break
    elif array[0] + array[1] > 0:
        array[1] = array[0] - array[1]
        array.pop(0)
    elif array[0] + array[1] < 0:
        array.pop(1)
print(array[0])