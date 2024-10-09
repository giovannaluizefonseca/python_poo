from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Garibald", 54)
aluno1 = Aluno("Juciclea", 16, 987)
prof1 = Professor("Ana", 35, "Matemática")

pessoa1.info()

aluno1.info()
aluno1.estudar()

prof1.info()
prof1.ensinar()