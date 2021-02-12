# Login_Cadastro
# Um programa em que é possível fazer Login(Usa outro arquivo como banco de dados) e Cadastro
# Para fazer a instalação do "PySimpleGui"
# Copiei "pip install PySimpleGUI" e logo em seguida cole isso no terminal do Python

import PySimpleGUI as sg
from Banco_de_dados import *


def janela_login():
    """Retorna a página de login"""
    sg.theme('Reddit')
    layout = [
        [sg.Text('Login'), sg.Input(key='login')],
        [sg.Text('Senha'), sg.Input(password_char='*', key='senha')],
        [sg.Button('Cadastro')],
        [sg.Button('Entrar')]
    ]
    return sg.Window('janela_login', layout=layout, finalize=True)


def janela_cadastro():
    """Retorna a página de cadastro"""
    sg.theme('Reddit')
    layout_cadastro = [
        [sg.Text('Seu novo login'), sg.Input(key='login')],
        [sg.Text('Sua nova senha'), sg.Input(password_char='*', key='senha')],
        [sg.Button('< Voltar', key='voltar')],
        [sg.Button('Criar nova conta', key='cnv')]
    ]
    return sg.Window('janela_cadastro', layout=layout_cadastro, finalize=True)


janela1, janela2 = janela_login(), None

while True:

    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WINDOW_CLOSED:
        break

    if window == janela2 and event == sg.WINDOW_CLOSED:
        break

    if window == janela1 and event == 'Entrar':

        if values['login'] in users:

            if values['senha'] == users[values['login']]:

                print('\033[32m-' * 60)
                print('Acesso autorizado')
                print('-' * 60)
                break

            else:

                print('\033[31m-' * 60)
                print('Acesso negado (Senha incorreta)')
                print('-' * 60)

        else:

            print('\033[31m-' * 60)
            print(f'Nenhuma conta registrada com "{values["login"]}"')
            print('-' * 60)

    if window == janela1 and event == 'Cadastro':

        janela1.hide()
        janela2 = janela_cadastro()

    if window == janela2 and event == 'cnv':

        if values['login'] not in users:

            print('\033[32m-' * 60)
            print('Conta criada com Sucesso!!')
            print('-' * 60)

            red = open('../Banco_de_dados.py', 'a')
            red.write(f'login = "{values["login"]}"\n'
                      f'senha = "{values["senha"]}"\n'
                      'users.update({login: senha})\n')

            red.close()
            break

        else:

            print('\033[31m-' * 60)
            print('Usuário já cadastrado')
            print('-' * 60)

    if window == janela2 and event == 'voltar':
        janela2.hide()
        janela1.un_hide()

