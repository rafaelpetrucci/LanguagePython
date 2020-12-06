n = int(input())
contador = 0
teste = []
for i in range(n):
    teste.append(input())
    if "0007" in teste[i]:
        contador = i + 1
print(contador)