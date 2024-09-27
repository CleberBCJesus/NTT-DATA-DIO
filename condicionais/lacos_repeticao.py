# Receba um numero do teclado e mostre os dois proximos numeros 

a = int(input("Informe um numero inteiro:  "))
print(a)

a += 1
print(a)

a += 1
print(a)

# comando "for" - numero exatos de vezes que devemos executar

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# atribui a "letra" cada caractere da string 'texto'
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: # executa no final do laço
    print()



# função built-in "range"
# 3 argumentos: stop, start, step

list(range(4))
# final menos 1 = [0,1,2,3]
list(range(0,4))

for numero in range(0,11):
    print(numero, end=" ")

# tabuada do 5
for numero in range(0, 51, 5): # start = 0, fim = 51(51 - 1), step = 5 em 5
    print(numero, end=" ")



# WHILE
# usado quando não se tem certeza do numero exato de interações

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar [2] Extrato [3] Sair: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato")
else:
    print("Obrigado por usar o sistema, até breve!")





while True:
    opcao2 = int(input("Informe um numero: "))

    if opcao2 == 10:
        break        # sair do laço
        # continue - pula o codigo

    print(opcao2)

