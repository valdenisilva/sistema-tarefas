tarefas = []
def Cadastrar_tarefa(tarefas):
#     {
# "titulo": titulo,
# "prioridade": prioridade,
# "situacao": "pendente"
# }
    titulo = input("Digite o titulo da tarefa ")
    tarefas.append(titulo)
    print("tarefa cadastrada com sucesso")

def Listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("nenhuma tarefa cadastrada!")
    else:
        print("\n tarefa cadastrada com sucesso")
        for i in range(len(tarefas)):
            print(i+1, " ", tarefas[i])

def Atualizar_situação_tarefa(tarefas):
    indice = int(input("digite o indce que deseja atualizar ")) -1 
    if indice >= 0 and indice < len(tarefas):
        nova_tarefa = input("digite a nova tarefa ")
        tarefas[indice] = nova_tarefa
        print("tarefa concluida")
    else:
        print("tarefa inexistente")
        
while True:
    print("tarefas")
    print("1:cadastrar")
    print("2:listar")
    print("3: atualizar")
    print("4: sair")
    opcao = input("Escolha uma opcao ")

    if opcao == '1':
        Cadastrar_tarefa(tarefas)
    elif opcao =='2':
        Listar_tarefas(tarefas)
    elif opcao == '3':
        Atualizar_situação_tarefa(tarefas)
    elif opcao == '4':
        print('Encerrar_sistema...')
        break
    else:
        print("Opcao invalida, escolha outro numero")




