'''Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro K indicando o
número de consultas que serão realizadas (0 < K ≤ 103). A segunda linha de um caso de teste contém dois números inteiros N e M
 representando as coordenadas do ponto divisor (-104 < N, M < 104). Cada uma das K linhas seguintes contém dois inteiros X e Y
 representando as coordenadas de uma residência (-104 ≤ X, Y ≤ 104).Em todas as coordenadas dadas, o primeiro valor  corresponde
 à direção leste-oeste, e o segundo valor corresponde à direção norte-sul.

O final da entrada é indicado por uma linha que contém apenas o número zero.

Saída
Para cada caso de teste da entrada seu programa deve imprimir uma linha contendo:

a palavra divisa se a residência encontra-se em cima de uma das linhas divisórias (norte-sul ou leste-oeste);
NO se a residência encontra-se na Nlogônia do Noroeste;
NE se a residência encontra-se na Nlogônia do Nordeste;
SE se a residência encontra-se na Nlogônia do Sudeste;
SO se a residência encontra-se na Nlogônia do Sudoeste.'''


while True:
    consultas = int(input()) #Número de consultas
    if consultas == 0:
        break
    n, m = str(input()).strip().split(' ')
    n = int(n)
    m = int(m)
    for c in range(consultas):
        x, y = str(input()).strip().split(' ')
        x = int(x)
        y = int(y)
        if x > n:
            if y > m:
                print('NE')
            elif y < m:
                print('SE')
            elif y == m:
                print('divisa')
        elif x < n:
            if y > m:
                print('NO')
            elif y < m:
                print('SO')
            elif y == m:
                print('divisa')
        elif x == n:
            print('divisa')
