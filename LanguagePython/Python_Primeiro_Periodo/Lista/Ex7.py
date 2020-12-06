'''QUESTÃO 07: Ler o nome de 2 times e o número de gols marcados na
partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser
impresso a palavra EMPATE.'''

print('Questão 07!')

times = list()
gols = list()

for count in range(2):
    times.append(str(input(f'Digite o nome do {count+1}º Time: ')).capitalize().strip())
    while True:
        gol = str(input(f'Digite quantos gols o {times[count]} fez na partida: ')).strip()
        if gol.isnumeric():
            gols.append(int(gol))
            break
        else:
            print('ERRO! Você digitou a quantidade de gols inválida!')
if gols[0] > gols[1]:
    print(f'O time vencedor da partida foi o {times[0]}!')
elif gols[1] > gols[0]:
    print(f'O time vencedor da partida foi o {times[1]}!')
elif gols[0] == gols[1]:
    print(f'Os times {times[0]} e {times[1]} terminaram a partida EMPATADOS.')