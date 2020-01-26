# Nome do projeto - Jogo de Aventura

# Objetivo - Um jogo que consistirá de vários finais distintos de acordo com as respostas dadas

import PySimpleGUI as sg 

class JogoAventura:

    def __init__(self):
        self.pergunta_1 = 'Você nasceu no norte ou no sul(n/s)? ' # Norte = lado A ; Sul = lado B;
        self.pergunta_2 = 'Você prefere a espada ou escudo(espada/escudo)? ' # espada = lado A; escudo = lado B;
        self.pergunta_3 = 'Qual é sua especialidade(linha de frente/tatico)? ' # linha de frente = lado A; # tático = lado B;
        self.final_historia_1 = 'Você é um heroi na linha de frente!'
        self.final_historia_2 = 'Você  será um  heroi protegendo as tropas!'
        self.final_historia_3 = 'Você irá se sacrificar na batalha!'
        self.final_historia_4 = 'Você não é capaz de lutar nessa batalha!'
    
    def Iniciar(self):

        # Layout

        layout = [
            [sg.Output(size=(30,0), key='respostas')],
            [sg.Input(size=(25,0), key='escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder')]
        ]

        # Janela

        self.janela = sg.Window('Jogo de Aventura', layout=layout)

        # Leitura dos dados
        while True:

            self.LerValor()

            # Impantação
            if self.eventos == 'Iniciar': 
                print(self.pergunta_1)
                self.LerValor()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta_2)
                    self.LerValor()
                    if self.valores['escolha'] == 'espada':
                        print(self.final_historia_1)
                    elif self.valores['escolha'] == 'escudo':
                        print(self.final_historia_2)
                elif self.valores['escolha'] == 's':
                    print(self.pergunta_3)
                    self.LerValor()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.final_historia_3)
                    elif self.valores['escolha'] == 'tatico':
                        print(self.final_historia_4)

    def LerValor(self):
        self.eventos, self.valores = self.janela.Read()
        
jogo = JogoAventura()
jogo.Iniciar()