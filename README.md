<h1>ROLA DADOS</h1>
<h4>Seu RPG mais digital</h4>
:arrow_right: Crie equações para suas rolagens e em segundos tenha o resultado, sem se preocupar em interromper a aventura
<h2> :bullettrain_side: Simplicidade</h2>
<h4>Clique nas opções, sem complicações</h4>
:arrow_forward: Teclas específicas para dados -- D20,D12,D10,D8,D6,D4
<br>
:arrow_forward: Teclas númericas de 0 a 9
<br>
:arrow_forward: Teclas de operações
<br>
:arrow_forward: Clique em rolar após escrever as equações e limpar para retornar ao estado inicial
<h2>Rodar</h2>
<h4>Acesse o diretorio onde estão as classes e digite o comando python3 main.py</h4>
<h2>Como funciona</h2>
:arrow_forward:Main.py
<h4>Aqui se importa todas as outras classes e as instânciam</h4>
:arrow_forward: ClasseBotaoDado.py
<h4>Essa classe tem a função de servir de molde para os botões de dados, assim não precisa ficar repetindo o codigo Tkinter </h4>
:arrow_forward: ClasseNumeroBotao.py
<h4>Essa classe é um molde para os botões númericos, fazendo assim não é necessario repetir 10 vezes</h4>
:arrow_forward: ClasseVisor.py
<h4>Aqui temos uma classe que recebe os valores inseridos pelo teclado, essa classe também tem dois metodos que regulam o que está sendo mostrado na tela</h4>
:arrow_forward: Funcionalidades.py
<h4>Essa classe é responsavel pelas principais funções do software</h4>
<li>"Encaminha" retira a parte não númerica do botão Dado e encaminha o valor para "Sortea"</li>
<li>"Sortea" gera um numero baseado no valor do botão dado passado por "Encaminha"</li>
<li>"Opera" calcula tudo e limpa a tela</li>
