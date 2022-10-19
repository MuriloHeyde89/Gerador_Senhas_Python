import random
from tkinter import Button, mainloop
import PySimpleGUI as sg
import os
from playsound import playsound

class PassGen:
    def __init__(self):
        #Layout
        sg.theme('Dark2')
        playsound('fundo.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(12, 1)),
            sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(12, 1)),
            sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)),key='total_chars', default_value=1, size=(4, 1))],
            [sg.Text('As senhas geradas estão sendo salvas no arquivo:',key='caminho_arquivo', size=(51,1))],
            [sg.Multiline(os.getcwd() + '\senhas.txt', disabled=True, size=(51,1))],
            [sg.Text('Nova senha gerada: ', size=(51,1))],
            [sg.Multiline('', disabled=True, size=(50,1), key='out')],
            [sg.Button('Gerar Senha', size=(13,1)), sg.Button('Sair', size=(13,1))], 
            {sg.Button('Limpar Tela', size=(13,1))}
        ]
        #janela
        self.janela = sg.Window('Gerador de Senhas', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                self.janela.find_element('out').Update(nova_senha)
                self.salvar_senha(nova_senha, valores)
            if evento == 'Limpar Tela':
                self.limpar_output()
            if evento == 'Sair':
                self.botao_sair()
    
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop rstuwxyz123456789!#$%¨*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n")
    
    def limpar_output(self):
        self.janela.FindElement('out').Update('')
    
    #criando botão sair (Pesquisando, sem cópia!)
    def botao_sair(self, Sair):
        self.botao_sair = Button(self.janela, text= 'Sair', command=self.janela.quit)
        self.botao.pack()
        self.botao_sair.pack()
        mainloop()

gen = PassGen()
gen.Iniciar() 