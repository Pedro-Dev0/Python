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