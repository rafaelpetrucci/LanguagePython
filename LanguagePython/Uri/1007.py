array = list()
for i in range(4):
    array.append(int(input()))
array.append(array[0]*array[1] - array[2]*array[3])
print("DIFERENCA = {}".format(array[4]))