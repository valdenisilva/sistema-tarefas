def Cadastrar(registros):
    nome = input("Digite o nome para ser cadastrado ")
    idade = int(input("Digite a idade a ser cadastrada"))
    registros.append([nome, idade])
    print("Registros cadastrados com sucesso!")

def Listar(registros):
    # if not (registros):
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
        nova_idade = int(input("digite a nova idade"))
        registros[indice] = [novo_nome, nova_idade]
        print("registro foi atualizado!")
    else: 
        print("indice invalido")
def Dellete(registros):
    if len(registros) == 0:
        print("registro nao encontrado!")
    else:
        indice = int(input("digite o indice que deseja remover "))
        if 0 <= indice < len(registros):
            registros.pop(indice)
            print("registro removido com sucesso")
        else:
            print("indice invalido")
            

# faz parte dos codigos comentados na class e no servico.py

# def cadastrar_tarefa(tarefas, titulo, descricao, prioridade, classe_tarefa):
#     nova_tarefa = classe_tarefa(titulo, descricao, prioridade)
#     tarefas.append(nova_tarefa)
#     return nova_tarefa

# def listar_tarefas(tarefas):
#     if not tarefas:
#         print("Nenhuma tarefa cadastrada.")
#         return
#     for indice, tarefa in enumerate(tarefas, start=1):
#         print(f"{indice}. {tarefa.exibir_resumo()}")
# def filtrar_por_situacao(tarefas, situacao):
#     return [tarefa for tarefa in tarefas if tarefa.situacao == situacao]

# def ler_dados_tarefa():
#     titulo = input("Título: ")
#     descricao = input("Descrição: ")
#     prioridade = input("Prioridade: ")
#     return titulo, descricao, prioridade