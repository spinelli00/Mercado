from logado import menucomlogin
from naologado import menu_nao_logado
from login import telalogin
# Verficar se o usuário deseja fazer login ou não 

def menu_principal():
    while True:
        print("\nBem-vindo ao Mercadinho!")
        print("1. Fazer login")
        print("2. Seguir sem login")
        escolha = input("Selecione uma opção (1 ou 2) >> ").strip()

        if escolha == '1':
            if telalogin():  # Chama o login, se for bem-sucedido, entra no menu logado
                menucomlogin()  # Menu para usuário logado
                break
        elif escolha == '2':
            menu_nao_logado()  # Menu para usuário não logado
            break
        else:
            print("Opção inválida! Tente novamente.")

menu_principal()
