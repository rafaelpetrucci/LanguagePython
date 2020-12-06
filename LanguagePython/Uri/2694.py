n = int(input())
for i in range(n):
    recebe = ''
    soma = 0
    valor = input().lower()
    tamanho = len(valor)
    for j in range(tamanho):
        if valor[j].isnumeric():
            recebe += valor[j]
            if j == tamanho - 1 or not valor[j + 1].isnumeric():
                valorAux = recebe
                recebe = ''
                soma += int(valorAux)
    print(soma)