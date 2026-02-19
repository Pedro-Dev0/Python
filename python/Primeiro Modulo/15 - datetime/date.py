from datetime import date, datetime

#hora formatada e dia
data_atual = date.today()
print(data_atual)

#data e hora formatada
data_hora_atual = datetime.now()
print(data_hora_atual)

#data e hora formatada com formatação personalizada
data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
print(data_hora_formatada)

data = date(2025, 8, 15)
print(data)

data1 = datetime(2025, 8, 15, 10, 30, 45) # isso é data e hora, não só data
print(data1)