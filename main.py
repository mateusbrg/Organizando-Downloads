import os
import pathlib
from modulos import *
from time import sleep

# Detectando pasta Downloads
userpath = pathlib.Path.home()  # Detectando pasta do usuário /Users//
pathstr = str(userpath) + '\\Downloads\\teste'  # Há uma forma melhor de fazer isso?
#  Alterado pra //teste para não ter risco de griffar a pasta Downloads
downloadpath = pathlib.Path(pathstr)  # Transformando a string em um objeto que aceita métodos
# Talvez com joinpath

#  Há maneiras melhores de fazer isso, mas usarei o pathstr como parâmetro para outras funções

traco('\033[1;34mOrganizador de Downloads\033[m')
print('\033[1mOlá! Vou te ajudar com a bagunça da sua pasta Downloads\033[m')
print('\033[1mProcurando pasta...\033[m')

os.chdir(downloadpath)  #  Mudando diretório que o programa vai atuar

sleep(1)
traco(f'\033[1mAnalisando\033[m \033[1;35m< {downloadpath} >\033[m')
sleep(1)

mostrarArquivos(pathstr)  #  Função mostrar arquivos