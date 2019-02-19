class Humano():

    def __init__(self, nome, idade, cor, peso):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.peso = peso

    def envelhecer(self):
        self.idade += 1

class Homem(Humano):

    def __init__(self, nome, idade, cor, peso, veiculo):
        # Chama o construtor da classe de quem herdou
        #super(Homem, self).__init__(nome, idade, cor)
        super().__init__(nome, idade, cor, peso)
        self.veiculo = veiculo

    def envelhecer(self):
        self.idade += 2
        
class Mulher(Humano):

    def engravidar(self):
        self.peso += 200

paramahansa = Homem('Paramahansa Yogananda', 45, 'Negro', 85, 'Fan 125cc')
coen = Mulher('Monja Coen', 50, 'Branca', 50)
print(coen.peso)
coen.engravidar()
print(coen.peso)
exit()

for i in range(0, 10):
    print(coen.nome, coen.idade)
    coen.envelhecer()

for i in range(0, 10):
    print(paramahansa.nome, paramahansa.idade)
    paramahansa.envelhecer()


