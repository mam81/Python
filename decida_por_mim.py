# Nome do projeto - Decida por mim

# Objetivo: Fazer uma pergunta(sobre uma ação) para o programa e receber uma resposta!

import random

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
        input('Faça uma pergunta: ')
        print(random.choice(self.respostas))

decisao = Decisao()
decisao.Iniciar()