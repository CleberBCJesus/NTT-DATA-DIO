# datetime
# import datetime

# d = datetime.date(2023,7,19)
# print(d)

from datetime import date, datetime, time, timedelta


# criando datas
d = date(2024,8,2)
print(d) # 2024-08-02
print(date.today()) # 2024-09-30


# criando datas e horas
c= datetime(2024,7,20,13,45)
print(c) # 2024-07-20 13:45:00

h = datetime(2024,7,20)
print(h) # 2024-07-20 00:00:00


d = d + timedelta(weeks=2)
print(d) # 2024-08-16

tipo_carros = "p"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carros == "p":
     data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
     print(f"O carro chegou: {data_atual} e ficara pronto em {data_estimada}")
elif tipo_carros == "m":
     print(data_atual)
else:
     print(data_atual)

     
print(date.today() - timedelta(days=1))

resultado = datetime(2024,7,10,19,20 - timedelta(hours=2))
print(resultado.time()) # somente as horas

print(datetime.now().hour)
print(datetime.now().date)


# construindo horas
hora = time(10,20,0)
print(hora)
