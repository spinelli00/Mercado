CAMINHO_PRODUTOS = "C:\\Users\\patri\\Desktop\\Projeto mercadinho\\produtos.txt"

def adicionaritens():
    while True:
        nomedoproduto = input("Digite o nome do produto >> ").title()
        try:
            quantidade = int(input("Digite quantos possui para adicionar ao estoque >> "))
            preco = float(input("Digite o preço de cada unidade do produto >> "))
        except ValueError:
            print("Erro nos dados inseridos. Tente novamente!")
            continue

        linha = f"{nomedoproduto},{quantidade},{preco:.2f}\n"

        try:
            with open(CAMINHO_PRODUTOS, "a", encoding="utf-8") as arquivo:
                arquivo.write(linha)
            print(f"Produto '{nomedoproduto}' adicionado com sucesso ao estoque!")
            break
        except Exception as e:
            print("Erro ao salvar o produto:", e)
            break

def removeritens():
    try:
        with open(CAMINHO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("O estoque está vazio!")
            return

        nome_remover = input("Digite o nome do produto que deseja remover >> ").title()
        nova_lista = [linha for linha in linhas if not linha.startswith(nome_remover + ",")]

        if len(nova_lista) == len(linhas):
            print(f"O produto '{nome_remover}' não foi encontrado no estoque.")
        else:
            with open(CAMINHO_PRODUTOS, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(nova_lista)
            print(f"Produto '{nome_remover}' removido com sucesso.")
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado.")

def listaritens():
    try:
        with open(CAMINHO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("O estoque está vazio.")
            return

        print("\nEstoque atual:")
        for linha in linhas:
            nome, quantidade, preco = linha.strip().split(",")
            print(f"- {nome}: {quantidade} unidades | R$ {preco}")
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado.")


def menucomlogin(): # Exibe o menu de opções para os usuarios que possuem login
    while True:
        try:
            print("\nMenu:")
            print("1. Adicionar itens ao estoque")
            print("2. Remover item do estoque")
            print("3. Listar itens do estoque")
            print("4. Sair")

            opcao = int(input("Selecione uma opção >> "))

            if opcao == 1:
                adicionaritens()
            elif opcao == 2:
                removeritens()
            elif opcao == 3:
                listaritens()
            elif opcao == 4:
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

        except ValueError:
            print("Por favor, digite um número válido!")
