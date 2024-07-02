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

    def test_realizar_venda_com_estoque_suficiente(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        resultado = self.estoque.realizarVenda("001", 3)
        self.assertEqual(resultado, 30.0)
        self.assertEqual(self.estoque.obterProduto("001")["quantidade"], 2)

    def test_realizar_venda_com_estoque_insuficiente(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        resultado = self.estoque.realizarVenda("001", 6)
        self.assertIsNone(resultado)
        self.assertEqual(self.estoque.obterProduto("001")["quantidade"], 5)

    def test_obter_relatorio_vendas(self):
        self.estoque.adicionarProduto("001", "Produto A", 10.0, 5)
        self.estoque.realizarVenda("001", 2)
        data_inicio = datetime.now() - timedelta(days=1)
        data_fim = datetime.now() + timedelta(days=1)
        relatorio = self.estoque.obterRelatorioVendas(data_inicio, data_fim)
        self.assertEqual(len(relatorio), 1)
        self.assertEqual(relatorio[0]["codigo"], "001")
        self.assertEqual(relatorio[0]["quantidade"], 2)
        self.assertEqual(relatorio[0]["valor_total"], 20.0)

class TestGerenciadorUsuarios(unittest.TestCase):
    def setUp(self):
        self.usuarios = GerenciadorUsuarios()

    def test_adicionar_usuario_valido(self):
        resultado = self.usuarios.adicionarUsuario("João", "joao@email.com", "senha123")
        self.assertTrue(resultado)

    def test_adicionar_usuario_email_invalido(self):
        resultado = self.usuarios.adicionarUsuario("João", "joao@email", "senha123")
        self.assertFalse(resultado)

    def test_adicionar_usuario_email_duplicado(self):
        self.usuarios.adicionarUsuario("João", "joao@email.com", "senha123")
        resultado = self.usuarios.adicionarUsuario("Maria", "joao@email.com", "outrasenha")
        self.assertFalse(resultado)