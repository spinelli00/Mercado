def menu_nao_logado():
    while True:
        print("\nMenu - Acesso sem login:")
        print("1. Visualizar produtos")
        print("2. Adicionar produtos ao carrinho")
        print("3. Voltar ao menu principal")
        escolha = input("Selecione uma opção (1, 2 ou 3) >> ").strip()

        if escolha == '1':
            visualizar_produtos()  # Exibe a lista de produtos
        elif escolha == '2':
            adicionar_carrinho()  # Adiciona produtos ao carrinho
        elif escolha == '3':
            print("Saindo para o menu principal...")
            return  # Retorna ao menu principal, quebrando o loop
        else:
            print("Opção inválida! Tente novamente.")


def visualizar_produtos():
    try:
        with open('C:\\Users\\patri\\Desktop\\Projeto mercadinho\\produtos.txt', 'r', encoding='utf-8') as produtos_arquivo:
            produtos = produtos_arquivo.readlines()

        if produtos:
            print("\nLista de produtos no estoque:")
            for produto in produtos:
                print(produto.strip())
        else:
            print("O estoque está vazio.")
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado!")

def adicionar_carrinho():
    produtos_disponiveis = ['Produto 1 - R$10', 'Produto 2 - R$20', 'Produto 3 - R$30']
    carrinho = []
    print("Produtos disponíveis: ")
    for idx, produto in enumerate(produtos_disponiveis, 1):
        print(f"{idx}. {produto}")

    while True:
        try:
            escolha = int(input("Escolha um produto para adicionar ao carrinho (0 para finalizar) >> "))
            if escolha == 0:
                break
            elif 1 <= escolha <= len(produtos_disponiveis):
                carrinho.append(produtos_disponiveis[escolha - 1])
                print(f"Produto {produtos_disponiveis[escolha - 1]} adicionado ao carrinho!")
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    print("\nItens no carrinho:")
    if carrinho:
        for item in carrinho:
            print(item)
    else:
        print("Nenhum item foi adicionado ao carrinho.")
