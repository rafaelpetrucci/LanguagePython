valor = input().split()
resultado = maximo = mes = 0
if valor[0] == "sab":
    print("sab {} {}".format(int(valor[1]), int(valor[2])))
elif valor[0] == "dom":
    print("dom {} {}".format(int(valor[1]), int(valor[2])))
else:
    if valor[0] == "seg":
        resultado = 6 - 1
    elif valor[0] == "ter":
        resultado = 6 - 2
    elif valor[0] == "qua":
        resultado = 6 - 3
    elif valor[0] == "qui":
        resultado = 6 - 4
    elif valor[0] == "sex":
        resultado = 6 - 5
    if int(valor[2]) == 1 or int(valor[2]) == 3 or int(valor[2]) == 5 or int(valor[2]) == 7 or int(valor[2]) == 8 or int(valor[2]) == 10 or int(valor[2]) == 12:
        maximo = 31
    elif int(valor[2]) == 2:
        maximo = 28
    else:
        maximo = 30
    soma = int(valor[1]) + resultado
    if soma > maximo:
        soma -= maximo
        mes = int(valor[2]) + 1
    else:
        mes = int(valor[2])
    if mes > 12:
        mes = 1
    print("sab {} {}".format(soma, mes))