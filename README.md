# Trabalho Prático 2 - Engenharia de Software 2

## Sistema de Gerenciamento de Estoque e Vendas

## Descrição
Este projeto é um sistema simples de gerenciamento de estoque e vendas, desenvolvido em Python utilizando a metodologia TDD (Test-Driven Development) para a disciplina de Engenharia de Software 2 da UFMG. Este sistema oferece funcionalidades para gerenciar produtos, realizar vendas, gerar relatórios e autenticar usuários. O objetivo principal do projeto é praticar conhecimentos no desenvolvimento de testes de unidade, testes de integração e automação de testes.

## Funcionalidades Principais
- Gerenciamento de estoque (adicionar, remover, atualizar produtos)
- Realização de vendas
- Geração de relatórios de vendas
- Gerenciamento de usuários (adicionar, autenticar)
- Operações autenticadas (vendas e relatórios)

## Estrutura do Projeto
O projeto possui três classes:
1. `GerenciadorEstoque`: Gerencia operações relacionadas ao estoque de produtos.
2. `GerenciadorUsuarios`: Lida com a gestão e autenticação de usuários.
3. `SistemaGerenciamento`: Integra as funcionalidades de estoque e usuários.

## Desenvolvimento Baseado em TDD
Este sistema está sendo desenvolvido seguindo os princípios do TDD:
1. Escrita de testes antes da implementação do código.
2. Implementação do código mínimo necessário para passar nos testes.
3. Refatoração do código mantendo a passagem nos testes.

## Testes
O projeto inclui: 
- 15 testes unitários cobrindo todas as funcionalidades básicas.
- 5 testes de integração para validar a interação entre diferentes componentes do sistema.