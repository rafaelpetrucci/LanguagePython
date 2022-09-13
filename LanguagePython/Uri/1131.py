dicionario = {'Inter': 0, 'Gremio': 0, 'Empates': 0}
while True:
    tupla = tuple(map(int, input().split()))
    if tupla[0] == tupla[1]:
        dicionario['Empates'] += 1
    elif tupla[0] > tupla[1]:
        dicionario['Inter'] += 1
    else:
        dicionario['Gremio'] += 1
    valor = input('Novo grenal (1-sim 2-nao)\n')
    if valor == '2':
        break
total = sum(dicionario.values())
print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}".format(total, dicionario['Inter'], dicionario['Gremio'], dicionario['Empates']))
if dicionario['Inter'] != dicionario['Gremio']:
    if dicionario['Inter'] > dicionario['Gremio']:
        print('Inter venceu mais')
    else:
        print('Gremio venceu mais')
else:
    print('Não houve vencedor')