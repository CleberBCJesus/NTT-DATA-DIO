# permite o desvio de fluxo de controle
# if, else, elif

idade = 10
MAIOR_DE_IDADE = 18

if idade < MAIOR_DE_IDADE:
    print("Menor de idade!")
elif idade >= MAIOR_DE_IDADE:
    print("Maior de idade")


opcao = int(input("Informe uma opcao: [1] Sacar  [2] Extrato:"))

if opcao == 1:
    valor = float(input("Informe o valor a ser sacado: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("opção inválida")

saldo = 0
saque = 10

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")