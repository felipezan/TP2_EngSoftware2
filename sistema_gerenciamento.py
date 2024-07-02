import datetime
import re

class GerenciadorEstoque:

    # metodo construtor
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

   # metodo que retorna informacoes de um produto
    def obterProduto(self, codigo):
        return self.produtos.get(codigo)

    # metodo que lista todos os produtos no estoque
    def listarProdutos(self):
        return list(self.produtos.values())

    # metodo que realiza uma venda se houver estoque suficiente
    def realizarVenda(self, codigo, quantidade):
        if codigo in self.produtos and self.produtos[codigo]["quantidade"] >= quantidade:
            produto = self.produtos[codigo]
            valor_total = produto["preco"] * quantidade
            self.produtos[codigo]["quantidade"] -= quantidade
            self.vendas.append({
                "codigo": codigo,
                "quantidade": quantidade,
                "valor_total": valor_total,
                "data": datetime.datetime.now()
            })
            return valor_total
        return None

    # metodo que gera um relatorio de vendas para um período especifico
    def obterRelatorioVendas(self, data_inicio, data_fim):
        vendas_periodo = [venda for venda in self.vendas 
                          if data_inicio <= venda["data"] <= data_fim]
        return vendas_periodo

class GerenciadorUsuarios:

    # metodo construtor
    def __init__(self):
        self.usuarios = {}

    # metodo que adiciona um novo usuario se o email for valido e unico
    def adicionarUsuario(self, nome, email, senha):
        if self.validarEmail(email) and email not in self.usuarios:
            self.usuarios[email] = {"nome": nome, "senha": senha}
            return True
        return False

    # metodo que valida o formato do email
    def validarEmail(self, email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao, email) is not None

    # metodo que autentica um usuario
    def autenticarUsuario(self, email, senha):
        if email in self.usuarios and self.usuarios[email]["senha"] == senha:
            return True
        return False    


class SistemaGerenciamento:

    # metodo construtor
    def __init__(self):
        self.estoque = GerenciadorEstoque()
        self.usuarios = GerenciadorUsuarios()

    # metodo que realiza uma venda apenas se o usuario estiver autenticado
    def realizarVendaAutenticada(self, email, senha, codigo_produto, quantidade):
        if self.usuarios.autenticarUsuario(email, senha):
            return self.estoque.realizarVenda(codigo_produto, quantidade)
        return None

    # metodo que gera um relatorio de vendas apenas se o usuario estiver autenticado
    def gerarRelatorioVendasAutenticado(self, email, senha, data_inicio, data_fim):
        if self.usuarios.autenticarUsuario(email, senha):
            return self.estoque.obterRelatorioVendas(data_inicio, data_fim)
        return None        