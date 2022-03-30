# Exercício 01

# A associação entre classes ocorre quando uma classe possui atributos que são objetos de outra classe. De acordo com esse conceito, observe o diagrama de classes abaixo, que representa uma associação onde uma Pessoa possui um Carro.


# Implemente as classes Pessoa e Carro.

# Classe Pessoa:
# Atributos:
# nome: nome da pessoa
# idade: idade da pessoa
# carro: objeto da classe Carro (valor inicial definido no construtor como None)
# Métodos:
# comprar_carro: recebe um objeto Carro e atribui esse objeto ao atributo carro.

# Classe Carro:
# Atributos:
# marca: marca do carro
# modelo: modelo do carro
# placa: placa do carro
# ano: ano de fabricação do carro
# Métodos: 
# Não possui

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
        self.carro = None
        
    def comprar_carro(self, carro):
        self.carro = carro 
        
       
        

class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano



meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)                            # imprime: João
print('Modelo do meu carro: ', eu.carro.modelo)         # imprime :Gol
print('Placa do meu carro: ', eu.carro.placa)           # imprime: AAA-1111

