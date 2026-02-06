def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da função ser chamada.")
        func(*args, **kwargs)  # Chama a função original
        print("Depois da função ser chamada.")
    return wrapper

@meu_decorador
def minha_funcao(nome):
    print(f"Esta é a minha função, {nome}.")

minha_funcao("Alice")