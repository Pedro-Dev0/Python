age = 22
name = "Malleus"
print(f'Olá meu nome é {name} e eu tenho {age} anos')

age, name = 22, "Malleus"
print(f'Olá meu nome é {name} e eu tenho {age} anos, e fico muito feliz em aprender Python!')

print('Olá meu nome é', name, 'e eu tenho', age, 'anos')  # atraves do concatenação]

meu_dinheiro = 1000.50
Saquei = 250.50
print(f'Eu tinha R${meu_dinheiro}, saquei R${Saquei} e agora tenho R${meu_dinheiro - Saquei}')
meu_dinheiro = meu_dinheiro - Saquei
print(f'eu tenho R${meu_dinheiro} no meu bolso')

CARTEIRA = 5000.00  # constante todo em maiusculo, não tem em python por isso é usado isso para que os programadores saibam que é uma constante
print(f'Eu tenho R${CARTEIRA} na minha carteira')

# pode ser usado _ para separar nomes grandes/ snake case meu_dinheiro_na_carteira = 3000.00
# ou camel case meuDinheiroNaCarteira = 3000.00