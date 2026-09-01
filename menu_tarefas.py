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
        print("/n tarefa cadastrada com sucesso")
        for i in range(len(tarefas)):
            print(i, " ", tarefas[i])

def Atualizar_situação_tarefa(tarefas):
    indce = int(input("digite o indce que deseja atualizar "))
    indce = -1 
    if indce >= 0 and indce < len(tarefas) -1:
        nova_tarefa = input("digite a nova tarefa ")
        tarefas[indce] = nova_tarefa
        print("tarefa concruida")
    else:
        print("tarefa inesistente")
        
while True:
    print("tarefas")
    print("1,cadastrar")
    print("2,listar")
    print("3, atualizar")
    print("4, sair")
    opcao = input("Escolha uma opcao ")

    if opcao == '1':
        Cadastrar_tarefa(tarefas)
    if opcao =='2':
        Listar_tarefas(tarefas)
    if opcao == '3':
        Atualizar_situação_tarefa(tarefas)
    if opcao == '4':
        print('Encerrar_sistema...')
        break
    else:
        print("Opcao invalida, escolha outro numero")




