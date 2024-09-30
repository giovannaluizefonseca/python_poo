class Livro:
    #Método construtor
    def __init__(self, titulo, autor, anopublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anopublicacao = anopublicacao

    def exibirInformacoes(self):
        print(f"O livro {self.titulo} do autor(a) {self.autor} foi publicado em {self.anopublicacao}.")

    def verificaridadeLivro(self, ano_atual):
        idade = ano_atual - self.anopublicacao
        if idade > 50:
            print("O livro é um clássico!")
        else:
            print("O livro ainda não é considerado um clássico.")
