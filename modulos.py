from colorama import Fore, Style, Back


def traco(msg):
    """
    -> Print personalizado com traços de acordo com o tamanho do parâmetro msg
    :param msg: Mensagem a ser deixada no meio do print, centralizada
    :return: Sem retorno
    """

    print(f'{Fore.GREEN}-{Style.RESET_ALL}' * 45)  # print('-')
    print(f' {msg:^45} ')
    print(f'{Fore.GREEN}-{Style.RESET_ALL}' * 45)  # print('-')

# ===================================== Feito com base no Gist de @robsonpiere ==============================#
# ================== https://gist.github.com/robsonpiere/fc256f6e7b7301d2d12343372cde93f9 ===================#
sffx = []  # Lista que será usada para guardar as pastas criadas pela função abaixo


def mostrarArquivos(caminho):
    """
    -> Função que mostra os arquivos de todas as pastas e subpastas de um diretório
    -> Também uma lista com todos os tipos de arquivos (sufixos .exe, .jpg, .pdf, etc)
    :param caminho: Caminho do diretório em tipo str()
    :return: Retorna a lista com os tipos de arquivos encontrados (sem repetições)
    """

    from pathlib import Path
    from time import sleep
    # Caso queira ver o que está intrínseco na função, adicione os comandos comentados (coloque cores).
    caminho = Path(caminho)  # Caminho como objeto
    subpastas = []  # Lista subpastas vazia
    global sffx  # Variável global de modulos.py

    sleep(1.5)
    traco(f'{Fore.BLACK}{Back.LIGHTCYAN_EX}-----> Analisando < {caminho} >{Style.RESET_ALL}') 
    for item in caminho.iterdir():  # Para cada item no caminho iterável
        if item.is_dir():  # Se o item for uma pasta
            subpastas.append(item)  # Adiciona na lista de subpastas
            continue  
            # Volta pro começo da iteração, ignorando o resto do processo
        print(f'{Fore.YELLOW}-> {Fore.CYAN}{item.name}{Style.RESET_ALL}')  
        # Se não for pasta, é arquivo, então mostra o nome
        # print('-> {item.name}')
        if item.suffix not in sffx:
            sffx.append(item.suffix)
        # print(subpastas)

    for subpasta in subpastas:  # Para cada subpasta na lista subpastas
        # print(subpastas)
        # print(subpasta)
        mostrarArquivos(subpasta)        
    return sffx
# ===================================== Obrigado @robsonpiere! ===========================================#

    # Por algum motivo, o Python guarda a primeira ocorrência da lista subpastas, fazendo com que várias variáveis subpastas 
    # temporárias existam. Eu não entendi a lógica dessa função, pensei em algo parecido, mas não nessa linha de pensamento
    # Buscarei explicações para o que acontece aqui.

    #  Não é possível usar o enumerate porque ele vai contar os diretórios e não printá-los, 
    # fazendo com que o índice fique com buracos
    #  As vezes o intellisense buga no Pycharm e aqui
    #  Variável .name
    
# =======================================================================================================#

def criarPastas(lst):
    """
    -> Função que cria as pastas de acordo com os sufixos encontrados na função moverArquivos():
    :param lst: Inserir aqui o Retorno da função moverArquivos()
    :return: Sem retorno
    """

    from os import makedirs
    from time import sleep

    for suffix in lst:  # Para cada sufixo em lst (lst é uma lista que foi retornada para main.py)
        try:  # Tenta isso aqui
            makedirs(suffix)
        except FileExistsError:
            print(f'{Fore.LIGHTBLUE_EX}Pasta {Fore.MAGENTA}{suffix}{Fore.LIGHTBLUE_EX} já foi criada!{Style.RESET_ALL}')
            #  Mesmo se essa pasta existir manualmente, ela será detectada
        else:
            print(f'{Fore.YELLOW}Criando pasta para arquivos {Fore.MAGENTA}{suffix}{Style.RESET_ALL}')
    print('')
    print('Feito!')
    sleep(1.5)

log = []  # Lista que serve como um arquivo log, que guarda todas as alterações feitas


