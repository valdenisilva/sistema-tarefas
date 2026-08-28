chamadas = []
chamado_1 = {
    "id": 1,
    "titulo": "computador nao iniciado",
    "situacao": "aberto",
    "responsavel": "juao"
}

print(type(chamado_1))

chamado_2 = {
    "id": 2,
    "situacoa": "em andamento",
    "responsavel": "maria"
}

chamado_3 = {
    "id": 3,
    "situacao": "",
    "responsavel": "antonio",
    "urgente": False
}

lista = [chamado_1, chamado_2]
print(type(chamado_1))

tarefas = []
proximo_id = 1

while True:
    print()
    print("menu")
    opcao = input("escolha uma opcao ")

    if opcao == "1":
        print()
        print("cadastro de tarefas")

        titulo = input("titulo: ").strip()
        if titulo == "":
            print("O titulo deve ser preenchido")
        else:
            prioridade = input("prioridade (baixa, media ou alta):").lower()
            if prioridade != "baixa" and prioridade != "media" and prioridade != "alta":
                print("prioridade einvalida")
            else:
                categoria = input("categoria da tarefa: ").strip().lower()
                prazo_horas = float(input("prazo estimado em horas: "))

                resposta_urgente = input("urgent (sin/nao)").lower()
                urgente = resposta_urgente == "sim"
                esforco = 1.5
                esforco_estimado = (prazo_horas * esforco)
                prioridade_alta = prioridade == "alta"
                "prioridade = prioridade_alta or urgente"

                tarefa = {
                    "id": proximo_id,
                    "titulo": titulo,
                    "prioridade": prioridade,
                    "categoria": categoria,
                    "prazo": prazo_horas,
                    "esforco": esforco_estimado,
                    "urgente": urgente,
                    "prioridade": prioridade,
                    "situacao": "pendente"
                }

                tarefas.append(tarefa)
                print(f"tarefa {proximo_id} cadastrado com sucesso")

                proximo_id = proximo_id + 1
    elif opcao == "2":
                print()
                print("lista de tarefas")
                if len(tarefas) == 0:
                    print("nenhuma tarefa encontrada")
                else:
                    for tarefa in tarefas:
                        print()
                        print(f"id: {tarefa["id"]}")
                        print(f"titulo: {tarefa["titulo"]}")
                        print(f"prioridade: {tarefa["prioridade"]}")
                        print(f"categoria: {tarefa["categoria"]}")
                        print(f"situacao: {tarefa["situacao"]}")

                        print(f"prazo: {tarefa["prazo"]:.2f} horas")
                        print(f"esforco estimado: {tarefa["esforco"]:.2f} horas")
                        print(f"urgent: {tarefa["urgente"]}")
                        print(f"prioridade: {tarefa["prioridade"]}")

                        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
    elif opcao == "3":
        situacao_desejada = input("situacao desejada: ").strip().lower()
        encontrou_tarefa = False
        for tarefa in tarefas:
            if tarefa["situacao"] == situacao_desejada:
                print()
                print(f"id: {tarefa["id"]}")
                print(f"titulo: {tarefa["titulo"]}")
                print(f"prioridade: {tarefa["prioridade"]}")
                print(f"categoria: {tarefa["categoria"]}")

                encontrou_tarefa = True
            if encontrou_tarefa == False:
                print("tarefa nao encontrada")

    elif opcao == "4":
        numero = input("informe o id da tarefa que deseja: ")
        if numero.isdigit():
            id_situacao =int(numero)
            nova_situacao = input("nova situacao: ").strip().lower()
#####
            id_procurado = True
        for tarefa in tarefas:
            if tarefa["id"] == id_procurado:
                tarefa["situacao"] = nova_situacao
                encontrou_tarefa = True
                print("situacao atualisada com sucesso")
                break
            if encontrou_tarefa == False:
                print("A tarefa nao foi encontrada")                        
            else:
                print("id invalido tente novamente")
    elif opcao == "5":
        categorias = set()
        for tarefa in tarefas:
            categorias.add(tarefa["categoria"])
        print()
        print("categorias")
        if len(categorias) == 0:
            print("nenhuma categoria foi encontrada")
        else:
            for categoria in categorias:
                print(f"{categoria}")
    elif opcao == "6":
        print()
        print("O sistema foi ncerrado")
        break
    else:
        print("Opcao invalida tente outra opcao")

        

