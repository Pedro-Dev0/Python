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