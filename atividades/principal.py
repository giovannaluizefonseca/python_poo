from livro import Livro

#Criando os objetos
p1 = Livro("As vantagens de ser invisível", "Stephen Chbosky", 1999)
p2 = Livro("Harry Potter e o Cálice de Fogo", "J.K. Rowling", 2000)
p3 = Livro("O retrato de Dorian Grey", "Oscar Wilde", 1890)


ano_atual = 2024
p1.exibirInformacoes()
p1.verificaridadeLivro(ano_atual)

print("="*50)

p2.exibirInformacoes()
p2.verificaridadeLivro(ano_atual)

print("="*50)

p3.exibirInformacoes()
p3.verificaridadeLivro(ano_atual)