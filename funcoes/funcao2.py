
def criar_carro(modelo, ano, placa,/,marca,motor):
    print(modelo, ano,placa,motor,marca)
    # depois da barra todos devem ser nomeados, antes não



criar_carro("Onix",2022,"qmq4d4", marca="chev",motor="1.0")


def criar_carro2(*,modelo, ano, placa,marca,motor):
    print(modelo, ano,placa,motor,marca)
    # todos os parametros devem ser nomeados


criar_carro2(modelo="Onix",ano=2022,placa="qmq4d4", marca="chev",motor="1.0")



def criar_carro2(modelo, ano,/, placa,*,marca,motor):
    print(modelo, ano,placa,motor,marca)
    # a placa passa a ser opcional



def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(f"resultado: {a} + {b} = {resultado}")


exibir_resultado(10,20, somar)

op = somar

print(op(10,40))


salario = 2000 # variavel global

def salario_bonus(bonus):
    global salario # palavra reservada global
    salario += bonus
    return salario


print(salario_bonus(500))