'''QUESTÃO 06: As maçãs custam R$ 1,30 cada se forem compradas menos de
uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um
programa que leia o número de maçãs compradas, calcule e escreva o custo
total da compra'''

print('Questão 06!')

while True:
    quantidade = str(input('Digite o número de maçãs compradas: ')).strip()
    if quantidade.isnumeric():
        quantidade = int(quantidade)
        break
    else:
        print('ERRO! Você digitou o valor incorreto!')
if quantidade < 12:
    valorTotal = 1.30 * quantidade
elif quantidade >= 12:
    valorTotal = quantidade
print(f'O valor total da compra é de: R${valorTotal:.2f}')