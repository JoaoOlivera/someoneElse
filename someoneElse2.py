class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))
        print(f"Livro '{titulo}' adicionado à biblioteca!")

    def listar_livros(self):
        if self.livros:
            print("Livros disponíveis na biblioteca:")
            for idx, livro in enumerate(self.livros, start=1):
                status = "Disponível" if livro.disponivel else "Emprestado"
                print(f"{idx}. '{livro.titulo}' por {livro.autor} [{status}]")
        else:
            print("Nenhum livro encontrado na biblioteca.")

    def emprestar_livro(self, numero_livro):
        if 1 <= numero_livro <= len(self.livros):
            livro = self.livros[numero_livro - 1]
            if livro.disponivel:
                livro.disponivel = False
                print(f"Livro '{livro.titulo}' emprestado com sucesso!")
            else:
                print("Este livro já está emprestado.")
        else:
            print("Livro não encontrado.")

    def devolver_livro(self, numero_livro):
        if 1 <= numero_livro <= len(self.livros):
            livro = self.livros[numero_livro - 1]
            if not livro.disponivel:
                livro.disponivel = True
                print(f"Livro '{livro.titulo}' devolvido com sucesso!")
            else:
                print("Este livro já está disponível na biblioteca.")
        else:
            print("Livro não encontrado.")

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== Sistema de Gerenciamento de Biblioteca ===")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            biblioteca.adicionar_livro(titulo, autor)
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            numero_livro = int(input("Digite o número do livro a ser emprestado: "))
            biblioteca.emprestar_livro(numero_livro)
        elif opcao == "4":
            numero_livro = int(input("Digite o número do livro a ser devolvido: "))
            biblioteca.devolver_livro(numero_livro)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()