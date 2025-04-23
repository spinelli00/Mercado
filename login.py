def telalogin(): # Exibe a tela para o usuário fazer login
    usuario = input("Digite o usuário >> ").strip()
    senha = input("Digite a senha >> ").strip()
    login_digitado = f"{usuario},{senha}"

    try:
        with open('C:\\Users\\patri\\Desktop\\Projeto mercadinho\\loginpermitidos.txt', 'r', encoding='utf-8') as loginspermitidos:
            logins = loginspermitidos.readlines()

        if login_digitado in logins:
            print("Login permitido! Indo para menu de usuario ... .")
            return True
        else:
            print("Login ou senha incorretos!")
            return False
    except FileNotFoundError:
        print("Arquivo de logins não encontrado!")
        return False
