n = int(input())
for i in range(n):
    string = input()
    lista = list()
    for s in range(len(string)):
        if string[s].isalpha():
            numero = ord(string[s]) + 3
            lista.append(chr(numero))
        else:
            lista.append(string[s])
    lista.reverse()
    total = len(lista)
    for s in range(total//2, total):
        numero = ord(lista[s]) - 1
        lista[s] = chr(numero)
    string = "".join(lista)
    print(string)