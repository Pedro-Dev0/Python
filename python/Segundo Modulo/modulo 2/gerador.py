# geradores são uma forma simples e eficiente de criar iteradores usando funções
# geradores utilizam a palavra-chave yield para produzir uma série de valores ao longo do tempo, pausando o estado da função entre cada valor
# quando a função geradora é chamada, ela retorna um objeto gerador sem executar o corpo da função imediatamente
# cada vez que o método __next__() do gerador é chamado, a função é executada até encontrar a próxima instrução yield, que produz um valor e pausa a execução novamente
# geradores são úteis para trabalhar com grandes conjuntos de dados ou fluxos de dados infinitos
# exemplo de gerador personalizado

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3, 4, 5]):
    print(i)

