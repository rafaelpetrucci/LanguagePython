'''QUESTÃO 10: Um mercado está vendendo frutas com a seguinte tabela de
Até 5Kg:                                        Acima de 5Kg:
Morango: R$ 2,00 p/Kg                           R$ 1,80 p/Kg
Maçã: R$ 1,50 p/Kg                              R$ 1,10 p/Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo
cliente.'''

def validaKg(str): #Função para verificar se o mesmo digitou um valor certo. [Número, ou Numero + letra]
    lista = list()
    for k, c in enumerate(str):
        if c.isnumeric() and k == 0:
            lista.append(c)
        else:
            if c.isnumeric():
                lista.append(c)
            elif c == '.':
                if k == 0:
                    lista.append('0')
                    lista.append('.')
                elif '.' not in lista:
                    lista.append(c)
    return lista


def validaReal(lista): #Função para verificar se o mesmo consegue realizar a transformação do valor informado para o Float.
    real = ''.join(lista)
    try:
        float(real)
        return True
    except:
        return False

#Programa Principal

print('Questão 10!')

ValorTotal = 0

while True:
    morangoStr = str(input('Quantos KG de Morango: ')).strip().replace(',', '.')
    validacao = validaKg(morangoStr)
    verdadeiro = validaReal(validacao)
    if verdadeiro:
        validacao = ''.join(validacao)
        morango = float(validacao)
        break
    else:
        print('ERRO! Você digitou a quantidade de KG inválida!')
 
while True:
    macaStr = str(input('Quantos KG de Maçã: ')).strip().replace(',', '.')
    validacao = validaKg(macaStr)
    verdadeiro = validaReal(validacao)
    if verdadeiro:
        validacao = ''.join(validacao)
        maca = float(validacao)
        break
    else:
        print('ERRO! Você digitou a quantidade de KG inválida!')

TotalKG = morango + maca

if morango > 5.0:
    ValorTotal += (1.80 * morango)
elif 0 < morango <= 5.0:
    ValorTotal += (2.00 * morango)
if 0 < maca <= 5.0:
    ValorTotal += (1.50 * maca)
elif maca > 5.0:
    ValorTotal += (1.10 * maca)

if TotalKG > 8.0 or ValorTotal > 25.00:
    ValorTotal = ValorTotal * 0.90 #Valor já com o desconto
print(f'O valor total a ser pago é de R${ValorTotal:.2f}')
