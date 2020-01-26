# Nome do projeto - Jogo de Aventura

# Objetivo - Um jogo que consistirá de vários finais distintos de acordo com as respostas dadas

class JogoAventura:

    def __init__(self):
        self.pergunta_1 = 'Você nasceu no norte ou no sul(n/s)? ' # Norte = lado A ; Sul = lado B;
        self.pergunta_2 = 'Você prefere a espada ou escudo(espada/escudo)? ' # espada = lado A; escudo = lado B;
        self.pergunta_3 = 'Qual é sua especialidade(linha de frente/tatico)? ' # linha de frente = lado A; # tático = lado B;
        self.final_historia_1 = 'Você é um heroi na linha de frente!'
        self.final_historia_2 = 'Você  será um  heroi protegendo as tropas!'
        self.final_historia_3 = 'Você irá se sacrificar na batalha!'
        self.final_historia_4 = 'Você não pe capaz de lutar nessa batalha!'
    
    def Iniciar(self):
        resposta_1 = input(self.pergunta_1)
        if resposta_1 == 'n':
            resposta_1A = input(self.pergunta_2)
            if resposta_1A == 'espada':
                print(self.final_historia_1)
            elif resposta_1A == 'escudo':
                print(self.final_historia_2)
        elif resposta_1 == 's':
            resposta_1A = input(self.pergunta_3)
            if resposta_1A == 'linha de frente':
                print(self.final_historia_3)
            elif resposta_1A == 'tatico':
                print(self.final_historia_4)

jogo = JogoAventura()
jogo.Iniciar()