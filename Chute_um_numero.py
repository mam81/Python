# Projeto: Chute um número
# Objetivo: Criar um algoritmo que gera um valor aleatório e eu tenho que ficar tentando o número até acertar

import random

class ChuteNumero:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentativas = 0
        self.tentar_novamente = True

    def Iniciar(self):
        self.GeradorNumero()
        self.PedirNumeroAleatorio()

        while self.tentar_novamente:

            try:

                self.tentativas += 1
            
                if int(self.valor_chute) > self.valor_aleatorio:
                    print('- Número muito alto!! - Chute um número menor(de 1 a 100)')
                    self.PedirNumeroAleatorio()
                    

                elif int(self.valor_chute) < self.valor_aleatorio:
                    print('- Número muito baixo!! -Chute um valor maior(de 1 a 100)')
                    self.PedirNumeroAleatorio()

                else:
                    self.tentar_novamente = False
                    print(f'Parabéns, você acertou o número {self.valor_aleatorio} com um total de {self.tentativas} tentativa(s)')

            except:
                print('Favor digitar apenas números!')
                self.Iniciar()

    def PedirNumeroAleatorio(self):
        self.valor_chute = input(f'Chute um número(de {self.valor_minimo} até {self.valor_maximo}): ')

    def GeradorNumero(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

numero = ChuteNumero()
numero.Iniciar()
