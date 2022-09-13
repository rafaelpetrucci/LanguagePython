valorX = int(input())
valorY = int(input())
lista = [valorX, valorY]
lista.sort()
for i in range(lista[0] + 1, lista[1]):
    resto = i % 5
    if resto == 2 or resto == 3:
        print(i)