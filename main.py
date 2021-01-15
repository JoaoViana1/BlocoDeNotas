import PySimpleGUI as sg
sg.ChangeLookAndFeel('BrownBlue') # change style

WIN_W: int = 90
WIN_H: int = 25
filename: str = None

#string variables to shorten loop and menu code
file_new: str = 'Novo.............(CTRL+N)'
File_open: str = 'Abrir.............(CRTL+O)'
file_save: str = 'Salvar..........(CRTL+S)'

menu_layout: list = [['Arquivo', [file_new, file_save, 'Salvar como', '---', 'Sair']],
                     ['Ferramentas', ['Contagem de palavras']],
                     ['Ajudar', ['Sobre']]]
layout: list = [[sg.Menu(menu_layout)],
                [sg.Text('> Novo arquivo <', font=('Consolas', 10), size=(WIN_W,1), key='_INFO_')],
                [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]]
window: object = sg.Window('Bloco de Notas do Foster', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
