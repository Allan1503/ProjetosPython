# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6

import sys
sys.path.append("C:/Users/allan/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/site-packages")
import PySimpleGUI as sg
import random


class SimuladorDeDado:
    valor_minimo = 1
    valor_maximo = 6
    mensagem = 'Você gostaria de gerar um novo valor para o  dado? [S/N]'

    # Layout
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Quer jogar o dado?')],
        [sg.Button('Sim'), sg.Button('Não')]
    ]

    layoutpos = [
        [sg.Text('Quer joga novamente?')],
        [sg.Button('Sim'), sg.Button('Não')],
    ]

    def __int__(self):
        self.valor_minimo
        self.valor_maximo
        self.mensagem

    def Iniciar(self):

        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout = self.layout)
        self.janelapos = sg.Window('Simulador de Dado', layout = self.layoutpos)

        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()

        # Fazer alguma coisa com esses valores
        while True:
            if self.eventos == sg.WIN_CLOSED or self.eventos == 'Não':
                print('Obrigado por participar!')
                break
            else:
                self.GerarValorDoDado()
                self.eventos, self.valores = self.janelapos.Read()

                if self.eventos == sg.WIN_CLOSED or self.eventos == 'Não':
                    print('Obrigado por participar!')
                    break
                else:
                    continue


    def GerarValorDoDado(self):
        saida = random.randint(self.valor_minimo, self.valor_maximo)
        print(saida)


simulador = SimuladorDeDado()

simulador.Iniciar()