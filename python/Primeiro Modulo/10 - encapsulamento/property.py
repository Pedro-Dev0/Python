class Foo:
    def __init__(self, x=None):
        self._x = x  # Atributo privado

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)  # Acessando o valor de x via propriedade
foo.x = 5     # Modificando o valor de x via setter
print(foo.x)  # Verificando o valor atualizado de x
del foo.x     # Deletando o valor de x via deleter
print(foo.x)  # Verificando o valor após deleção