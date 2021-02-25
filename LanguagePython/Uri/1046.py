horas = list(map(int, input().split()))
if horas[1] < horas[0]:
    horas[1] += 24
    print("O JOGO DUROU {} HORA(S)".format(horas[1] - horas[0]))
elif horas[0] == horas[1]:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU {} HORA(S)".format(horas[1] - horas[0]))