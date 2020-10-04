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
def mostrarArquivos(caminho):

    from pathlib import Path
    # Caso queira ver o que está intrínseco na função, adicione os comandos comentados (coloque cores).

    caminho = Path(caminho)  # Caminho como objeto
    subpastas = []  # Lista subpastas vazia
    print(f' Analisando < {caminho} > ') 
    for item in caminho.iterdir():  # Para cada item no caminho iterável
        if item.is_dir():  # Se o item for uma pasta
            subpastas.append(item)  # Adiciona na lista de subpastas
            continue  
            # Volta pro começo da iteração, ignorando o resto do processo
        print(f' {item.name} ')  # Se não for pasta, é arquivo, então mostra o nome
        # print(subpastas)

    for subpasta in subpastas:  # Para cada subpasta na lista subpastas
        # print(subpastas)
        # print(subpasta)
        mostrarArquivos(subpasta)        

# ===================================== Obrigado @robsonpiere! ===========================================#

        # Por algum motivo, o Python guarda a primeira ocorrência da lista subpastas, fazendo com que várias variáveis subpastas 
        # temporárias existam. Eu não entendi a lógica dessa função, pensei em algo parecido, mas não nessa linha de pensamento
        # Buscarei explicações para o que acontece aqui.

    #  Não é possível usar o enumerate porque ele vai contar os diretórios e não printá-los, fazendo com que o índice fique com buracos
    #  As vezes o intellisense buga no Pycharm e aqui
    #  Variável .name
    
# =======================================================================================================#