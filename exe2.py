
# Observe o diagrama de classes abaixo, que representa uma associação onde um Pedido possui uma lista de Produtos.



# Implemente as classes Produto e Pedido.

# Classe Pedido:
# Atributos:
# produtos: Lista de objetos do classe Produto (inicializar no construtor como uma lista vazia)
# Métodos:
# adicionar_produto: recebe um objeto Produto e o adiciona na lista de produtos.
# calcular_valor: deve retornar o valor total do pedido (soma dos preços de todos os produtos do pedido)

# Classe Produto:
# Atributos:
# nome: nome do produto
# preco: preço do produto
# quantidade: quantidade de itens do produto
# Métodos: 
# Não possui


# Você pode utilizar o programa abaixo para testar as suas classes:

# cafe = Produto('Café Solúvel', 5.50, 1)
# arroz = Produto('Arroz Integral', 4.90, 2)
# feijao = Produto('Feijão Preto', 2.80, 2)
# meu_pedido = Pedido()
# meu_pedido.adicionar_produto(cafe)
# meu_pedido.adicionar_produto(arroz)
# meu_pedido.adicionar_produto(feijao)
# print('O valor total é: ', meu_pedido.calcular_valor())	    # imprime 20.90

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self,produto):
        self.produtos.append(produto)
    
    def calcular_valor(self):
        soma = 0 
        for i in self.produtos:   # i  é a variavel indice
            preco_produto = i.quantidade * i.preco
            soma += preco_produto
        return soma
            
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())
            
# cafe = Produto('Zero Bala', 5.50, 1)
# arroz = Produto('Colher Integral', 4.90, 2)
# feijao = Produto('Arroz Preto', 2.80, 2)

# meu_pedido = Pedido()

# meu_pedido.adicionar_produto(cafe)
# meu_pedido.adicionar_produto(arroz)
# meu_pedido.adicionar_produto(feijao)

# print(meu_pedido.produtos)

