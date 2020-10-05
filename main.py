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

pastas = mostrarArquivos(pathstr)  #  Função mostrar arquivos
#  mostrarArquivos() retorna uma lista com os sufixos encontrados dos arquivos analisados
criarPastas(pastas)  # Função criarPastas recebe a lista 

moverArquivos(pathstr, pastas)

print('ATENÇÃO!')
print('A pasta Downloads será aberta')
sleep(1)
print('Veja se gostou das alterações')
sleep(1)
print('Se quiser desfazer as alterações, volte aqui no programa e confirme a respectiva opção')
print('NÃO FECHE O PROGRAMA!')
for c in range(5, 0, -1):
    sleep(1)
    print(f'Abrindo pasta Downloads em {c}')
    
os.startfile(pathstr)

print('''
        Quer manter as alterações?
        Digite 'S' para manter as alterações
        Digite 'N' para desfazer alterações
        
        As pastas vazias são temporárias e serão apagadas
        ''')

while True:
    try:
        opcao = str(input('Sua opção: ')).strip().upper()
    except:
        print('ERRO! Opção Inválida!')
    else:
        if opcao not in 'SN':
            print('ERRO! Digite "S" para sim e "N" para não')
        else:
            break
if opcao in 'N':
    desfazer()
    removerVazios(pathstr)
else:
    removerVazios(pathstr)

print('Muito obrigado por usar o programa!')
print('Feito com muito <3 por @mateusbrg')
