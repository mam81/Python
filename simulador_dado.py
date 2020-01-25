# Simulador de Dado

#  - Simular um dado,gerando valores de 1 até 6 - 

import random
import PySimpleGUI as sg 

class Dado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostara de gerar um novo valor? '

        # Layout

        self.layout = [
            [sg.Text('Deseja jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def iniciar(self):

        # Janela

       self.janela = sg.Window('Simulador de Dado', layout=self.layout)  

        # Ler os valores na tela

       self.eventos, self.valores = self.janela.Read()
        
        # Fazer allgo com esses valores

       try:
           if self.eventos == 'Sim' or self.eventos == 'S':
               self.gerar_valor()
           elif self.eventos =='Não' or self.eventos == 'N':
               print('Agradecemos a participação, volte sempre :)')
           else:
               print('Favor digitar sim ou não (considerando pontuações)!')
       except:
           print('Ocorreu um erro ao receber sua resposta!')
            
    def gerar_valor(self):
        print(random.randint(self.valor_minimo, self.valor_maximo)) 


dado_simulado = Dado()
dado_simulado.iniciar()


