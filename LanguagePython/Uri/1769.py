while True:
    try:
        n = input().replace(".", "").replace("-", "")
        total = 0
        contador = 1
        for i in range(len(n) - 2):
            total += (int(n[i]) * contador)
            contador += 1
        resto1 = total % 11
        if resto1 == 10:
            resto1 = 0
        if resto1 == int(n[9]):
            total = 0
            contador = 9
            for i in range(len(n) - 2):
                total += (int(n[i]) * contador)
                contador -= 1
            resto2 = total % 11
            if resto2 == 10:
                resto2 = 0
            if resto2 == int(n[10]):
                print("CPF valido")
            else:
                print("CPF invalido")
        else:
            print("CPF invalido")
    except EOFError:
        break
