def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da função ser chamada.")
        func(*args, **kwargs)  # Chama a função original
        print("Depois da função ser chamada.")
    return wrapper

@meu_decorador
def minha_funcao(nome):
    print(f"Esta é a minha função, {nome}.")

minha_funcao("Alice")  # Chama a função decorada

#meu_decorador(minha_funcao)()  # Chama a função decorada

# decorado nada mais é do que uma função que recebe que é gravada por return e retorna outra função por argumento ou seja a função decorada 

# args e kwargs são usados para passar argumentos para a função original, permitindo que o decorador seja flexível e possa ser aplicado a funções com diferentes assinaturas e não quebra a função original.