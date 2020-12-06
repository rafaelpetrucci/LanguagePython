n = int(input())
sup = ['Q', 'J', 'K', 'A']
for i in range(n):
    palavra = input()
    aux = sup.copy()
    for j in palavra:
        if j in aux:
            aux.remove(j)
    if len(aux) == 0:
        print("Aaah muleke")
    else:
        print("Ooo raca viu")