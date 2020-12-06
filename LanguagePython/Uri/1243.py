while True:
    numeros = list()
    testando = list()
    try:
        string = input().split(" ")
        for i in range(len(string)):
            if i == len(string) - 1:
                aux = string[i]
                if aux[len(aux) - 1] == '.':
                    for teste in range(len(aux) - 1):
                        testando.append(aux[teste])
                    string[i] = "".join(testando)
            if string[i].isalpha():
                numeros.append(len(string[i]))
        if len(numeros) == 0:
            media = 0
        else:
            media = sum(numeros) // len(numeros)
        if media <= 3:
            print("250")
        elif media <= 5:
            print("500")
        elif media >= 6:
            print("1000")
        testando.clear()
        numeros.clear()
    except EOFError:
        break