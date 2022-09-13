dicionario = {1: 0, 2: 0, 3: 0}
while True:
    value = int(input())
    if 1 <= value <= 4:
        if value == 4:
            break
        dicionario[value] += 1
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(dicionario[1], dicionario[2], dicionario[3]))