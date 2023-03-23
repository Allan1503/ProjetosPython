# Importa as bibliotecas necessárias
import PySimpleGUI as sg
import os
import pickle

# Verifica se o arquivo "usuarios.pickle" existe. Se não existir, cria um arquivo vazio.
if not os.path.exists('usuarios.pickle'):
    with open('usuarios.pickle', 'wb') as f:
        pickle.dump({}, f)

# Define uma classe para a tela de login
class TelaLogin:
    def __init__(self):
        # Define o tema da janela
        sg.theme('DarkBlue')
        # Define o layout da janela
        layout = [
            [sg.Text('Nome de Usuário:'), sg.Input(key='usuario')],
            [sg.Text('Senha:'), sg.Input(key='senha', password_char='*')],
            [sg.Button('Entrar'), sg.Button('Cadastrar')]
        ]
        # Cria a janela
        self.janela = sg.Window('Tela de Login', layout)
        self.tela_cadastro = None
        self.usuario_logado = None

    def Iniciar(self):
        # Loop principal da janela
        while True:
            # Lê os eventos e valores da janela
            evento, valores = self.janela.Read()
            # Verifica se o evento é o fechamento da janela
            if evento == sg.WIN_CLOSED:
                break
            # Verifica se o evento é o botão "Entrar"
            if evento == 'Entrar':
                usuario = valores['usuario']
                senha = valores['senha']
                # Verifica se o login é válido
                if self.ValidarLogin(usuario, senha):
                    self.usuario_logado = usuario
                    sg.popup(f'Bem-vindo, {usuario}!')
                    self.janela.close()
                    break
                else:
                    sg.popup('Usuário ou senha inválidos.')
            # Verifica se o evento é o botão "Cadastrar"
            elif evento == 'Cadastrar':
                self.ExibirTelaCadastro()

        self.janela.close()

    def ValidarLogin(self, usuario, senha):
        # Carrega os usuários registrados do arquivo "usuarios.pickle"
        with open('usuarios.pickle', 'rb') as f:
            usuarios_registrados = pickle.load(f)
        # Verifica se o usuário e senha informados são válidos
        if usuario in usuarios_registrados and usuarios_registrados[usuario] == senha:
            return True
        else:
            return False

    def ExibirTelaCadastro(self):
        # Define o tema da janela
        sg.theme('DarkBlue')
        # Define o layout da janela
        layout = [
            [sg.Text('Nome:'), sg.Input(key='nome')],
            [sg.Text('E-mail:'), sg.Input(key='email')],
            [sg.Text('Nome de Usuário:'), sg.Input(key='usuario')],
            [sg.Text('Senha:'), sg.Input(key='senha', password_char='*')],
            [sg.Button('Cadastrar'), sg.Button('Cancelar')]
        ]
        # Cria a janela de cadastro
        self.tela_cadastro = sg.Window('Cadastro de Usuário', layout)
        # Loop principal da janela de cadastro
        while True:
            # Lê os eventos e valores da janela de cadastro
            evento, valores = self.tela_cadastro.Read()
            # Verifica se o evento é o fechamento da janela de cadastro ou o botão "Cancelar"
            if evento == sg.WIN_CLOSED or evento == 'Cancelar':
                break
# Verifica se o usuário clicou no botão "Cadastrar"
            elif evento == 'Cadastrar':
                
                # Obtém os dados digitados pelo usuário
                nome = valores['nome']
                email = valores['email']
                usuario = valores['usuario']
                senha = valores['senha']
                
                # Verifica se todos os campos foram preenchidos
                if nome.strip() == '' or email.strip() == '' or usuario.strip() == '' or senha.strip() == '':
                    sg.popup('Por favor, preencha todos os campos.')
                
                # Verifica se o nome de usuário já está cadastrado
                elif self.ValidarCadastro(usuario):
                    
                    # Abre o arquivo "usuarios.pickle"
                    with open('usuarios.pickle', 'rb') as f:
                        usuarios_registrados = pickle.load(f)
                    
                    # Adiciona o usuário e senha ao dicionário "usuarios_registrados"
                    usuarios_registrados[usuario] = senha
                    
                    # Salva o dicionário "usuarios_registrados" no arquivo "usuarios.pickle"
                    with open('usuarios.pickle', 'wb') as f:
                        pickle.dump(usuarios_registrados, f)
                    
                    # Exibe uma mensagem de sucesso e fecha a janela de cadastro
                    sg.popup('Cadastro realizado com sucesso!')
                    self.tela_cadastro.close()
                    break
                else:
                    sg.popup('Nome de usuário já cadastrado.')
        self.tela_cadastro.close()


        self.tela_cadastro.close()

    def ValidarCadastro(self, usuario):
        with open('usuarios.pickle', 'rb') as f:
            usuarios_registrados = pickle.load(f)
        if usuario in usuarios_registrados:
            return False
        else:
            return True

tela_login = TelaLogin()
tela_login.Iniciar()