def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Executando antes da função")
        funcao(*args, **kwargs)
        print("Executando depois da função")
    return envelope

@meu_decorador
def diz_ola(nome, sobrenome="Silva"):
    print(f"Olá Mundo! {nome} {sobrenome}")

#*args, **kwargs permitem passar uma quantidade variável de argumentos para a função decorada

#/ * e aqui permitem que a função envelope de ordens de passagem dos argumentos para a função original

diz_ola("Pedro")