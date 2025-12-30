import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Executando antes da função")
        resultado = funcao(*args, **kwargs)
        print("Executando depois da função")
        return resultado

    return envelope

@meu_decorador
def diz_ola(nome, sobrenome="Silva"):
    print(f"Olá Mundo! {nome} {sobrenome}")
    return f"{nome.upper()} {sobrenome.upper()}"

#*args, **kwargs permitem passar uma quantidade variável de argumentos para a função decorada

#/ * e aqui permitem que a função envelope de ordens de passagem dos argumentos para a função original

resultado = diz_ola("Pedro")
print(f"Resultado da função decorada: {resultado}")

print(diz_ola.__name__)  # Isso mostrará 'envelope' sem o uso de functools.wraps
print(diz_ola.__name__) # Isso mostrará 'diz_ola' com o uso de functools.wraps