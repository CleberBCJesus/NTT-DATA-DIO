# operador E = and
# operador de negação = not
# operador OU = or
# 
# 
# 
# 
# 

saldo = 1000
saque = 200
limite = 100
conta_especial = True


print(saldo >= saque and saque <= limite)
print(not 1000 > 500)
print((saldo >= saque) or (conta_especial and saldo < saque))