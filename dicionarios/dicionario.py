# classe dict
# conjunto não ordenado de pares chave : valor
# onde as chaves são unicas
# são delimitados por chaves

pessoa = {"nome":"Cleber", "idade":39}

pessoa1 = dict(nome="Nice", idade = 53)

pessoa["telefone"] = "9984571256"


print(pessoa)
print(pessoa["nome"])

pessoa["nome"] = "Diego"

print(pessoa)

# Dicionários aninhados

contatos = {
    "cbc@gmail.com": {"nome": "Cleber", "idade": 39},
    "cbc1@gmail.com": {"nome": "Nice", "idade": 52},
    "cbc2@gmail.com": {"nome": "Diego", "idade": 14, "extra": {"a":1}},
}

contato = contatos["cbc1@gmail.com"]["nome"]
print(contato)

extra = contatos["cbc2@gmail.com"]["extra"]["a"]
print(extra)


for chave in contatos:
    print(chave, contatos[chave])

print("*"*50)

for chave, valor in contatos.items():
    print(chave, valor)


