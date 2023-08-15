# Criando o menu

menu = """
----- MENU -----

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção: 
"""

# Variáveis iniciais

saldo = 0
LIMITE = 500 # Constante
extrato = ""
numero_De_Saques = 0
LIMITE_DE_SAQUES = 3 # Constante

# Execução do programa

while True:

    opcao = input(menu)

    if opcao == "d":
        print("----- Depósito -----")
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("""\nErro: Operação falhou!
Por favor digite uma valor válido.\n""")

    elif opcao == "s":
        print("----- Saque -----")
        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_Saldo = (valor > saldo)
        excedeu_Limite = (valor > LIMITE)
        excedeu_Saques = (numero_De_Saques >= LIMITE_DE_SAQUES)

        if excedeu_Saldo:
            print("""\nErro: Operação falhou!
Saldo insuficiente.\n""")

        elif excedeu_Limite:
            print("""\nErro: Operação falhou!
O valor do saque excedeu o limite.\n""")

        elif excedeu_Saques:
            print("""\nErro: Operação falhou!
Número de saques excedido.\n""")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_De_Saques += 1
        else:
            print("""\nErro: Operação falhou!
Por favor digite uma valor válido.\n""")

    elif opcao == "e":
        print("----- Extrato -----")

        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------")

    elif opcao == "q":
        break

    else:
        print("""\nErro: Opção inválida!
Por favor selecione uma das alternativas do menu.\n""")
    