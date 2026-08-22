registros = []
while True:
    print("\n registros")
    print("1- cadastrar")
    print("2- listar")
    print("3-atualizar")
    print("4- sair")

    opcao = input("Escolha uma opcao")

    if opcao == "1":
        nome = input("Digite o nome a ser cadastrado")
        registros.append(nome)
        print("Registro efetuado com sucesso!")
    elif opcao == "2":
        if len(registros) == 0:
            print("\n nao a registros cadastrados")
        else:
            print("\n Registros cadastrados")
            for i in range(len(registros)):
                print(i, " ", registros [i])

    elif opcao =="3":
        if len(registros) == 0:
            print("nenhum registro disponivel para atualizacao")
        else:
            print("\n registros cadastrados")
            for i in range(len(registros)):
                print(i," ", registros[i] )
            indice = int(input("digite o numero do registro que deseja atualizar"))
            if indice >= 0 and indice< len(registros):
                novo_nome = input("Digite o novo nome:")
                registros[indice] = novo_nome
                print("Registro atualizado com sucesso!")
            else:
                print("Registro invalido!")

    elif opcao == "4":
        print("Encerrando o sistema")
        break
    else:
        print("opcao invalida, tente novamente")

registros = []

def Cadastrar(registros):
    nome = input("Digite o nome para ser cadastrado ")
    registros.append(nome)
    print("Registros cadastrados com sucesso!")

def Listar(registros):
    if len(registros) == 0:
        print("nenhum registro cadastrado!")
    else:
        print("\n Registro cadastrado!")
def Listar(registros):
    if len(registros) == 0:
        print("nenhum registro cadastrado.")
    else:
        print("\n registro cadastrado.")
        for i in range(len(registros)):
            print(i, " ", registros[i])
def Atualisar(registros):
    indice = int(input("digite o indice para atualizar "))
    if indice >= 0 and indice < len(registros):
        novo_nome = input("digite o novo nome ")
        registros[indice] = novo_nome 
        print("registro foi atualizado!")
    else: 
        print("indice invalido")
def Dellete(registros):
    if len(registros) == 0:
        print("registro nao encontrado!")
    else:
        indice = int(input("digite o indice que deseja remover "))
        if 0 <= indice < len(registros):
            registros = registros.pop(indice)
            print("registro removido com sucesso")
        else:
            print("indice invalido")



        

while True:
    print("\n registros")
    print("1- cadastrar")
    print("2- listar")
    print("3-atualizar")
    print("4-Dellete")
    print("5- sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        Cadastrar(registros)
    elif opcao == "2":
        Listar(registros)
    elif opcao == "3":
        Atualisar(registros)
    elif opcao == "4":
        Dellete(registros)
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")
