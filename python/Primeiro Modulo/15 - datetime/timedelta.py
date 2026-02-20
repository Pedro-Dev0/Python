# time delta - diferença entre datas e horas

from datetime import datetime, time, date, timedelta

tipo_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

# formatar para data brasileira
#data_atual = data_atual.strftime('%d/%m/%Y %H:%M:%S')

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta.strftime('%d/%m/%Y %H:%M:%S')(minutes=tempo_pequeno)
    data_estimada_formatada = data_estimada.strftime('%d/%m/%Y %H:%M:%S')
    print(f'O carro saiu ás {data_atual} e a previsão de chegada é ás {data_estimada_formatada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro saiu ás {data_atual} e a previsão de chegada é ás {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro saiu ás {data_atual} e a previsão de chegada é ás {data_estimada}')