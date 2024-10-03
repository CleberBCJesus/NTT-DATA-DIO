# listas são objetos mutáveis, podemos alterar seus valores após a criação
# list()
# acesso direto - frutas[0]

frutas = ["uva", "coco","cereja"]



letras = list("Cleber")

numeros = list(range(10))

carro = ["ferrari", "f8", 42000000, 2020, "sbo"]

lista = [1,2,3,4,5,6]

lista_copia = lista.copy()

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(len(lista))
print(lista_copia)
print(letras)
print(numeros)
print(frutas)
print(carro)
print(frutas[0])
print(frutas[-2])


print(matriz[0]) # primeira linha

print(matriz[0][2]) # primeira linha, terceira coluna



lista3 = ["c","l","e","b","e","r"]

lista3[2:]
lista3[:2]
lista3[1:3]
lista3[0:3:2]
lista3[::]
lista3[::-1]

for letra in lista3:
    print(letra)


for indice, letra in enumerate(lista3):
    print(indice, letra)


numeros_2 = [1,10,22,33,45,61,78,4,10201,50]
pares = []

for numero in numeros_2:
    if numero % 2 == 0:
        pares.append(numero)

pares2 = [numero for numero in numeros_2 if numero % 2 == 0]
# quadrado = [numero **2 for numero in numeros]

print(pares)
print(pares2)

