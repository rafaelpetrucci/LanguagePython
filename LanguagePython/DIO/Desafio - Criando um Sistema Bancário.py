menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[q] Sair

Opção: """

saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor informado inválido.")
    elif opcao == '2':
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Você não tem saldo suficiente")
        elif valor > limite:
            print("O valor do saque excede o limite disponível.")
        elif saques >= LIMITE_SAQUES:
            print("Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques += 1
        else:
            print("Valor informado inválido.")
    elif opcao == '3':
        print("--- Extrato ---")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------")
    elif opcao == 'q':
        break
    else:
        print("Opção inválida.")