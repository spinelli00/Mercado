# PyCommerce
Sistema de Gerenciamento de Estoque e Carrinho de Compras

Este é um sistema de gerenciamento de mercadinho, desenvolvido em Python. O projeto visa proporcionar uma interface interativa para a gestão de um estoque de produtos e o carrinho de compras de clientes. O sistema possui duas formas de acesso: com login (para usuários administrativos com login predefinido) e sem login (para usuários comuns).

Funcionalidades principais:
Login de Usuário: Permite que usuários administrativos façam login para acessar funcionalidades exclusivas, como adicionar e remover itens do estoque.

Menu para Usuários Não Logados: Usuários sem login podem visualizar os produtos disponíveis no estoque e adicionar itens ao carrinho de compras.

Gerenciamento de Estoque: O sistema permite adicionar, remover e listar produtos no estoque. As alterações são armazenadas em arquivos locais.

Carrinho de Compras: Usuários podem adicionar itens ao carrinho, mas não têm permissão para modificar o estoque sem login.

Tecnologias Utilizadas:
Python 3.11

Arquivos de texto (.txt) para armazenamento de produtos listados

Arquivo Pickle para codificar os logins permitidos (loginpermitidos.pickle)

Estrutura simples de menus para interação com o usuário

Como usar:
Execute o script main.py.

O programa pedirá para o usuário escolher entre fazer login ou seguir sem login.

No caso de login, o sistema valida as credenciais em um arquivo loginpermitidos.pickle.

Caso o usuario possua o login será concedida a permissão de adicionar items itens to estoque, remover itens do estoque e listar os itens presentes no estoque

Caso não o usuário poderá visualizar os produtos disponiveis no estoque e adicionar itens ao seu carrinho de compra

Requisitos:
Python 3.11 instalado

Arquivos de login e produtos configurados corretamente
