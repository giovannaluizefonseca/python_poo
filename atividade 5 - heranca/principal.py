from personagem import Personagem, Heroi, Vilao

personagem1 = Personagem("Valentina Vortex", 100, "Intermediário")
heroi1 = Heroi("Sombra Luminosa", 100, "Novato", "Giovanna Fonseca", 50)
vilao1 = Vilao("Rainha do Terror", 70, 100, "Lendário")

personagem1.receberDano(10)
personagem1.verificarVida()
personagem1.detalhes()

print("="*60)

heroi1.mostrarIdentidadeSecreta("Giovanna Fonseca")
heroi1.executarHabilidade("Raio Laser", 10) # Raio Laser é a habilidade e 10 é a energiaConsumida
heroi1.recarregarEnergia(20) # 20 é a energiaRecuperada
heroi1.mostrarEnergia()
heroi1.detalhes()

print("="*60)

vilao1.desferirGolpe("Soco Forte", 15)
vilao1.planejarArmadilha("Armadilha para urso")
vilao1.mostrarMalicia()
vilao1.detalhes()
