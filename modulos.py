import pathlib


def traco(msg):
    """
    -> Print personalizado com traços de acordo com o tamanho do parâmetro msg
    :param msg: Mensagem a ser deixada no meio do print, centralizada
    :return: Sem retorno
    """

    tam = len(msg) + 4
    print('\033[1;34m' + '-' * tam, end='')  # print('-')
    print('\033[m')
    print(f'  {msg:^}  ')
    print('\033[1;34m' + '-' * tam, end='')  # print('-')
    print('\033[m')

# ===================================== Feito com base no Gist de @robsonpiere ==============================#
# ================== https://gist.github.com/robsonpiere/fc256f6e7b7301d2d12343372cde93f9 ===================#
sffx = []


def mostrarArquivos(caminho):
    """
    -> Função que mostra os arquivos de todas as pastas e subpastas de um diretório
    -> Também uma lista com todos os tipos de arquivos (sufixos .exe, .jpg, .pdf, etc)
    :param caminho: Caminho do diretório em tipo str()
    :return: Retorna a lista com os tipos de arquivos encontrados (sem repetições)
    """

    from pathlib import Path
    # Caso queira ver o que está intrínseco na função, adicione os comandos comentados (coloque cores).
    caminho = Path(caminho)  # Caminho como objeto
    subpastas = []  # Lista subpastas vazia
    global sffx  # Variável global de modulos.py

    print(f' Analisando < {caminho} > ') 
    for item in caminho.iterdir():  # Para cada item no caminho iterável
        if item.is_dir():  # Se o item for uma pasta
            subpastas.append(item)  # Adiciona na lista de subpastas
            continue  
            # Volta pro começo da iteração, ignorando o resto do processo
        print(f' {item.name} ')  # Se não for pasta, é arquivo, então mostra o nome
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

    #  Não é possível usar o enumerate porque ele vai contar os diretórios e não printá-los, fazendo com que o índice fique com buracos
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

    for suffix in lst:
        try:
            makedirs(suffix)
        except FileExistsError:
            print(f'Pasta {suffix} já foi criada!')
        else:
            print(f'Criando pasta para arquivos {suffix}')
    print('Feito!')


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
                caminhonovo = f'C:\\Users\\teteu\\Downloads\\teste\\{pasta}\\{item.name}'
                move(caminhoantigo, caminhonovo)  # Função move() da biblioteca Shutil
                print(f'Movendo < {item.name} > para < {pasta} > ')

    for subpasta in subpastas:  # Para cada subpasta in subpastas
        while True:
            try:  # Tente pra mim
                opcao = str(input(f'Deseja mover os itens de {subpasta}? [S/N]: ')).strip().upper()
            except:  # Se der erro (TypeError, KeyboardError, etc)
                print('Opção inválida! Por favor, tente novamente!')
            else:  # Se não der esses erros, vamos analisar outros
                if opcao[0] not in 'SsNn':   # Se opção não estiver em 'SsNn'
                    print('ERRO! Por favor, digite uma opção válida')  
                else:  # Se estiver 
                    break 

        if opcao[0] in 'S':  # Se a opção for SIM
            print(f'Acessando pasta < {subpasta} >')
            moverArquivos(subpasta, sffx)  #  De novo aquela lógica maluca lá
        elif opcao[0] in 'N':  # Se a opção for NÃO
            continue  # Ignora a subpasta


def desfazer(pathstr, lst):
    """
    -> Função que desfaz qualquer alteração feita anteriormente.
    -> É a função moverArquivos com apenas uma linha trocada
    :param pathstr: Caminho da pasta Downloads em tipo str()
    :param lst: Lista de pastas criadas (retorno de mostrarArquivos())
    """

    from shutil import move
    from pathlib import Path
    
    subpastas = []
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
                caminhonovo = f'C:\\Users\\teteu\\Downloads\\teste\\{pasta}\\{item.name}'
                move(caminhoantigo, caminhonovo)  # Função move() da biblioteca Shutil
                print(f'Movendo < {item.name} > para < {pasta} > ')










#  PAREI AQUI, PRECISO COMENTAR A FUNÇÃO ABAIXO E FAZER UMA QUE DESFAZ ALTERAÇÕES





def removerVazios(pathstr):
    from pathlib import Path
    from os import rmdir

    downloadpath = Path(pathstr)
    n = 0
    for item in downloadpath.iterdir():
        if item.is_dir():
            try:
                rmdir(item)
            except OSError:
                continue
            else:
                n += 1
                
    print(f'Removi {n} pasta(s) vazia(s)!')

    #  C:\\Users\teteu\\Downloads\\pasta sffx\\subpasta pasta\\arquivo.any
    #  C:\\Users\\teteu\\Downloads\\{novo}\\{arquivo.any}
    # Usar .remove na pergunta das pastas a serem movidas
