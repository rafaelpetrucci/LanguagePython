def menu_():
    menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Criar Conta
[6] Listar contas
[7] Listar CPFs - Usuários
[q] Sair

Opção: """

    return input(menu)


USUARIO = {'atual': ''}


def saque(*, banco, agencia):
    tamanho = len(banco[agencia])
    if tamanho > 0:
        conta = int(input('Informe a conta para saque: '))
        if 1 >= conta <= tamanho:
            valor = float(input("Informe o valor do saque: "))
            if valor > banco[agencia][conta - 1]['saldo']:
                print("Você não tem saldo suficiente")
            elif valor > banco[agencia][conta - 1]['limite']:
                print("O valor do saque excede o limite disponível.")
            elif banco[agencia][conta - 1]['saques'] >= banco[agencia][conta - 1]['lim_saques']:
                print("Número máximo de saques atingido.")
            elif valor > 0:
                banco[agencia][conta - 1]['saldo'] -= valor
                banco[agencia][conta - 1]['extrato'] += f"Saque: R$ {valor:.2f}\n"
                banco[agencia][conta - 1]['saques'] += 1
            else:
                print("Valor informado inválido.")
        else:
            print('Conta inválida')
    else:
        print('Não existe conta cadastrada no Sistema.')
    return banco


def depositar(banco, agencia, /):
    tamanho = len(banco[agencia])
    if tamanho > 0:
        conta = int(input('Informe a conta para deposito: '))
        if 1 >= conta <= tamanho:
            valor = float(input("Informe o valor de depósito: "))

            if valor > 0:
                banco[agencia][conta - 1]['saldo'] += valor
                banco[agencia][conta - 1]['extrato'] += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Valor informado inválido.")
        else:
            print('Conta inválida')
    else:
        print('Não existe conta cadastrada no Sistema.')
    return banco


def visualizar(banco, /, *, agencia):
    tamanho = len(banco[agencia])
    if tamanho > 0:
        conta = int(input('Informe a conta para extrato: '))
        if 1 >= conta <= tamanho:
            print("--- Extrato ---")
            print("Não foram realizadas movimentações." if not banco[agencia][conta - 1]['extrato'] else banco[agencia][conta - 1]['extrato'])
            print(f"\nSaldo: R$ {banco[agencia][conta - 1]['saldo']:.2f}")
            print("---------------")
        else:
            print('Conta inválida')
    else:
        print('Não existe conta cadastrada no Sistema.')


def criar_usuario():
    cpf = input('Digite o CPF: ')
    if cpf not in USUARIO:
        aux = dict()
        aux['Nome'] = input('Digite o nome do Usuário: ')
        aux['Data Nascimento'] = input('Digite a data de nascimento: ')
        aux['Endereço'] = input('Digite o endereço: ')
        USUARIO[cpf] = aux
        USUARIO['atual'] = cpf
        print("Usuário cadastrado!")
    else:
        print("O CPF informado já existe no sistema.")


def criar_conta(banco, agencia):
    if USUARIO['atual'] != '':
        cpf = input('Informe o CPF para criar a conta: ')
        if cpf in USUARIO:
            conta = {'saldo': 0,
                     'limite': 500,
                     'extrato': "",
                     'saques': 0,
                     'lim_saques': 3,
                     'cpf': cpf}
            banco[agencia].append(conta)
            print('Conta Criada com sucesso.')
        else:
            print('CPF inválido!')
    return banco

def listar_user():
    for cpf, valor in USUARIO.items():
        if cpf == 'atual':
            continue
        print(f"NOME: {valor['Nome']}")
        print(f"CPF: {cpf}")
        print(f"Data Nascimento: {valor['Data Nascimento']}")
        print(f"Endereço: {valor['Endereço']}")
        print('-----------------------------')


def listar_contas(banco, agencia):
    for i, valor in enumerate(banco[agencia]):
        print(f'Conta: {i+1}')
        print(f"Usuário: {valor['cpf']}")
        print(f"limite: {valor['limite']}")
        print(f"saques: {valor['saques']}")
        print(f"Saques Limite: {valor['lim_saques']}")
        print('-----------------------------')



agencia = '0001'
banco = {agencia: []}
while True:

    opcao = menu_()

    if opcao == '1':
        banco = depositar(banco, agencia)
    elif opcao == '2':
        banco = saque(banco=banco, agencia=agencia)
    elif opcao == '3':
        visualizar(banco, agencia=agencia)
    elif opcao == '4':
        criar_usuario()
    elif opcao == '5':
        banco = criar_conta(banco, agencia)
    elif opcao == '6':
        listar_contas(banco, agencia)
    elif opcao == '7':
        listar_user()
    elif opcao == 'q':
        break
    else:
        print("Opção inválida.")
