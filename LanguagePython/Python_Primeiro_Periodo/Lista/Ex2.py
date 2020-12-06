'''QUESTÃO 02: Escreva um algoritmo para ler o salário mensal e o percentual
de reajuste. Calcular e escrever o valor do novo salário.'''
print('Questão 02!')
salarioM = float(input('Digite o seu salário Mensal: R$'))
lista = list()
while True:
    percentual = str(input('Digite o percentual de Reajuste do Salário: ')).strip()
    if percentual.isnumeric():
        percentual = int(percentual)
        break
    elif '%' in percentual:
        for valor in percentual:
            if not valor == '%' and not valor == ' ':
                lista.append(valor)
        ValorInteiro = ''.join(lista)
        if ValorInteiro.isnumeric():
            percentual = int(ValorInteiro)
            break
    print('ERRO! Você digitou um valor inválido! Repita! \n')
SalarioTotal = (salarioM*percentual/100)+salarioM
print(f'O seu novo salário será de R${SalarioTotal}')