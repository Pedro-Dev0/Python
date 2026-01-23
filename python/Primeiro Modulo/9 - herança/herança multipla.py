class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass


gato = Gato(nro_patas=4, cor_pelo="marrom")
ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="preto", cor_bico="amarelo")

print(gato.cor_pelo)
print(ornitorrinco.cor_pelo)  # Isso causará um erro, pois ornitorrinco não tem cor_pelo definido