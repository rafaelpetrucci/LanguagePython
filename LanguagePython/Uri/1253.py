alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ultimo = len(alfabeto) - 1
n = int(input())
lista = list()
for i in range(n):
    string = input()
    for s in string:
        lista.append(s)
    passo = int(input())
    for s in range(len(lista)):
        index = alfabeto.index(lista[s])
        soma = index - passo
        if soma < 0:
            soma = passo - (index + 1)
            soma = ultimo - soma
        lista[s] = alfabeto[soma]
    string = "".join(lista)
    print(string)
    lista.clear()