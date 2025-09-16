#  Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente. Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

nome_Acesso = 'admin'
senha_Acesso = '12345'


print("===== Bem Vindo ao Sistema =====\n")
while True:
    print("      Menu:      ")
    resposta = input(" 1. Fazer Login \n 2. Sair \n Escolha uma opção: ")
    
    if resposta == "1":
        for tentativas in range(3, 0, -1):
            usuario_Acesso = input("Digite o Nome de Acesso: ")
            senha_Usuario = input("Digite a senha de Acesso: ")
            if usuario_Acesso == nome_Acesso and senha_Usuario == senha_Acesso:
                print("\nBoas vindas ao sistema!!!\n")
                break
        
            elif usuario_Acesso != nome_Acesso or senha_Usuario != senha_Acesso:
                print(f'\nO login está incorreto! Você tem {tentativas - 1} tentativas restantes\n')
                tentativas -= 1
        else:
            for acesso in range(1,4):
                print("Acesso Bloqueado")
            print("\nVocê ultrapassou o limite de tentativas. Voltando para o Menu. . .\n")
            continue
        break   
     
    elif resposta == "2":
        print("Encerrando o programa. . .")
        break
    else:
        print("Opção inválida! Tente novamente.")
    
    

