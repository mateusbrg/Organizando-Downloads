import os
import pathlib
from modulos import *
from time import sleep
from colorama import Fore, Style, Back

# Detectando pasta Downloads
userpath = pathlib.Path.home()  # Detectando pasta do usuário /Users//
pathstr = str(userpath) + '\\Downloads\\teste'  # Há uma forma melhor de fazer isso?
#  Alterado pra //teste para não ter risco de griffar a pasta Downloads
downloadpath = pathlib.Path(pathstr)  # Transformando a string em um objeto que aceita métodos
# Talvez com joinpath

#  Há maneiras melhores de fazer isso, mas usarei o pathstr como parâmetro para outras funções
os.system('cls')  # Para executar comandos no sistema. Será executado o comando cls para limpar o terminal

traco(f'{Fore.LIGHTRED_EX}Organizador de Downloads{Style.RESET_ALL}')
print('Olá! Vou te ajudar com a bagunça da sua pasta Downloads')
print('')
input('Aperte < enter > para continuar!')  

os.system('cls')  

print('Procurando pasta...')

os.chdir(downloadpath)  #  Mudando diretório que o programa vai atuar

pastas = mostrarArquivos(pathstr)  #  Função mostrar arquivos
#  mostrarArquivos() retorna uma lista com os sufixos encontrados dos arquivos analisados
print()
sleep(1)
criarPastas(pastas)  # Função criarPastas recebe a lista 
print('')
input(f'Aperte < enter > para continuar!')
os.system('cls')

print('Agora vamos organizar os arquivos!')
sleep(2)

moverArquivos(pathstr, pastas)  # Função moverArquivos
print()

os.system('cls')

print(f'{Fore.LIGHTRED_EX}ATENÇÃO!')
print(f'{Fore.WHITE}A pasta Downloads será aberta')
sleep(1)
print(f'{Fore.YELLOW}Veja se gostou das alterações')
sleep(1)
print(f'{Fore.WHITE}Se quiser desfazer as alterações, volte aqui no programa e confirme a respectiva opção')
print(f'{Fore.LIGHTRED_EX}NÃO FECHE O PROGRAMA!')
print(Style.RESET_ALL)

for c in range(5, 0, -1):
    sleep(1)
    print(f'Abrindo pasta Downloads em {c}')
    
os.startfile(pathstr)

print(f'''
        Quer manter as alterações?
        Digite '{Fore.LIGHTGREEN_EX}S{Style.RESET_ALL}' para manter as alterações
        Digite '{Fore.LIGHTRED_EX}N{Style.RESET_ALL}' para desfazer alterações
        
        As pastas vazias são temporárias e serão apagadas
        ''')
print('')

#  Bloco da opção do usuário
while True:  # Loop em caso de erros
    try:  # Tente isso
        opcao = str(input('Sua opção: ')).strip().upper()
    except:  # Se der erro
        print(f'{Fore.RED}ERRO! Opção Inválida!{Style.RESET_ALL}')
    else:  # Se não der erro, analisaremos outro
        if opcao not in 'SN':  # Se não estiver em S ou N, volta pro começo do Loop
            print(f'{Fore.RED}ERRO! Digite "S" para sim e "N" para não{Style.RESET_ALL}')
        else:  # Se tudo estiver ok
            break
if opcao in 'N':  # Se a opção é desfazer alterações
    desfazer()  # Função desfazer()
    removerVazios(pathstr)  # Remover pastas vazias que foram criadas pela função criarPastas()
else:  # Se não
    removerVazios(pathstr)  # Somente remove as pastas vazias que sobraram de caminhos antigos

print('')
print('=' * 38)
print(' Muito obrigado por usar o programa! ')
print(f' Feito com muito {Fore.LIGHTRED_EX}<3{Style.RESET_ALL} por {Style.BRIGHT}@mateusbrg{Style.RESET_ALL} ')
print('=' * 38)
print('')
input(' Aperte < enter > para fechar o programa... ')
os.system('exit')
