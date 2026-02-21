import pytz
from datetime import datetime, timezone, timedelta

d = datetime.now(pytz.timezone('Japan'))
print(d)

d = datetime.now(pytz.timezone('America/Sao_Paulo'))
print(d)

sao_paulo = datetime.now(timezone(timedelta(hours=-3)))
print(sao_paulo)

japan = datetime.now(timezone(timedelta(hours=9)))
print(japan)