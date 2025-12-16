def exibir_mensagem():
    print("Olá! Esta é uma mensagem exibida pela função exibir_mensagem.")

exibir_mensagem()

def somar_numeros(a, b):
    return a + b      
resultado = somar_numeros(20, 7)
print(f"A soma é: {resultado}")

somar_numeros

def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

saudacao_personalizada("Ana")

def saudacao_personalizada1(nome="Visitante"):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")


saudacao_personalizada1()
saudacao_personalizada1("Carlos")