t = int(input())
for p in range(t):
    populacao = list()
    count = 0
    valor = str(input()).strip()
    separado = valor.split(' ')
    for c in range(len(separado)):
        if c < 2:
            populacao.append(int(separado[c]))
        else:
            populacao.append(float(separado[c]))
    while populacao[0] <= populacao[1]:
        count += 1
        populacao[0] += int(populacao[0] * (populacao[2]/100))
        populacao[1] += int(populacao[1] * (populacao[3]/100))
        if count > 100:
            break
    if count > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(count))
