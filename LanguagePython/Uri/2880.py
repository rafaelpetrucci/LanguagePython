palavra = input().strip()
crib = input().strip()
indice = len(palavra) - len(crib)
posicoes = 0

for i in range(indice + 1):
    igualdade = 0
    indiceP = i
    for k in range(len(crib)):
        numero = ord(palavra[indiceP])
        if numero < 65 or numero > 90:
            indiceP += 1
        if palavra[indiceP] == crib[k]:
            igualdade += 1
            break
        indiceP += 1
    if igualdade == 0:
        posicoes += 1
print(posicoes)