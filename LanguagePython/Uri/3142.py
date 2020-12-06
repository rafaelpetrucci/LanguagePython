while True:
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    try:
        soma = 0
        s = input()
        tamanho = len(s)
        if tamanho > 3:
            print("Essa coluna nao existe Tobias!")
            continue
        elif tamanho == 3:
            if s[0] == 'Y' or s[0] == 'Z':
                print("Essa coluna nao existe Tobias!")
                continue
            elif s[0] == 'X':
                index = alfabeto.index(s[1]) + 1
                if index > 6:
                    print("Essa coluna nao existe Tobias!")
                    continue
                elif index == 6:
                    index = alfabeto.index(s[2]) + 1
                    if index > 4:
                        print("Essa coluna nao existe Tobias!")
                        continue
            index = (alfabeto.index(s[0])+1) * 676
            soma += index
            soma += ((alfabeto.index(s[1])+1) * 26)
            soma += alfabeto.index(s[2]) + 1
            print(soma)
            continue
        elif tamanho == 1:
            index = alfabeto.index(s[0]) + 1
            print(index)
        elif tamanho == 2:
            index = (alfabeto.index(s[0]) + 1) * 26 + (alfabeto.index(s[1]) + 1)
            print(index)
    except EOFError:
        break