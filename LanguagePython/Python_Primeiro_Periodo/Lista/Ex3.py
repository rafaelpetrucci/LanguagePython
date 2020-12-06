'''QUESTÃO 03: Ler o ano atual e o ano de nascimento de uma pessoa.
Escrever uma mensagem que diga se ela poderá ou não votar este ano (não
é necessário considerar o mês em que a pessoa nasceu).'''

from datetime import date

print('Questão 03!')
anoAtual = date.today().year
while True:
    nascimento = str(input('Digite o ano do seu Nascimento: ')).strip()
    if nascimento.isnumeric():
        nascimento = int(nascimento)
        break
    else:
        print('ERRO! Você digitou um ano inválido!')
idade = anoAtual - nascimento
if idade >= 18:
    print('Você poderá votar este ano!')
else:
    print('Você não poderá votar este ano!')
