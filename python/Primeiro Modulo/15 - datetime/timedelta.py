# time delta - diferença entre datas e horas

from datetime import datetime, time, date, timedelta

tipo_carro = 'G'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro saiu ás {data_atual} e a previsão de chegada é ás {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro saiu ás {data_atual} e a previsão de chegada é ás {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro saiu ás {data_atual} e a previsão de chegada é ás {data_estimada}')