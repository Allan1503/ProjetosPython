# Projeto 3 - Chute o número
# objetivo: Criar um algorítimo que gera um valor aleatório e eu tenho que ficar tentando o número até eu acertar
import random 

import sys
sys.path.append("C:/Users/allan/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/site-packages")
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        self.valor_aleatorio = 0
        self.tentativas = 0
        self.janela = None
        self.janela_aberta = False

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute', size=(30,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(30,10))]
        ]
        # Criação da janela
        self.janela = sg.Window('Chute o número', layout=layout)
        self.janela_aberta = True
        # Gera um número aleatório
        
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Lê os valores da tela
                if not self.janela_aberta:
                    return
                self.evento, self.valores = self.janela.Read()
                if self.evento == sg.WIN_CLOSED:
                    self.janela.close()
                    self.janela_aberta = False
                    break
                # Verifica se o valor digitado é um número
                try:
                    valor_chute = int(self.valores['ValorChute'])
                except ValueError:
                    print('Por favor, digite apenas números!')
                    continue
                # Verifica se o valor digitado é o valor correto
                self.tentativas += 1
                if valor_chute == self.valor_aleatorio:
                    if self.janela_aberta:
                        print('PARABÉNS VOCÊ ACERTOU!!')
                        self.tentar_novamente = False
                        self.janela.close()
                        self.janela_aberta = False
                        break
                elif valor_chute > self.valor_aleatorio:
                    print('Chute um valor mais baixo...')
                else:
                    print('Chute um valor mais alto...')
        except:
            print('Ocorreu um erro ao executar o programa.')
            self.janela.close()
            self.janela_aberta = False

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =  random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()