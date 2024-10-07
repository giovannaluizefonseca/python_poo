class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        print(f"O item {self._titulo} do autor(a) {self._autor} foi publicado em {self._anoPublicacao} e tem {self._numeroPagina} páginas.")

    def calcularIdadeItem(self, ano_atual):
        idade = ano_atual - self._anoPublicacao
        if idade > 70:
            print(f"O item {self._titulo} é do ano {self._anoPublicacao}, tem idade de {idade} anos e é muito antigo.")
        elif 30 <= idade <= 70:
            print(f"O item {self._titulo} é do ano {self._anoPublicacao}, tem idade de {idade} anos e é recente.")
        else:
            print(f"O item {self._titulo} é do ano {self._anoPublicacao}, tem idade de {idade} anos e é contemporâneo.")


class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina > 300:
            print(f"O livro {self._titulo} tem {self._numeroPagina} páginas e é longo.")
        else:
            print(f"O livro {self._titulo} tem {self._numeroPagina} páginas e é curto.")


class Revista(Biblioteca):
    def verificarEdicao(self):
        if self._anoPublicacao < 1998:
            print(f"A revista {self._titulo} é de {self._anoPublicacao} e é uma edição especial.")
        else:
            print(f"A revista {self._titulo} é de {self._anoPublicacao} e não é uma edição especial.")
