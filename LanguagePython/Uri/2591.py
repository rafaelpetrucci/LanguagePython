c = int(input())
for i in range(c):
    valida = somaH = somaK = 0

    k = input().replace("me", ',').replace('h', '').replace('k', '')
    for j in range(len(k)):
        if valida > 0:
            if k[j] == 'a':
                somaK += 1
        elif valida == 0:
            if k[j] == ',':
                valida += 1
            elif k[j] == 'a':
                somaH += 1
    somaH -= 1
    total = somaH * somaK + somaK
    print('k', end="")
    for j in range(total):
        print('a', end="")
    print()
