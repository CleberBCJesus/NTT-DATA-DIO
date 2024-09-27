# é um bloco de código identificado por um nome e
# pode receber uma lista de parâmetros, esses parâmetros podem
# ou não ter valores padrão
# paradigma estruturado

def exibir_mensagem():
    print("olá mundo")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")


exibir_mensagem()
exibir_mensagem_2(nome="Cleber")
exibir_mensagem_3()
exibir_mensagem_3(nome="Diego")


def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([1,2,3,10]))
print(retornar_antecessor_sucessor(10))



def salvar_carro(marca, modelo, ano, placa):
    # salvar no banco de dados...
    print(f"Carro inserido com sucesso! {marca} - {modelo} - {ano} - {placa}")


salvar_carro("Fiat","Palio",1999,"abc-1234")
salvar_carro(marca = "Fiat",modelo = "Palio",ano = 1999,placa = "abc-1234")
salvar_carro(**{"marca":"Fiat","modelo":"Palio","ano":1999,"placa":"abc-1234"})



def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Quinta-feira, 26/09/2024",
    "aaaaaaaaaa",
    "bbbbbbbbbbbb",
    "cccccccccccccc",
    "ddddddddddddddddd",
    autor="Cleber",
    ano=1999,
)

