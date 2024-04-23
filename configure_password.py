"""
Caixas de diálogo para interação com usuários
"""
#from pyautogui import alert, confirm, prompt, password
import shutil
import pyautogui
import os


mensagem = 'Ferramenta para armazenar senha de conexão!'
pyautogui.alert(mensagem,
      title='Horizon Connect',
      button='Iniciar coleta de senha?')

pergunta = 'Deseja Prosseguir?'

resposta = pyautogui.confirm(pergunta,
                    buttons=['Sim', 'Não'])
print(resposta)


#COLETA NOVA SENHA
if resposta.upper()[0] == 'S':
    USUARIO = pyautogui.prompt(text='Digite seu usuário: ', title="Informe o usuário")
    #SENHA = pyautogui.password(text='Digite sua senha: ', title="Update Password")
    pyautogui.alert(text='Senha armazenada com sucesso.')
    pyautogui.alert(text='Faça um logoff e inicie novamente!')

    #DELETAR ARQUIVO ANTIGO
    if os.path.exists("/home/usuario/HorizonClick/inicializa-vmhorizon.sh"):
        os.remove("/home/usuario/HorizonClick/inicializa-vmhorizon.sh")
    else:
        print("O arquivo não existe!")

    #CRIAR ARQUIVOS DE INICIALIZACAO
    arquivo = open('/home/clickti/HorizonClick/inicializa-vmhorizon.sh', "a", encoding='utf-8')
    arquivo.write(f"#!/bin/bash \n")
    #arquivo.write(f"/usr/bin/vmware-view -u {USUARIO} -p {SENHA} -q")
    arquivo.write(f"/usr/bin/vmware-view -u {USUARIO} audi.dominio.com.br -q")
    os.chmod("/home/usuario/HorizonClick/inicializa-vmhorizon.sh", 0o777)
else:
    pyautogui.alert(text='Oxi, não vai trabalhar não???')
