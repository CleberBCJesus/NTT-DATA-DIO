# import datetime
from datetime import datetime

# d = datetime.datetime.now()
data_hora_atual = datetime.now()
mascara_ptbr = "%d/%m/%Y"
mascara_en = "%Y-%m-%d %H:%M"
data_hora_str = "2024-01-10 10:20"

# print(d.strftime("%d/%m/%Y %H:%M"))
print(data_hora_atual.strftime(mascara_ptbr))

print(type(data_hora_str))


data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)

print(type(data_convertida))