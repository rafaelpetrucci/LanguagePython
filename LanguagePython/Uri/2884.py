import operator

n, m = map(int, input().split())
l = input().split()
array = [False] * m
arrayAux = [False] * m
l.pop(0)
inter = list()
contador = 0
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(len(l)):
    array[l[i] - 1] = not array[l[i] - 1]
copia = array.copy()
for i in range(n):
    aux = input().split()
    aux.pop(0)
    for i in range(len(aux)):
        aux[i] = int(aux[i])
    inter.append(aux.copy())

continua = True
while continua:
    for i in range(n):
        for k in range(len(inter[i])):
            array[inter[i][k] - 1] = not array[inter[i][k] - 1]
        contador += 1
        if operator.eq(arrayAux, array):
            continua = False
            break
    if operator.eq(array, copia):
        contador = -1
        continua = False
print(contador)