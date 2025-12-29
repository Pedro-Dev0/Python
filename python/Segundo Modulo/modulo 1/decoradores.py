def bom_dia(nome):
    return f"Bom dia! {nome}"

def mensagem_pedro(funcao, nome):
    return funcao(nome)

print(mensagem_pedro(bom_dia, "Ana"))

# funções internar = inner functions 
def saudacao(nome):
    def bom_dia():
        return f"Bom dia! {nome}"
    
    def boa_tarde():
        return f"Boa tarde! {nome}"
    
    if nome == "Pedro":
        return bom_dia()
    else:
        return boa_tarde()

print(saudacao("Pedro"))
print(saudacao("Maria"))
    
def calcular(operacao):
    def soma(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b
    
    """if operacao == "+":
        return soma
    else:
        return subtracao"""
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtracao
        
resultado = calcular("+")(5, 3)
print(resultado)
resultado = calcular("-")(5, 3)
print(resultado)

def meu_decorador(funcao):
    def envelope():
        print("Executando antes da função")
        funcao()
        print("Executando depois da função")
    return envelope

@meu_decorador # açucar sintático para que não precise ficar atribuindo a função decorada a uma variável, nesse caso a própria função pega como referencia o meu decorador e junta com a função diz_ola
def diz_ola():
    print("Olá Mundo!")




"""diz_ola = meu_decorador(diz_ola)"""
diz_ola()

