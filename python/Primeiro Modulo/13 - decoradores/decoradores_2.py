def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da função ser chamada.")
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return wrapper

@meu_decorador
def minha_funcao(nome):
    print(f"Esta é a minha função, {nome}.")
    
    return nome.upper()

resultado = minha_funcao("Alice")
print(f"Resultado da função decorada: {resultado}")
