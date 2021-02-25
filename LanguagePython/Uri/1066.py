count = [0]*4
for i in range(5):
    value = int(input())
    if value % 2 == 0:
        count[0] += 1
    else:
        count[1] += 1
    if value > 0:
        count[2] += 1
    elif value < 0:
        count[3] += 1
print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(count[0], count[1], count[2], count[3]))