# Trabalho Prático 2 - Engenharia de Software 2

## Sistema de Gerenciamento de Estoque e Vendas

## Descrição
Este projeto é um sistema simples de gerenciamento de estoque e vendas, desenvolvido em Python utilizando a metodologia TDD (Test-Driven Development) para a disciplina de Engenharia de Software 2 da UFMG. Este sistema oferece funcionalidades para gerenciar produtos, realizar vendas, gerar relatórios e autenticar usuários. O objetivo principal do projeto é praticar conhecimentos no desenvolvimento de testes de unidade, testes de integração e automação de testes.

## Funcionalidades do Sistema
- Gerenciamento de estoque (adicionar, remover, atualizar produtos)
- Realização de vendas
- Geração de relatórios de vendas
- Gerenciamento de usuários (adicionar, autenticar)
- Operações autenticadas (vendas e relatórios)

## Estrutura do Projeto
O projeto possui as três classes principais abaixo em sistema_gerenciamento e um main como inicio do programa:
1. `GerenciadorEstoque`: Gerencia operações relacionadas ao estoque de produtos.
2. `GerenciadorUsuarios`: Lida com a gestão e autenticação de usuários.
3. `SistemaGerenciamento`: Integra as funcionalidades de estoque e usuários.

## Desenvolvimento Baseado em TDD
Este sistema está sendo desenvolvido seguindo os princípios do TDD:
1. Escrita de testes antes da implementação do código.
2. Implementação do código mínimo necessário para passar nos testes.
3. Refatoração do código mantendo a passagem nos testes.

## Boas Práticas Implementadas
- Testes através de APIs públicas
- Foco no comportamento em vez da implementação
- Nomes descritivos para os testes
- Testes focados e não-complexos
- Uso de `setUp` pra preparar o ambiente de teste
- Cobertura abrangente de casos de uso, incluindo cenários de erro

## Testes
O projeto inclui: 
- 15 testes unitários cobrindo todas as funcionalidades básicas.
- 5 testes de integração para validar a interação entre componentes do sistema.

### Executando os Testes
Pra executar os testes, use os seguintes comandos:

```
python -m unittest discover -v
```

## Como executar os Testes localmente

1. Clone o repo:
   ```
   git clone https://github.com/felipezan/TP2_EngSoftware2.git
   ```
2. Vá até a raiz:
   ```
   cd TP2_EngSoftware2
   ```
3. Execute os testes:
   ```
   python -m unittest discover -v
   ```

