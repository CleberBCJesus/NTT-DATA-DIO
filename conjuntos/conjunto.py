# set é uma coleção que não possui objetos repetidos
# set([1,2,3,3,4,5,1]) # {1,2,3,4,5}
# elimina numeros elementos iguais
# não tem ordem para eliminação
# não tem indexação

set("abacaxi") # {bacxi}

setando = set (("palio", "gol", "chev", "gol"))

print(setando)

# acessando dados
# converter para lista

lista = list(setando)

print(lista[0])

# ou usar for

carros = {"gol", "hb20", "gm"}

for indice, carro in enumerate(carros):
    print(indice, carro)


conjunto_a = {1,2,3}
conjunto_b = {2,3,4,5}

# união de conjuntos
print(conjunto_a.union(conjunto_b))
# intersecção
print(conjunto_a.intersection(conjunto_b))
# diferença
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.intersection(conjunto_a))
# diferença simétrica
print(conjunto_a.symmetric_difference(conjunto_b))
# se é sub conjunto de um conjunto
print(conjunto_a.issubset(conjunto_b)) # true
# o contrário do anterior
print(conjunto_a.issuperset(conjunto_b)) # False
# se não tem intersecção entre eles
conjunto_c = {1,2}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.intersection(conjunto_c))

sorteio = {1,2}

# adiciona um elemento senão existir no conjunto
sorteio.add(25)
# apaga o conjunto
sorteio.clear()
# fazer uma cópia
sorteio.copy()
# descartar um valor, não retorna erro se o elemento não existir
sorteio.discard(1)
# tira elementos em sequencia
sorteio.pop()
# remover elementos da lista, retorna erro se não existir no conjunto
sorteio.remove(0)

# tamanho
len(sorteio)

# se um elemento está no conjunto
1 in sorteio
