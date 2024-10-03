# trabalhando com fuso-horários

# python -m venv .env

# source .env/bin/activate

# pip install pytz

from datetime import datetime, timezone, timedelta
import pytz

dat_hora_atual = datetime.now(pytz.timezone("Europe/Oslo"))
dat_hora_atual_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(dat_hora_atual)
print(dat_hora_atual_2)

# sem usar o pytz
# offset = diferenças de horas

data3_oslo = datetime.now(timezone(timedelta(hours=2)))
data3_sp = datetime.now(timezone(timedelta(hours=-3)))

print()
print(data3_oslo)
print(data3_sp)

date_s = "2023-05-01"
data_o = datetime.strptime(date_s, "%Y-%d-%m")
print(data_o)