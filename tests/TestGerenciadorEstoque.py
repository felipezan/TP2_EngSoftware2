import unittest
from datetime import datetime, timedelta
from sistema_gerenciamento import GerenciadorEstoque, GerenciadorUsuarios, SistemaGerenciamento

class TestGerenciadorEstoque(unittest.TestCase):
    def setUp(self):
        self.estoque = GerenciadorEstoque()

    def test_adicionar_produto_com_sucesso(self):
        resultado = self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        self.assertTrue(resultado)
        self.assertEqual(self.estoque.obterProduto("001"), {"nome": "Produto A", "preco": 10.0, "quantidade": 5})

    def test_adicionar_produto_duplicado(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        resultado = self.estoque.adicionarProduto("001", "Produto B", 15.0, 3)
        self.assertFalse(resultado)

    def test_remover_produto_existente(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        resultado = self.estoque.removerProduto("001")
        self.assertTrue(resultado)
        self.assertIsNone(self.estoque.obterProduto("001"))

    def test_remover_produto_inexistente(self):
        resultado = self.estoque.removerProduto("999")
        self.assertFalse(resultado)

    def test_atualizar_quantidade_produto_existente(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        resultado = self.estoque.atualizarQuantidade("001", 10)
        self.assertTrue(resultado)
        self.assertEqual(self.estoque.obterProduto("001")["quantidade"], 10)

    def test_atualizar_quantidade_produto_inexistente(self):
        resultado = self.estoque.atualizarQuantidade("999", 10)
        self.assertFalse(resultado)

    def test_obter_produto_existente(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        produto = self.estoque.obterProduto("001")
        self.assertEqual(produto, {"nome": "Produto A", "preco": 10.0, "quantidade": 5})

    def test_obter_produto_inexistente(self):
        produto = self.estoque.obterProduto("999")
        self.assertIsNone(produto)

    def test_listar_produtos(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        self.estoque.adicionarProduto("002", "Produto B", 15.0, 3)
        produtos = self.estoque.listarProdutos()
        self.assertEqual(len(produtos), 2)
        self.assertIn({"nome": "Produto A", "preco": 10.0, "quantidade": 5}, produtos)
        self.assertIn({"nome": "Produto B", "preco": 15.0, "quantidade": 3}, produtos)        

