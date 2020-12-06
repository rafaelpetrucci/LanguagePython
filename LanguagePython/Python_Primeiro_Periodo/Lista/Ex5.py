'''QUESTÃO 05: Ler 3 valores (A, B e C) representando as medidas dos lados
de um triângulo e escrever se forma ou não um triângulo. OBS: para formar
um triângulo, o valor de cada lado deve ser menor que a soma dos outros
dois.'''

print('Questão 05!')

triangulo = list()
for c in range(1, 4):
    triangulo.append(float(input(f'Digite a medida do {c}º Lado do triângulo: ')))
if triangulo[0] < triangulo[1] + triangulo[2] and triangulo[1] < triangulo[0] +triangulo[2] and triangulo[2] < triangulo[0] + triangulo[1]:
    print('Com as medidas ', end='')
    for valor in triangulo:
        print(f'{valor}', end=' -> ')
    print('formam um triângulo!')
else:
    print('Não é possível formar um triângulo com as medidas informadas!')