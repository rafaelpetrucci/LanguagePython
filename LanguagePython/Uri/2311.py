competidores = int(input())
nome = list()
for c in range(competidores):
    nome.append(str(input()).strip())
    nome.append(float(input()))
    numero = str(input()).strip()
    notas = numero.split(' ')
    for p in range(len(notas)):
        notas[p] = float(notas[p])
    notas.sort()
    notas.pop(0)
    notas.pop(-1)
    soma = sum(notas) * nome[1]
    nome.append(notas[:])
    nome.append(soma)
    print('{} {:.2f}'.format(nome[0], nome[3]))
    nome.clear()
