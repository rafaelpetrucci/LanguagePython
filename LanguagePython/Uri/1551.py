alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total = len(alfabeto)
n = int(input())
for i in range(n):
    aux = alfabeto.copy()
    string = input().upper()
    for s in range(len(string)):
        if string[s] in aux:
            aux.remove(string[s])
    if len(aux) == 0:
        print("frase completa")
    elif (total/2) >= len(aux):
        print("frase quase completa")
    else:
        print("frase mal elaborada")
    aux.clear()