def moverArquivos(pathstr, lst):
    """
    -> Função que move os arquivos pras respectivas pastas de acordo com o tipo de arquivo (.any)
    -> Quando encontra subpastas, é solicitado ao usuário se os arquivos locais deverão ser movidos ou não
    :param pathstr: Caminho da pasta Downloads em tipo str()
    :param lst: Lista de pastas criadas (retorno de mostrarArquivos())
    """

    from shutil import move
    from pathlib import Path
    
    subpastas = []
    global log
    caminho = Path(pathstr)  # Transformando str em um objeto iterável

    for pasta in lst:  # Para cada pasta nas pastas que foram criadas (retorno de mostrarArquivos())
        for item in caminho.iterdir():  # Para cada item no caminho da pasta Downloads
            if item.is_dir():  # Se o item é um diretório 
                if item.name in lst:  # Se o diretório já está na lista de pastas criadas
                    continue  # Ignora essa pasta
                #  Isso deve ser feito porque a função iterdir() também analisará os itens de pastas, pois esses itens
                #  São pastas que foram criadas na pasta Downloads
                elif item not in subpastas:  # Se o diretório encontrado não está nas subpastas 
                # Antes era item.name, mas dá conflito em str e objeto Path
                # Note que o elif só acontece se o if de cima for False
                    subpastas.append(item)  # Adiciona essa subpasta na lista subpastas
            
            elif item.match(f'*{pasta}'):  # Se o sufixo do item for o mesmo que o nome da pasta (função match())
                caminhoantigo = item  # Só pra explicitar
                caminhonovo = f'{pathstr}\\{pasta}\\{item.name}' # pathstr guarda o local da Pasta Downloads
                log.append(caminhoantigo)  # Append no log do programa para uso de backup
                log.append(caminhonovo)  # Append no log do programa para uso de backup
                move(caminhoantigo, caminhonovo)  # Função move() da biblioteca Shutil
                print(f'{Fore.LIGHTCYAN_EX}Movendo ' 
                f'{Fore.LIGHTWHITE_EX}{item.name} ' 
                f'{Fore.GREEN}para ' 
                f'{Fore.LIGHTWHITE_EX}{pasta}{Style.RESET_ALL}')
                # print('Movendo {item.name} para {pasta}')
    print('')

    for subpasta in subpastas:  # Para cada subpasta in subpastas
        while True:
            try:  # Tente pra mim
                opcao = str(input(f'{Fore.LIGHTWHITE_EX}Deseja mover os itens de {subpasta}? [S/N]: {Style.RESET_ALL}')).strip().upper()
            except:  # Se der erro (TypeError, KeyboardError, etc)
                print(f'{Fore.RED}Opção inválida! Por favor, tente novamente!{Style.RESET_ALL}')
            else:  # Se não der esses erros, vamos analisar outros
                if opcao[0] not in 'SsNn':   # Se opção não estiver em 'SsNn'
                    print(f'{Fore.LIGHTRED_EX}ERRO! Por favor, digite uma opção válida{Style.RESET_ALL}')  
                else:  # Se estiver 
                    break 
        if opcao[0] in 'S':  # Se a opção for SIM
            traco(f'{Back.BLUE}Acessando pasta < {subpasta} >{Style.RESET_ALL}')
            moverArquivos(subpasta, sffx)  #  De novo aquela lógica maluca lá
        elif opcao[0] in 'N':  # Se a opção for NÃO
            continue  # Ignora a subpasta
        
    #  C:\\Users\home\\Downloads\\pasta sffx\\subpasta pasta\\arquivo.any
    #  C:\\Users\\home\\Downloads\\{novo}\\{arquivo.any}


def desfazer():
    """
    -> Função que desfaz qualquer alteração feita anteriormente.
    -> Utiliza da lista log que guardou todos os antigos diretórios dos arquivos
    :return: Sem retorno
    """

    from shutil import move

    global log  #  Variável global log
    indicenovo = (len(log) - 1)  # O índice novo está no len(log) - 1
    indiceantigo = (len(log) - 2)  # O índice antigo está no len(log) - 2
    print(f'{Fore.LIGHTCYAN_EX}Desfazendo alterações...{Style.RESET_ALL}')
    while indiceantigo >= 0:  # Enquanto indiceantigo não chegar no índice 0
        indicenovo -= 2  # Subtrai 2
        indiceantigo -= 2  # Subtrai dois
        novo = log[indicenovo]  # O índice novo já está como str()
        antigo = str(log[indiceantigo])  # O índice antigo estava como objeto da classe Path
        move(novo, antigo)  # Move(novo, antigo)


def removerVazios(pathstr):
    """
    -> Função que remove pastas vazias
    :param pathstr: Diretório no tipo str()
    :return: Sem retorno
    """

    from pathlib import Path
    from os import rmdir

    downloadpath = Path(pathstr)  
    n = 0
    for item in downloadpath.iterdir():  # Para cada item no objeto iterável 
        if item.is_dir():  # Se o item é um diretório
            try:
                rmdir(item)
                # A função os.rmdir() só apaga diretórios vazios
            except OSError:  # Se o diretório não está vazio, dá a exceção OSError
                continue  # Pula esse item
            else:  # Se não der erros
                n += 1  # Conta a pasta apagada
                
    print(f'Removi {Fore.LIGHTRED_EX}{n}{Style.RESET_ALL} pasta(s) vazia(s)!')
