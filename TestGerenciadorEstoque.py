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