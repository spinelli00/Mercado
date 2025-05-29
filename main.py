from logado import menucomlogin
from naologado import menu_nao_logado
from login import telalogin

def menu_principal():
    try :
        while True:
            print("----------------------------")
            print("\n| Bem-vindo ao Mercadinho! |")
            print("\n----------------------------")
            print("1. Acessar menu de administrador")
            print("2. Acessar menu de usuário")
            escolha = input("Selecione uma opção (1 ou 2) >> ").strip()

            match escolha:
                case '1':
                    if telalogin():  
                        menucomlogin()  
                        break
                case '2':
                    menu_nao_logado() 
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
    except ValueError :
        print("Opção inválida! Tente novamente.")


if __name__ == '__main__' :
    menu_principal()
