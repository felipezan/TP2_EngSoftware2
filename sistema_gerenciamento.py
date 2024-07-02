import datetime
import re

class GerenciadorEstoque:
    def __init__(self):
        self.produtos = {}
        self.vendas = []

    # metodo que adiciona um novo produto ao estoque
    def adicionarProduto(self, codigo, nome, preco, quantidade):
        if codigo not in self.produtos:
            self.produtos[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
            return True
        return False

    # metodo que remove um produto do estoque
    def removerProduto(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo]
            return True
        return False

    # metodo que atualiza a quantidade de um produto
    def atualizarQuantidade(self, codigo, nova_quantidade):
        if codigo in self.produtos:
            self.produtos[codigo]["quantidade"] = nova_quantidade
            return True
        return False        