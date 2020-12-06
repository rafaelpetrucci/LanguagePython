valorStr = str(input()).strip()
valor = valorStr.split()

if valor[3] == '1':
    if valor[4] == '1':
        print('Jogador 2 ganha!')
    else:
        print('Jogador 1 ganha!')
elif valor[3] == '0':
    if valor[4] == '1':
        print('Jogador 1 ganha!')
    else:
        soma = int(valor[1]) + int(valor[2])
        if valor[0] == '1':
            if soma % 2 == 0:
                print('Jogador 1 ganha!')
            else:
                print('Jogador 2 ganha!')
        elif valor[0] == '0':
            if soma % 2 == 0:
                print('Jogador 2 ganha!')
            else:
                print('Jogador 1 ganha!')