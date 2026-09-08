class Tarefa:
    def __init__(self, indice, nome, idade):
        self.nome = nome
        self.indice = indice
        self.idade = idade
        def Cadastrar(registros):
            self.nome = nome
            self.idade = idade
            # pass
        def Listar(registros):
            return(
                f"nome: {self.nome, self.idade}"
            )
            # pass
        def Atualisar(registros):
            
            pass
        def Dellete(registros):
            pass
        

# este trexo fas parte do trecho comentado em servicos.py

# class Tarefa:
#     def __init__(self, titulo, descricao, prioridade):
#         self.titulo = titulo
#         self.descricao = descricao
#         self.prioridade = prioridade
#         self.situacao = "Pendente"
#     def concluir(self):
#         self.situacao = "Concluída"
#     def exibir_resumo(self):
#         return (
#         f"Título: {self.titulo} | "
#         f"Prioridade: {self.prioridade} | "
#         f"Situação: {self.situacao}"
# )