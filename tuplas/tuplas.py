# estrutura imutável

frutas = ("uva", "coco", "pera", "maçã", "tomate", "cereja",)

letras = tuple("cleber")

numeros = tuple([1,2,3,4])

pais = ("brasil",)


print(frutas[0])
print(frutas[-1])

matriz = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
)


print(matriz[0])
print(matriz[0][2])

frutas[:2]

frutas[1:3]


frutas[0:3:3]
frutas[::-1]
print(frutas.count("uva"))

print(frutas.index("uva"))

len(frutas)
