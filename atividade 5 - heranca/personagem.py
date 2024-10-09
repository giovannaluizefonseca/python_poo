class Personagem:
    def __init__(self, nome, vida, rank):
        self._nome = nome
        self._vida = vida
        self._rank = rank

    def receberDano(self, dano):
        self._vida -= dano
        print(f"{self._nome} recebeu {dano} de dano.")

    def verificarVida(self):
        if self._vida > 0:
            print(f"{self._nome} ainda está vivo e tem {self._vida} pontos de vida.")
        else:
            print(f"{self._nome} está morto!")

    def detalhes(self):
        print(f"Nome: {self._nome}, Vida: {self._vida}, Rank: {self._rank}")

class Heroi(Personagem):
    def __init__(self, nome, vida, rank, identidadeSecreta, energia):
        super().__init__(nome, vida, rank)
        self._identidadeSecreta = identidadeSecreta
        self._energia = energia
    
    def mostrarIdentidadeSecreta(self, identidadeSecreta):
        self._identidadeSecreta = identidadeSecreta
        print(f"{self._nome} tem sua identidade secreta de {identidadeSecreta}.")
    
    def executarHabilidade(self, tipoHabilidade, energiaConsumida):
        if self._energia >= energiaConsumida:
            self._energia -= energiaConsumida
            print(f"{self._nome} usou a habilidade {tipoHabilidade} e consumiu {energiaConsumida} de energia.")
        else:
            print(f"{self._nome} não tem energia suficiente para usar {tipoHabilidade}.")

    def recarregarEnergia(self, energiaRecuperada):  
        self._energia += energiaRecuperada
        print(f"{self._nome} recarregou {energiaRecuperada} de energia.")

    def mostrarEnergia(self):
        print(f"{self._nome} agora tem {self._energia} de energia.")

class Vilao(Personagem):
    def __init__(self, nome, malicia, vida, rank):
        super().__init__(nome, vida, rank)
        self._malicia = malicia

    def desferirGolpe(self, tipoGolpe, maliciaConsumida):  
        if self._malicia >= maliciaConsumida:
            self._malicia -= maliciaConsumida
            print(f"{self._nome} desferiu o golpe {tipoGolpe}, potencializado por {maliciaConsumida} de malícia.")
        else:
            print(f"{self._nome} não tem malícia suficiente para desferir o golpe {tipoGolpe}.")
    
    def planejarArmadilha(self, tipoArmadilha):
        print(f"{self._nome} está planejando uma armadilha: {tipoArmadilha}.")

    def mostrarMalicia(self):
        print(f"{self._nome} agora tem {self._malicia} de malícia.")
