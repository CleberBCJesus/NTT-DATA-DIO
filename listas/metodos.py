lista = []
numeros = [1,2,3,4,5,6,2,3,1,2,5,3,6,8,9,10,10,11]

lista.append(1)
lista.append("cleber")
lista.append([1,2,3])

print(lista)

lista_copia = lista.copy()

lista.clear()

print(lista)
print(lista_copia is lista)
print(id(lista), id(lista_copia))
print(lista_copia)

print(numeros.count(2)) # quantas vezes o elemento aparece na lista

numeral = [1,2,3]
vogal = ["a","b","c"]

print(numeral)
numeral.extend([1,4]) # acrescenta no final

print(numeral)

print(numeral.index(2)) # PRIMEIRA OCORRENCIA do elemento na lista

print(vogal)
vogal.pop() # deleta a partir do ultimo elemento
print(vogal)
vogal.pop()
print(vogal)
vogal.pop(0) # deletar por posição
print(vogal)

vogal = ["a","b","c"]

print(vogal.remove("c")) # remove o elemento pelo nome

print(vogal.reverse()) # espelhamento

lista4 = [10,1,3,6,8,9]
print(lista4)
lista4.sort() # ordena a lista
print(lista4)

lista4 = [10,1,3,6,8,9]
lista4.sort(reverse=True) # ordena e espelha
print(lista4)

lista4 = ["oi", "hello", "uva", "casaco"]
print(lista4)
lista4.sort(key=lambda x: len(x)) # oredena por tamanho
print(lista4)


lista4 = ["oi", "hello", "uva", "casaco"]
print(lista4)
lista4.sort(key=lambda x: len(x), reverse=True) # oredena por tamanho e espelha
# print(sorted(linguagens))
# print(sorted(linguagens, key=lambda x: len(x), reverse))
print(lista4)

print(len(lista4))