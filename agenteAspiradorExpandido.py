import random


class Ambiente:
    def __init__(self, locais):
        # Instanciando locais e condições dos locais.
        # 0 indica que o local está limpo e 1 indica que está sujo.
        self.locais = locais
        # Sujando um dos locais aleatoriamente.
        for local in self.locais:
            self.locais[local] = random.randint(0, 1)


class AgenteAspirador(Ambiente):
    def __init__(self, posicaoAgente, Ambiente):
        # 0 indica a posição A, 1 indica posição B.
        self.posicaoAgente = posicaoAgente
        
        if(int(len(Ambiente.locais)/2) > self.posicaoAgente or self.posicaoAgente == len(Ambiente.locais)-1):
            for i in range(self.posicaoAgente, -1, -1): # -1 = 0 na posicao
                self.posicaoAgente = i
                self.Mapa(Ambiente)
        elif(int(self.posicaoAgente != 7 or len(Ambiente.locais)/2) <= self.posicaoAgente or self.posicaoAgente == 0):
            for i in range(self.posicaoAgente, len(Ambiente.locais), 1):
                self.posicaoAgente = i
                self.Mapa(Ambiente)

    def Mapa(self, Ambiente):
        # '~' indica sujeira, '#' indica limpo.
        print( self.posicaoAgente)
        for index, pos in enumerate(Ambiente.locais):
            if(self.posicaoAgente == index):
                print('^ ', end='')
            elif(Ambiente.locais[pos] == 0):
                print('# ', end='')
            elif(Ambiente.locais[pos] == 1):
                print('~ ', end='')
        print()




locais = {'A': '0', 'B': '0', 'C': '0', 'D': '0', 'E': '0', 'F': '0', 'G': '0'}
ambiente = Ambiente(locais)
aspirador = AgenteAspirador(random.randint(0, len(ambiente.locais) - 1), ambiente)
