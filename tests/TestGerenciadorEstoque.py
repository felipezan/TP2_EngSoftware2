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
