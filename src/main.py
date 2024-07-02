from src.sistema_gerenciamento import SistemaGerenciamento
from datetime import datetime, timedelta

# metodo que inicializa o sistema
def main():
    
    sistema = SistemaGerenciamento()

    print("Sistema de Gerenciamento de Estoque e Vendas!")

    # adicionando usuarios
    sistema.usuarios.adicionarUsuario("Alice", "alice@email.com", "senha123")
    sistema.usuarios.adicionarUsuario("Bob", "bob@email.com", "senha456")

    # adicionando produtos
    sistema.estoque.adicionarProduto("001", "Camiseta", 29.99, 50)
    sistema.estoque.adicionarProduto("002", "Calça Jeans", 89.99, 30)
    sistema.estoque.adicionarProduto("003", "Tênis", 119.99, 20)