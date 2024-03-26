class Tarefa:
    def __init__(self, descricao, concluida=False):
        self.descricao = descricao
        self.concluida = concluida

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        self.tarefas.append(Tarefa(descricao))
        print(f"Tarefa '{descricao}' adicionada com sucesso!")

    def listar_tarefas(self):
        if self.tarefas:
            print("Tarefas:")
            for idx, tarefa in enumerate(self.tarefas, start=1):
                status = "Concluída" if tarefa.concluida else "Pendente"
                print(f"{idx}. [{status}] {tarefa.descricao}")
        else:
            print("Nenhuma tarefa encontrada.")

    def marcar_concluida(self, numero_tarefa):
        if 1 <= numero_tarefa <= len(self.tarefas):
            self.tarefas[numero_tarefa - 1].concluida = True
            print("Tarefa marcada como concluída!")
        else:
            print("Tarefa não encontrada.")

def main():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            gerenciador.adicionar_tarefa(descricao)
        elif opcao == "2":
            gerenciador.listar_tarefas()
        elif opcao == "3":
            numero_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            gerenciador.marcar_concluida(numero_tarefa)
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()