'''QUESTÃO 08: Ler as 3 notas obtidas por um aluno nas 3 verificações e a
média dos exercícios que fazem parte da avaliação. Calcular a média de
aproveitamento, usando a fórmula:
A atribuição de conceitos obedece a tabela abaixo:
Média de Aproveitamento: Conceito:
>= 9,0 A
>= 7,5 e < 9,0 B
>= 6,0 e < 7,5 C
< 6,0 D'''

print('Questão 08!')

def validaReal(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False


notas = list()
count = 1
final = ''
while len(notas) < 4:
    if len(notas) < 3:
        nota = str(input(f'Digite a {count}ª nota do Aluno: ')).strip()
    elif len(notas) == 3:
        nota = str(input(f'Digite a Média dos exercícios: ')).strip()
    validacao = validaReal(nota)
    if validacao and 0 <= float(nota) <= 10:
        notas.append(float(nota))
        count += 1
    else:
        print('A nota informada é inválida:')
media = (((notas[0] + notas[1]) * 2) + (notas[2] * 3) + notas[3])/7
if media >= 9.0:
    final = 'A'
elif media >= 7.5:
    final = 'B'
elif media >= 6.0:
    final = 'C'
elif media >= 0:
    final = 'D'
print(f'A média final do aluno, foi: "{final}"!')