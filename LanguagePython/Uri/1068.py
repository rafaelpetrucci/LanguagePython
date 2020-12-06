while True:
    try:
        expressao = input().strip()
        parenteses = []
        for valor in expressao:
            if len(parenteses) == 0:
                if valor == ")":
                    parenteses.append(valor)
                    break
                elif valor == "(":
                    parenteses.append(valor)
                else:
                    continue
            else:
                if valor == "(":
                    parenteses.append(valor)
                elif valor == ")":
                    parenteses.pop()
                else:
                    continue
        if len(parenteses) == 0:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break