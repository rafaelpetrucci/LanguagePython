'''QUESTÃO 09: Um posto está vendendo combustíveis com a seguinte tabela
de descontos:
• Álcool: até 20 litros, desconto de 3% por litro.
• Álcool: acima de 20 litros, desconto de 5% por litro.
• Gasolina: até 20 litros, desconto de 4% por litro.
• Gasolina: acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: Álcool, Gasolina), calcule e
imprima o valor a ser pago pelo cliente sabendo-se que o preço da gasolina
é de R$ 1,20 o litro e o álcool R$ 0,90.'''

print('Questão 09!')


def validaReal(numero):
    try:
        float(numero)
        return True
    except:
        return False

while True:
    litros = str(input('Quantos Litros foram comprados: ')).strip()
    validacao = validaReal(litros)
    if validacao and float(litros) > 0:
        litros = float(litros)
        break
    else:
        print('ERRO! Quantidade de litros informada é inválida!')

while True:
    combustivel = str(input('Digite o tipo de combustível [Gasolina/Alcool]: ')).strip().capitalize()
    if combustivel == 'Gasolina' or combustivel == 'Alcool' or combustivel == 'Álcool':
        break
    else:
        print('ERRO! Você digitou o combustível inválido!!')

desconto = valorTotal = 0

if combustivel == 'Gasolina':
    if litros > 20.0:
        valorTotal = litros * 1.20 * 0.94
    elif litros <= 20.0:
        valorTotal = litros * 1.20 * 0.96
elif combustivel == 'Alcool' or combustivel == 'Álcool':
    if litros > 20.0:
        valorTotal = litros * 0.90 * 0.95
    elif litros <= 20.0:
        valorTotal = litros * 0.90 * 0.97
print(f'O valor total a ser pago é de R${valorTotal:.2f}!')
