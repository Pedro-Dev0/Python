# criar função só para ser executada em posição específica, com duas ou mais entradas 
def saudacao(nome, mensagem, /, saudacao_extra, *, pontuacao):
    print(f"Olá, {nome}! {mensagem} {saudacao_extra} {pontuacao}")

# chamando a função com argumentos posicionais
saudacao("Maria", "Bem-vinda ao nosso programa!", "Tenha um ótimo dia", pontuacao="!")
# chamando errado para mostrar erro 
saudacao("Bem-vinda ao nosso programa!", "Maria", "Tenha um ótimo dia", pontuacao="!")  # Isso causará um erro

# chamando a função com argumentos nomeados
#saudacao("João", mensagem="Fico feliz em vê-lo!", saudacao_extra="Aproveite seu tempo", pontuacao=".")
# chamando errado para mostrar erro

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")

exibir_resultado(33, 5, subtrair)

op = subtrair
exibir_resultado(33, 5, op)
print(op(33, 5))  # Chama a função subtrair diretamente através da variável op


#salario bonus em global. sem porcentual

salario = 2000
def calcular_bonus(valor_bonus):
    global salario
    salario += valor_bonus
    print(f"Salário atualizado com bônus: {salario}")

calcular_bonus(3000)
print(f"Salário fora da função: {salario}")
