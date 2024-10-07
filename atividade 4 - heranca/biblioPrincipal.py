from biblioteca import Biblioteca, Livro, Revista

ano_atual = 2024

a1 = Biblioteca("1984", "George Orwell", 1949, 416)
p1 = Livro("1984", "George Orwell", 1949, 416)

a1.detalhes()

p1.calcularIdadeItem(ano_atual)
p1.verificarTamanho()

print("="*50)

a2 = Biblioteca("Revista Veja", "Roberto Civita", 1968, 120)
p2 = Revista("Revista Veja", "Roberto Civita", 1968, 120)

a2.detalhes()

p2.calcularIdadeItem(ano_atual)
p2.verificarEdicao()