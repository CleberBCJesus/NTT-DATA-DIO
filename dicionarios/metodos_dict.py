contatos = {
    "cbc@gmail.com": {"nome": "Cleber", "idade": 39},
    "cbc1@gmail.com": {"nome": "Nice", "idade": 52},
    "cbc2@gmail.com": {"nome": "Diego", "idade": 14, "extra": {"a":1}},
}


# limpar o dicionario
contatos.clear()
# copiar o dicionario
copia = contatos.copy()
# criar chaves
dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "fone"], "vazio")

# acessar valor
contatos.get("chave") # None = padrão se não encontrar a chave
contatos.get("chave", {}) # retorna {} 
contatos.get("cbcj@gmail.com",{})

contatos.items() # retorna uma lista de tuplas

contatos.keys() # retorna só as chaves


# remover 
resultado = contatos.pop("cbcj@gmail.com", "não entrei a chave")

contatos.popitem() # retira na sequencia

# insere o valor se a chave não existir
contatos. setdefault("nome", "gui")

# atualizar uma chave que já existe ou insere se não existir
contatos.update({"cbcj@gmail.com": {"nome": "cleber"}})


# retorna só os valores
contatos.values()


# se tem valores no dict
"cbcj@gmail.com" in contatos
"idade" in contatos["cbcj@gmail.com"]


# remover objetos
del contatos["cbcj@gmail.com"]["telefone"] # remove só o telefone
del contatos["cbc1@gmail.com"]


