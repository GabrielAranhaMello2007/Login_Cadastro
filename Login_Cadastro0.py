# Login_Cadastro
# Um programa em que é possível fazer Login(Usa outro arquivo como banco de dados) e Cadastro
# Para fazer a instalação do "PySimpleGui"
# Copie "pip install PySimpleGUI" e logo em seguida cole isso no terminal do Python

import PySimpleGUI as sg
from Banco_de_dados import *


import PySimpleGUI as Sg
from Banco_de_dados import *
import time


def janela_login():

    Sg.theme('DarkBlack')
    layout = [
        [Sg.Text('Login', size=(30, 1))],
        [Sg.Input(key='login', size=(25, 1))],
        [Sg.Text('', text_color='red', size=(25, 1), key='text1')],
        [Sg.Text('Senha', size=(30, 1))],
        [Sg.Input(size=(25, 1), key='password', password_char='*')],
        [Sg.Text('', text_color='red', key='text2', size=(30, 1))],
        [Sg.Text(size=(29, 10))],
        [Sg.Button('Entrar')],
        [Sg.Button('Cadastro')],
        [Sg.Text(size=(0, 1))]
    ]
    return Sg.Window('Janela Login', finalize=True, layout=layout)


def janela_login_correct():

    Sg.theme('DarkBlack')
    layout = [
        [Sg.Text(size=(32, 1))],
        [Sg.Text(size=(5, 0)), Sg.Text('Acesso concedido\n'
                                       'A janela será encerrada em ...5 segundos', text_color='green', key='jlc')],
        [Sg.Text()]
    ]
    return Sg.Window('Acesso concedido', finalize=True, layout=layout)


def janela_cadastro_correct():

    Sg.theme('DarkBlack')
    layout = [
        [Sg.Text(size=(32, 1))],
        [Sg.Text(size=(5, 1)), Sg.Text('Conta criada com sucesso', text_color='green', key='jcc')],
        [Sg.Text()]
    ]
    return Sg.Window('Acesso concedido', finalize=True, layout=layout)


def janela_cadastro():

    Sg.theme('DarkBlack')
    layout = [
        [Sg.Text('Novo login', size=(30, 1))],
        [Sg.Input('', key='login_cadastro', size=(25, 1))],
        [Sg.Text('', key='text3', text_color='red', size=(25, 1))],
        [Sg.Text('Crie sua senha', size=(30, 1))],
        [Sg.Input(key='password_cadastro_1', size=(25, 1), password_char='*')],
        [Sg.Text('Confirme sua senha', size=(30, 1))],
        [Sg.Input(key='password_cadastro_2', size=(25, 1), password_char='*')],
        [Sg.Text('', key='text4', text_color='red', size=(30, 1))],
        [Sg.Text(size=(29, 10))],
        [Sg.Button('Cadastrar')],
        [Sg.Text(size=(0, 1))]
    ]
    return Sg.Window('Janela Cadastro', finalize=True, layout=layout)


janela1, janela2, janela3, janela4 = janela_login(), None, None, None


def verifica_login():

    win = False

    if window == janela1:
        try:
            users[value['login']]
        except KeyError:
            window['text1'].update('Usuário não encontrado')
        else:
            window['text1'].update('')

            if users[value['login']] != value['password']:
                window['text2'].update('Senha incorreta')

            else:
                window['text2'].update('')

                if event == 'Entrar':
                    win = True
    return win


def verifica_cadastro():

    win = False

    if window == janela2:
        if value['login_cadastro'] in users:
            window['text3'].update('Login já em uso')

        else:
            window['text3'].update('')

            if value['password_cadastro_1'] != value['password_cadastro_2']:
                window['text4'].update('As senhas não coincidem')

            else:
                window['text3'].update('')

                
                if event == 'Cadastrar':
                    red = open('Banco_de_dados.py', 'a')
                    red.write(f'login = "{value["login_cadastro"]}"\n'
                              f'senha = "{value["password_cadastro_1"]}"\n'
                              'users.update({login: senha})\n')
                win = True
                
    return win


while True:
    window, event, value = Sg.read_all_windows()

    if event == Sg.WINDOW_CLOSED:
        break

    if window == janela1:
        verifica_login()

    if event == 'Cadastro':
        janela1.hide()
        janela2 = janela_cadastro()

    if window == janela2:
        verifica_cadastro()

    if verifica_cadastro() is True:
        janela2.hide()
        janela4 = janela_cadastro_correct()

        time.sleep(5)
        break

    if verifica_login() is True:
        janela1.hide()
        janela3 = janela_login_correct()

        time.sleep(5)
        break

