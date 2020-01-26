# Nome do projeto - Decida por mim

# Objetivo: Fazer uma pergunta(sobre uma ação) para o programa e receber uma resposta!

import random
import PySimpleGUI as sg 

class Decisao:

    def __init__(self):

        self.respostas = [
            'Com certeza,você deve fazer isso!',
            'Vai em frente',
            'Não sei,você que sabe',
            'Não faça isso não!',
            'Acho que tá hora certa!'
        ]

    def Iniciar(self):

        # Layout
        layout = [
            [sg.Text('Faça uma pergunta')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Resposta')]
        ]

        # Janela
        self.janela = sg.Window('Decida por mim', layout=layout)

        while True:

            # Valores
            self.eventos, self.valores = self.janela.Read()

            # Implantação valores
            if self.eventos == 'Resposta':
                print(random.choice(self.respostas))

decisao = Decisao()
decisao.Iniciar()