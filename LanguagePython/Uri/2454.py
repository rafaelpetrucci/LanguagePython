valorStr = str(input()).strip()
valor = valorStr.split()

if valor[0] == '0':
    print('C')
else:
    if valor[1] == '0':
        print('B')
    elif valor[1] == '1':
        print('A')