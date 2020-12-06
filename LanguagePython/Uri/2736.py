n, m, y = input().strip().split()
contador = i = 1
while i < int(n):
    if contador == 3 or contador == 12 or contador == 13:
        i -= 1
    i += 1
    contador += 1
print("contador: {}".format(contador))