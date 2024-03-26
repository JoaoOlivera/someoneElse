class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada!")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida}' removida!")
        else:
            print("Índice inválido. Tarefa não encontrada.")

    def visualizar_tarefas(self):
        if self.tarefas:
            print("Tarefas:")
            for idx, tarefa in enumerate(self.tarefas):
                print(f"{idx}. {tarefa}")
        else:
            print("Nenhuma tarefa na lista.")

def main():
    lista_tarefas = ListaDeTarefas()

    while True:
        print("\n=== Lista de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Visualizar Tarefas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            lista_tarefas.adicionar_tarefa(tarefa)
        elif opcao == "2":
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            lista_tarefas.remover_tarefa(indice)
        elif opcao == "3":
            lista_tarefas.visualizar_tarefas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()