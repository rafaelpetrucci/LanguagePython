hora = list(map(int, input().split()))
if hora[3] < hora[1]:
    hora[3] += 60
    hora[2] -= 1
if hora[2] < hora[0] or hora[0] == hora[1] == hora[2] == hora[3]:
    hora[2] += 24
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora[2] - hora[0], hora[3] - hora[1]))