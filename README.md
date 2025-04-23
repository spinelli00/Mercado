# Mercado
Sistema de Gerenciamento de Estoque e Carrinho de Compras

Este é um sistema simples de gerenciamento de mercadinho, desenvolvido em Python. O projeto visa proporcionar uma interface interativa para a gestão de um estoque de produtos e o carrinho de compras de clientes. O sistema possui duas formas de acesso: com login (para usuários administrativos) e sem login (para usuários comuns).

Funcionalidades principais:
Login de Usuário: Permite que usuários administrativos façam login para acessar funcionalidades exclusivas, como adicionar e remover itens do estoque.

Menu para Usuários Não Logados: Usuários sem login podem visualizar os produtos disponíveis no estoque e adicionar itens ao carrinho de compras.

Gerenciamento de Estoque: O sistema permite adicionar, remover e listar produtos no estoque. As alterações são armazenadas em arquivos locais.

Carrinho de Compras: Usuários podem adicionar itens ao carrinho, mas não têm permissão para modificar o estoque sem login.

Tecnologias Utilizadas:
Python 3

Arquivos de texto (.txt) para armazenamento de dados

Estrutura simples de menus para interação com o usuário

Como usar:
Execute o script main.py.

O programa pedirá para o usuário escolher entre fazer login ou seguir sem login.

No caso de login, o sistema valida as credenciais em um arquivo loginpermitidos.txt.

Dependendo da escolha, o usuário terá acesso ao menu de gerenciamento de estoque ou ao menu de compras.

Requisitos:
Python 3.x instalado

Arquivos de login e produtos configurados corretamente
