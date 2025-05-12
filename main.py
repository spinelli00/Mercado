from logado import menucomlogin
from naologado import menu_nao_logado
from login import telalogin

def menu_principal():
    while True:
        print("----------------------------")
        print("\n| Bem-vindo ao Mercadinho! |")
        print("\n----------------------------")
        print("1. Acessar menu de administrador")
        print("2. Acessar menu de usuário")
        escolha = input("Selecione uma opção (1 ou 2) >> ").strip()

        if escolha == '1':
            if telalogin():  
                menucomlogin()  
                break
        elif escolha == '2':
            menu_nao_logado() 
            break
        else:
            print("Opção inválida! Tente novamente.")

menu_principal()
