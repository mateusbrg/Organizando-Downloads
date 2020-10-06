# Organizador de Downloads
Uma ferramenta que limpa a bagunça da sua Pasta Downloads! 📁⏬ 

---
Após terminar os três módulos do [Curso de Python 3](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6), disponível no canal [Curso em Vídeo](https://www.youtube.com/user/cursosemvideo) do Youtube, pensei em ferramentas que pudessem me ajudar no dia a dia. Foi quando eu abri minha pasta Downloads.

Aquela bagunça encontrada me levou a pensar não só em como automatizar a organização, mas também em como ajudar outras pessoas com essa tarefa. Assim nasceu o meu primeiro grande projeto!

---
## Funcionamento

Baseado nas bibliotecas `OS`, `pathlib` e `shutil` built-ins da linguagem, o projeto foi construído 100% em Python e organiza os arquivos de acordo com o tipo deles (.exe, .pdf, etc). Foi excelente para treinar todos os conceitos vistos no Curso de Python 3 do Professor Guanabara.

## Instalação

Para você que só quer usar o programa, não é necessário nenhuma instalação! Basta baixar e executar a ferramenta.

Baixe o instalador para Windows (.exe) [clicando aqui]

### Para você desenvolvedor, siga os passos abaixo:



Antes de qualquer coisa, você precisa ter o [Python](https://www.python.org/downloads/) instalado na máquina.

Também será necessário instalar a biblioteca `colorama`, para que as cores no terminal funcionem. Instale com `pip` ou com outro gerenciador de pacotes PyPi:

```
pip install colorama
```

Após a instalação da biblioteca, o programa pode ser executado através do arquivo **main.py**

## Execução

### Antes
![ANTES](https://raw.githubusercontent.com/mateusbrg/Organizando-Downloads/master/img/Antes.png)
### Depois
![DEPOIS](https://raw.githubusercontent.com/mateusbrg/Organizando-Downloads/master/img/Depois.png)

## Issues conhecidas

* O programa NÃO roda em sistemas [UNIX](https://pt.wikipedia.org/wiki/Unix). Futuramente pretendo portabilizá-lo, mas fica em aberto para contribuições da comunidade.
* O programa não funcionará se sua pasta de Downloads tiver um nome diferente do padrão do sistema.
* Atualizações futuras nas bibliotecas `pathlib`, `shutil` e `os` podem inviabilizar a ferramenta, fazendo-se necessário uma atualização.
* O programa pode bagunçar arquivos de jogos e outros programas não-instaláveis presentes na pasta Downloads. O mesmo pergunta se você quer "organizar" essas subpastas, então tome cuidado!

---
## Contribuições
Encontrou algum problema? Fique à vontade e contribua! Será um prazer falar com você e poder aprender mais sobre Python e programação!


## Agradecimentos

Agradeço imensamente ao usuário [robsonpiere](https://github.com/robsonpiere) que disponibilizou um [Gist aqui no GitHub](https://gist.github.com/robsonpiere/fc256f6e7b7301d2d12343372cde93f9) com uma função para listar pastas e subpastas. Me ajudou muito! Muito Obrigado!

### Fontes e Links úteis

* [Documentação biblioteca os](https://docs.python.org/3/library/os.html)
* [Documentação biblioteca pathlib](https://docs.python.org/3/library/pathlib.html)
* [Documentação shutil](https://docs.python.org/3/library/shutil.html)
* [Documentação colorama](https://pypi.org/project/colorama/)

## Licença
MIT License © 2020 [Mateus Braga](https://github.com/mateusbrg)
