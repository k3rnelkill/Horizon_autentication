#!/usr/bin/python3

import shutil
import pyautogui
import os


mensagem = 'Ferramenta para armazenar senha de conexão!'
pyautogui.alert(mensagem,
      title='ClickTI Horizon Connect',
      button='Iniciar coleta de senha?')

pergunta = 'Deseja Prosseguir?'

resposta = pyautogui.confirm(pergunta,
                    buttons=['Sim', 'Não'])
print(resposta)


#COLETA NOVA SENHA
if resposta.upper()[0] == 'S':
    USUARIO = pyautogui.prompt(text='Digite seu usuário: ', title="Informe o usuário")
    SENHA = pyautogui.password(text='Digite sua senha: ', title="Update Password")
    pyautogui.alert(text='Senha armazenada com sucesso.')
    pyautogui.alert(text='Reiniciando o sistema!')

    #DELETAR ARQUIVO ANTIGO
    if os.path.exists("inicializa-vmhorizon.sh"):
        os.remove("inicializa-vmhorizon.sh")
    else:
        print("O arquivo não existe!")

    #CRIAR ARQUIVOS DE INICIALIZACAO
    arquivo = open('inicializa-vmhorizon.sh', "a", encoding='utf-8')
    arquivo.write(f"#!/bin/bash \n")
    arquivo.write(f"/usr/bin/vmware-view -u {USUARIO} -p {SENHA} -q")
    os.chmod("inicializa-vmhorizon.sh", 0o777)
    os.system("reboot")
else:
    pyautogui.alert('OXII, não vai trabalhar não???')
