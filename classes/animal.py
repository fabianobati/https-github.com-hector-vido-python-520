# Classe que define uma abstração de mamíferos

class Animal():
    
    def __init__(self, **kwargs):
    #def __init__(self, peso=0, idade=0, cor='', nome='', especie=''):
    #def __init__(self, *args):
        for k in kwargs:
            self[k] = kwargs[k]

    def __str__(self):
        return 'Você printou o gatinho {0}'.format(self.nome)

    def __setitem__(self, key, value):
        setattr(self, key, value)

gatin = Animal(nome='Lucas', cor='Rosa')
gatin2 = Animal(nome='Roger', cor='Pink')

print(gatin)
print(gatin2)
