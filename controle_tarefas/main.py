from tarefa import Tarefa
from servicos import Cadastrar, Listar, Atualisar,Dellete

registros = []
while True:
    print("\n registros")
    print("1- Cadastrar")
    print("2- listar")
    print("3-Atualisar")
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
        

# para testar este, descomente este trexo e a class tarefa

# from tarefa import Tarefa
# from servicos import cadastrar_tarefa, filtrar_por_situacao, listar_tarefas, ler_dados_tarefa

# tarefas = []
# cadastrar_tarefa(
#     tarefas,
#     "Revisar chamados",
#     "Verificar chamados pendentes da equipe",
#     "Alta",
#     Tarefa,
# )
# cadastrar_tarefa(
#     tarefas,
#     "Atualizar manual interno",
#     "Ajustar instruções de atendimento",
#     "Média",
#     Tarefa,
# )
# cadastrar_tarefa(
#     tarefas,
#     "Planejar reunião",
#     "Preparar pauta da reunião semanal",
#     "Baixa",
#     Tarefa,
# )
# # Demonstração da mudança de estado.
# tarefas[0].concluir()
# print("Todas as tarefas:")
# listar_tarefas(tarefas)
# print("\nTarefas concluídas:")
# tarefas_concluidas = filtrar_por_situacao(tarefas, "Concluída")
# listar_tarefas(tarefas_concluidas)
# titulo, descricao, prioridade = ler_dados_tarefa()