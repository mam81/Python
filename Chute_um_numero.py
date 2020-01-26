# Projeto: Chute um número

# Objetivo: Criar um algoritmo que gera um valor aleatório e eo usuário deve arriscar valores para acertar!

import random 
import PySimpleGUI as sg

class Chute_Numero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentativas = 0
        self.tentar_novamente = True
    
    def Iniciar(self):

        # Layout

        layout = [
            [sg.Text('Seu Chute',size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Confirmar')],
            [sg.Output(size=(39,10))]
        ]
        # criar uma janela
        self.janela = sg.Window('Chute o numero!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                
                # receber os valores

                self.evento, self.valores = self.janela.Read()

                # Fazer alguma coisa com estes valores

                if self.evento == 'Confirmar':
                    self.valor_do_chute = self.valores['ValorChute']

                    while self.tentar_novamente:

                        self.tentativas += 1

                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print(f'Parabéns você acertou!! Ao todo foi gasto {self.tentativas} tentativas para o acerto do número {self.valor_aleatorio}')
                            break

                        elif int(self.valor_do_chute) > self.valor_aleatorio:
                            print(f'Chute um valor mais baixo(de {self.valor_minimo} até {self.valor_maximo})!')
                            break

                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print(f'Chute um valor mais alto(de {self.valor_minimo} até {self.valor_maximo})!')
                            break
                
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()
            

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =  random.randint(self.valor_minimo,self.valor_maximo)

chute = Chute_Numero()
chute.Iniciar()
