# vendo entrada de dados e saída de dados

nome = input("Qual é o seu nome? ")
print("Olá,", nome)

# como viu acima , usamos a função input() para receber dados do usuário e a função print() para mostrar dados na tela, assim representando a entrada e a saída de dados.

sobrenome = input("Qual é o seu sobrenome? ")
print("Seu nome completo é", nome, sobrenome, end="...\n")
print("Seu nome completo é", nome, sobrenome, sep="#")
print("Seu nome completo é", nome, sobrenome)

# note que no primeiro print() acima, usamos o parâmetro end para mudar o final da linha, que por padrão é uma nova linha (\n). Colocamos "...\n" para que a linha termine com reticências e depois pule para a próxima linha.

# no segundo print() usamos o parâmetro sep para mudar o separador entre os valores que estamos imprimindo. Por padrão, o separador é um espaço em branco, mas colocamos "#" para que os valores sejam separados por esse caractere.