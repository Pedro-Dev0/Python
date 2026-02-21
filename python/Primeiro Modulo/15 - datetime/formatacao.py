from datetime import datetime

data_atual = datetime.now()
print(data_atual)

data_hora_string = '20/06/2024 15:30:00'
mascara = '%d/%m/%Y %H:%M:%S'

data_hora = data_atual.strftime(mascara)
print(data_hora)

# para que serve o strftime? para formatar a data e hora em uma string, ou seja, transformar um objeto datetime em uma string formatada de acordo com a máscara fornecida.  e o strptime? para transformar uma string em um objeto datetime, ou seja, parsear uma string de acordo com a máscara fornecida e retornar um objeto datetime correspondente.