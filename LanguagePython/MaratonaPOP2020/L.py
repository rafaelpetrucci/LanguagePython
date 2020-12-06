a1, a2 = map(int, input().split())
lista1 = list()
lista2 = list()
for i in range(a1):
    aux = list(map(int, input().split()))
    lista1.append(aux.copy())

b1, b2 = map(int, input().split())
for i in range(b1):
    aux = list(map(int, input().split()))
    lista2.append(aux.copy())

if a2 == b1:
    aux = [0] * b2
    lista3 = [a1][b2]
    print(lista3)
    for m in range(b2):
        for i in range(a1):
            soma = 0
            aux = []
            for j in range(b1):
                resultado = lista1[i][j] * lista2[j][m]
                soma += resultado
            aux.append(soma)
else:
    print("IMPOSSIVEL MULTIPLICAR")
