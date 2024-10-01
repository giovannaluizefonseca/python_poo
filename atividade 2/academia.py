class Aluno:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def exibirDados(self):
        print(f"O(A) aluno(a) {self.nome} de {self.idade} anos pesa {self.peso}kg e sua altura é {self.altura} metros.")

    def calcularImc(self):
        imc = self.peso/self.altura**2
        print(f"O Índice de Massa Corporal do(a) aluno(a) é {imc:.2f}")