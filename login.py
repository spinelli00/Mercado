import pickle
from utils import cleardisplay



def telalogin():
    usuario = input("Digite o usuário >> ").strip()
    senha = input("Digite a senha >> ").strip()
    login_digitado = f"{usuario},{senha}"

    try:
        with open('C:\\Users\\patri\\Desktop\\Projeto mercadinho\\loginpermitidos.pickle', 'rb') as loginspermitidos:
            logins = pickle.load(loginspermitidos)

        if login_digitado in logins:
            print("Login permitido! Indo para menu de usuario ...")
            cleardisplay()
            return True
        else:
            print("Login ou senha incorretos, Voltando ao menu principal !")
            cleardisplay()
            return False
            
    except FileNotFoundError:
        print("Arquivo de logins não encontrado, Voltando ao menu principal !")
        cleardisplay()
        return False
        
        
