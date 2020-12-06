t = int(input())
for p in range(t):
    anos = 0
    PA, PB, G1, G2 = (str(input()).strip().split())
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    while PA <= PB:
        anos += 1
        PA += int(PA * (G1/100))
        PB += int(PB * (G2/100))
        if anos > 100:
            break
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(anos))
