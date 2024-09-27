# 3 formas de interpolar strings
# %, format, f strings

nome = "Cleber"
idade = 39
profissao = "Fiscal de loja"

dados = {"nome": "Cleber", "idade": 20}

print(" Olá, meu nome é %s. Eu tenho %d anos de idade, trabalho com %s." % (nome, idade, profissao))

print(" Olá, meu nome é {}. Eu tenho {} anos de idade, trabalho com {}." .format(nome, idade, profissao))
print(" Olá, meu nome é {1}. Eu tenho {0} anos de idade, trabalho com {2}." .format(idade, nome, profissao))
print(" Olá, meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao}." .format(nome = nome, idade = idade, profissao = profissao))
print(" Olá, meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao}.".format(**dados))

print(f" Olá, meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao}.")


pi = 3.14159

print(f"Valor de PI: {pi:.2f}") # apenas 2 casas decimais

print(f"Valor de PI: {pi:10.2f}") # 10 espaços em branco