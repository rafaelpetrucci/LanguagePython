n = int(input())
lista = list()
positivo = negativo = 0
for i in range(n):
    nome = input().split(" ")
    if nome[0] == "+":
        positivo += 1
    elif nome[0] == "-":
        negativo += 1
    lista.append(nome[1])
lista.sort()
for i in range(len(lista)):
    print(lista[i])
print("Se comportaram: {} | Nao se comportaram: {}".format(positivo, negativo))