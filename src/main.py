from src.sistema_gerenciamento import SistemaGerenciamento
from datetime import datetime, timedelta

# metodo que inicializa o sistema
def main():
    
    sistema = SistemaGerenciamento()

    print("Sistema de Gerenciamento de Estoque e Vendas!")

    # adicionando alguns usuarios exemplo
    sistema.usuarios.adicionarUsuario("Alice", "alice@email.com", "senha123")
    sistema.usuarios.adicionarUsuario("Bob", "bob@email.com", "senha456")

    # adicionando alguns produtos exemplo
    sistema.estoque.adicionarProduto("001", "Camiseta", 29.99, 50)
    sistema.estoque.adicionarProduto("002", "Calça Jeans", 89.99, 30)
    sistema.estoque.adicionarProduto("003", "Tênis", 119.99, 20)

    while True:

        # menu principal
        print("\nEscolha uma opção:")
        print("1. Listar produtos")
        print("2. Realizar venda")
        print("3. Gerar relatório de vendas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            produtos = sistema.estoque.listarProdutos()
            print("\nProdutos disponíveis:")
            for produto in produtos:
                print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

        elif opcao == "2":

            email = input("Email do usuário: ")
            senha = input("Senha: ")
            codigo = input("Código do produto: ")
            quantidade = int(input("Quantidade: "))

            resultado = sistema.realizarVendaAutenticada(email, senha, codigo, quantidade)
            if resultado:
                print(f"Venda realizada com sucesso. Valor total: R${resultado:.2f}")
            else:
                print("Falha na venda. Verifique as credenciais, o código do produto e a quantidade disponível.")

        elif opcao == "3":

            email = input("Email do usuário: ")
            senha = input("Senha: ")
            data_inicio = datetime.now() - timedelta(days=30)  # pegando so dos ultimos 30 dias
            data_fim = datetime.now()

            relatorio = sistema.gerarRelatorioVendasAutenticado(email, senha, data_inicio, data_fim)
            if relatorio:
                print("\nRelatório de Vendas:")
                for venda in relatorio:
                    print(f"Código: {venda['codigo']}, Quantidade: {venda['quantidade']}, "
                          f"Valor Total: R${venda['valor_total']:.2f}, Data: {venda['data']}")
            else:
                print("Falha ao gerar relatório. Verifique as credenciais.")

        elif opcao == "4":
            print("Thanks (: ")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()    