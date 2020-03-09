import random


class Ambiente:
    def __init__(self):
        # Instanciando locais e condições dos locais.
        # 0 indica que o local está limpo e 1 indica que está sujo.
        self.locais = {'A': '0', 'B': '0'}
        # Sujando um dos locais aleatoriamente.
        self.locais['A'] = random.randint(0, 1)
        self.locais['B'] = random.randint(0, 1)


class AgenteAspirador(Ambiente):
    def __init__(self, posicaoAgente, Ambiente):
        # 0 indica a posição A, 1 indica posição B.
        self.posicaoAgente = posicaoAgente
        # '~' indica sujeira, '#' indica limpo.
        print("Mapa do local: ")
        for pos in Ambiente.locais:
            if(Ambiente.locais[pos] == 0):
                print('#', end='')
            elif(Ambiente.locais[pos] == 1):
                print('~', end='')
        print()

        # Existem 2 posições. O objetivo do agente é de deixar o ambiente completamente limpo e ter conhecimento disso.
        # Ele apenas deixa sua posição atual se ela estiver limpa.
        # Após limpar completamente o ambiente, seu trabalho termina.
        self.limpeza = 0
        while(self.limpeza < 2):
            if(self.posicaoAgente == 0):
                print("\nAgente está em A.")
                if(Ambiente.locais['A'] == 0):
                    print("A está limpo.")
                    self.posicaoAgente = 1
                    self.limpeza += 1
                elif(Ambiente.locais['A'] == 1):
                    print("A está sujo.")
                    print("Limpando A...")
                    Ambiente.locais['A'] = 0
                    self.posicaoAgente = 1
                    self.limpeza += 1
            elif(self.posicaoAgente == 1):
                print("\nAgente está em B.")
                if(Ambiente.locais['B'] == 0):
                    print("B está limpo.")
                    self.posicaoAgente = 0
                    self.limpeza += 1
                elif(Ambiente.locais['B'] == 1):
                    print("B está sujo.")
                    print("Limpando B...")
                    Ambiente.locais['B'] = 0
                    self.posicaoAgente = 0
                    self.limpeza += 1
            if(self.limpeza < 2):
                if(self.posicaoAgente == 0):
                    print("Indo para A...")
                else:
                    print("Indo para B...")
            elif(self.limpeza == 2):
                print("\nLimpeza concluída.")


ambiente = Ambiente()
aspirador = AgenteAspirador(random.randint(0, 1), ambiente)
