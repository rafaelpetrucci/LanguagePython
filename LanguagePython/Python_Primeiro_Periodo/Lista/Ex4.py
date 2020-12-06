'''QUESTÃO 04: Ler 3 valores (considere que não serão informados valores
iguais) e escrever a soma dos dois maiores'''

print('Questão 04!')

valores = list()

while len(valores) < 3:
    numero = int(input('Digite um valor número Inteiro: '))
    if numero not in valores:
        valores.append(numero)
    else:
        print('ERRO! Valor digitado repetido!')
    valores.sort()
soma = valores[1] + valores[2]
print(f'A soma dos valores {valores[1]} + {valores[2]} é igual à {soma}')