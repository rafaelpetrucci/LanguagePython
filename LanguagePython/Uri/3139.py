numeroA, minimo = input().split(" ")
numeroA = int(numeroA)
minimo = int(minimo)
dias = input().split(" ")
contador = soma = 0
for i in range(len(dias)):
    dias[i] = int(dias[i])
print(dias)
while numeroA < minimo:
    total = sum(dias)
    total = total / 30
    total = int(round(total, 0))
    dias.pop(0)
    dias.append(total)
    numeroA += total
    soma += total
    contador += 1
print(soma)
print(contador)
