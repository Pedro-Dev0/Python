def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada.")
        func()
        print("Depois da função ser chamada.")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Esta é a minha função.")

minha_funcao()  # Chama a função decorada

#meu_decorador(minha_funcao)()  # Chama a função decorada

# decorado nada mais é do que uma função que recebe que é gravada por return e retorna outra função por argumento ou seja a função decorada 

