import os
import shutil

# criar diretorio
#os.mkdir("exemplo")

#mover arquivo
#shutil.move('C:/Users/Malleus/Documents/GitHub/Python/girikakuri.txt' , 'C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos')

#renomear arquivo
#os.rename('C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos/girikakuri.txt' , 'C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos/bbnomoney.txt')

#escrever
file = open('C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos/bbnomoney.txt', 'w+')
file.write(f'BERSERK é um anime e manga feito por Kentaro Miura e Tetsuya Saito e fala sobre a luta pela sobrevivência em um mundo pós-apocalíptico, tudo isso interpretado por seu protagonista o Guts que se depara com inúmeras adversidades e desafios juntamente com a marca da maldição\n AHHAAHAHAHAH')

#ler
file = open('C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos/bbnomoney.txt', 'r')
conteudo = file.read()
print(conteudo)
file.close

#remover arquivo
#os.remove('C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos/bbnomoney.txt')

try:
    shutil.move('C:/Users/Malleus/Documents/GitHub/Python/girikakuri.txt' , 'C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos')
except FileNotFoundError as exc:
    print('Arquivo não encontrado')
    print(exc)

try:
    file = open('C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/', 'r')
except PermissionError as exc:
    print('não foi possivel abrir o arquivo')
    print(exc) 