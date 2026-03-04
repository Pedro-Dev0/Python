import os
import shutil

# criar diretorio
#os.mkdir("exemplo")

#mover arquivo
shutil.move('C:/Users/Malleus/Documents/GitHub/Python/gurikakuri.txt' , 'C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos')

#renomear arquivo
os.rename('C:/Users/Malleus/Documents/GitHub/Python/python/Primeiro Modulo/16 - arquivos/gurikakuri.txt' , 'bbnomoney.txt')

#remover arquivo
os.remove('C:/Users/Malleus/Documents/GitHub/Python/bbnomoney.txt')

