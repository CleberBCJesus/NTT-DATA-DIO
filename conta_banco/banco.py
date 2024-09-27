# versao 1
# trabalha com apenas 1 usuario
# sacar - depositar - extrato
# limite máximo de 3 saques diários, limite máximode 500,00 por saque
# exibir mensagem por falta de saldo
# guardar todos os saques em uma variável e exibir na operação extrato
# no final do extrato exibir o saldo atual


menu = '''
    ---- Escolha uma das opções abaixo ----
    [1] depositar
    [2] sacar
    [3] extrato
    [4] sair
    ---------------------------------------
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)


    if opcao == "1":
        deposito = float(input("Digite o valor para deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Valor depositado: R${deposito}\n"
            print("Deposito realizado com sucesso!")
        else:
            print("Valor do depósito inválido!")
        
    
    elif opcao == "2":
        saque = float(input("Digite o valor a ser sacado: "))
        if saque <= limite and numero_saques <= LIMITE_SAQUES and saque > 0 and saque <= saldo:
            saldo -= saque
            numero_saques += 1
            extrato += f"Valor sacado: R${saque}\n"
            print("Saque realizado com sucesso!")
        
        elif saque > limite:
            print("O limite de saque é de R$ 500,00")

        elif saque > saldo:
            print("Você está sem saldo, veja seu extrato")

        elif numero_saques > LIMITE_SAQUES:
            print("Você excedeu o limite diário de saque")

        else:
            print("Ocorreu algum problema, reveja o valor de saque")


    elif opcao == "3":
        print("---------- EXTRATO ----------")
        print("Sem movimentações no período!" if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Opção inválida")
