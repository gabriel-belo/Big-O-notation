# Big-O-notation
Estudando notação Big O com vídeo do freecodecamp

A notação Big O é usada para analisar a eficiência de um algoritmo à medida que sua entrada se aproxima do infinito. Que significa que, à medida que o tamanho da entrada do algoritmo cresce, quão drasticamente os requisitos de espaço ou tempo crescem com ele. 

Uma constante é qualquer passo que não é dependente(escalonado) a entrada da função.
Constantes são valores fixos que indiferem da entrada.

No Big O temos uma hierarquia de crescimento:

<img src="https://github.com/user-attachments/assets/5e7f4fc0-3fe0-458e-8642-501220e5a8f1" width="300" height="400">

✅ O que Big O não é:
<ul>
  <li>Não te dá o tempo real de execução (tipo: "roda em 1 segundo").</li>
  <li>Ele não mede o tempo no relógio, porque isso depende de hardware, linguagem de programação, compilador, etc.</li>
</ul>


<h3>Big O(1)</h3>
No exemplo do arquivo2 temos Big O(1), pois é uma operação constante, multiplicar e imprimir leva sempre o mesmo tempo, independente do tamanho da entrada.
Para algoritmos que são constantes e independem de qualquer variável n.

<h3>Big O(n)</h3>
Em O(n), para cada item, você faz uma ação só.

Utilizando um exemplo: Uma dentista leva 30 minutos para cuidar de um paciente, então sabemos que a fórmula para saber quanto tempo ela irá levar para cuidar de todos os pacientes é 30 * o número de paciente, com isso podemos categorizar sua eficiência como linear, já que não ocorre variação é um valor constante. Na notação Big O dizemos Big O(n) onde n é igual ao número de pacientes. O valor do tempo que a dentista leva para atender cada paciente indifere na questão de aumentar de forma linear o tempo, ou seja, o tempo ser 30 minutos ou 3 horas, não modifica a forma com que o tempo irá aumentat somente será um tempo maior mas ele continuará aumentando de forma linear



<table border="1" cellspacing="0" cellpadding="8">
  <thead>
    <tr>
      <th>Conceito</th>
      <th>Exemplo do Dia a Dia</th>
      <th>Analogia Big O</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tempo</td>
      <td>Cozinhar um prato para n pessoas</td>
      <td>
        Quantas ações você vai fazer (picar legumes, mexer panela).<br>
        Se o tempo cresce com n, é O(n).<br>
        Se cada pessoa pede um prato diferente e você faz n x n pratos, é O(n²).
      </td>
    </tr>
    <tr>
      <td>Espaço (memória)</td>
      <td>Mesa de jantar para n pessoas</td>
      <td>
        Quantas cadeiras/pratos/talheres você precisa colocar na mesa.<br>
        Se precisa de um prato por pessoa → O(n).<br>
        Se você colocar um prato para cada combinação de entrada e prato principal → O(n²).
      </td>
    </tr>
  </tbody>
</table>

<h3>Big O(n²)</h3>

Em O(n²), para cada item, você precisa combinar ele com todos os outros itens. No exemplo podemos ver que o print() ocorre 16 vezes, pois sua entrada é 4 dando assim 4², isso isgnifica que O(n²), pois o bloco de código tem dois loops for aninhados que geral esta repetição que gera o quadrado do valor da entrada.

Exemplo:
O(n²) → Mandar cartas para todos os vizinhos
Agora, você quer que cada pessoa da sua rua envie cartas para todos os outros vizinhos.
➡️ O João manda carta pro Pedro, pro Carlos, pra Maria...
➡️ A Maria também manda carta pro João, pro Pedro, pro Carlos...

🔸 Se tiver 10 pessoas na rua:

Cada pessoa vai mandar 10 cartas (inclusive pra si mesma ou não).
Vai dar 10 x 10 = 100 cartas!
🔸 Se tiver 100 pessoas, seriam 100 x 100 = 10.000 cartas!
🔸 Quadrado da entrada!
Isso é O(n²) → cada item interage com todos os outros itens.

<h3>Big O(n³)</h3>

O que significa O(n³)?
Significa que o número de operações (ou o tempo para resolver um problema) cresce com o cubo do tamanho da entrada (n³).
Se n dobra, o número de operações aumenta 8 vezes (2³ = 8).

✅ Por que O(n³) acontece?
Porque você tem 3 níveis de repetição:

Um loop dentro de outro loop, dentro de outro loop.
Ou você está fazendo três passos dependentes entre si, onde cada passo depende de n elementos.
👉 Toda vez que, para cada item, você precisa fazer um trabalho com cada outro item, para cada outro item de novo, temos O(n³).

Cada etapa depende da anterior.

Como cada uma das 3 etapas tem n opções, você tem n³ possibilidades para considerar, planejar ou calcular.

Por exemplo: Você não pode decidir o palestrante antes de escolher local e horário.

exemplo simples:
🔸 Montar uma caixa de combinações
<ul>
  <li>Você tem n tipos de pão.</li>
  <li>Para cada pão, tem n tipos de recheio.</li>
  <li>Para cada recheio, tem n tipos de molho.</li>
</ul>

👉 Se você quiser listar todas as combinações possíveis de sanduíche:
<ul>
  <li>Para cada pão → n recheios → n molhos.</li>
  <li>Total de combinações: n × n × n = n³.</li>
</ul>

Se você tiver 5 pães, 5 recheios e 5 molhos, são 5³ = 125 combinações!

<h3>O(log n)</h3>

<h4>log n é quantas vezes você consegue dividir um número por 2 até chegar em 1.</h4>

Um logaritmo é a potência à qual um número precisa ser elevado para obter outro número
Em ciência da computação, a menos que especificado de outra forma, podemos sempre assumir que o número que queremos elevar à potência da soma é dois.

Em termos simples, log n é o número de vezes que você pode dividir n por 2 antes de chegar a 1.

O que O(log n) indica sobre o algoritmo?
Significa que a cada passo a quantidade de dados que você precisa considerar diminui pela metade, e o número de passos necessários cresce muito devagar, mesmo que n aumente bastante.

Exemplos clássicos de algoritmos O(log n):

Busca Binária: Em uma lista ordenada, você compara o elemento do meio e elimina metade da lista a cada tentativa. A cada passo, o espaço de busca é dividido por 2.

Algumas operações em árvores balanceadas (como AVL ou Red-Black Tree): Operações como inserção, remoção e busca costumam ser O(log n) porque a altura da árvore cresce logaritmicamente em relação ao número de elementos.

Exemplo: 
?^?= 8 de acordo com a afirmação acima temos 2^?=8
Em outra forma isto é Log2 8=?
o dois é a base

No exemplo em arquivo5 iniciamos chamando a função com logFunc(8) depois a chamamos novamente com logFunc(4) e depois a chamamos novamente com logFunc(2) e então a chamamos novamente com logFunc(1) e depois temos o caso base, temos então três niveis neste caso: nível 1 de logFunc(8) para logFunc(4), nível 2 logFunc(4) para logFunc(2) e nível 3 logFunc(2) para logFunc(1).

Então como multiplicação é o inverso da divisão podemos ver o resultado da potência 2³ fazendo 1x2x2x2=8

<table border="1" cellpadding="8" cellspacing="0">
  <caption><strong>Resumindo a diferença</strong></caption>
  <thead>
    <tr>
      <th>Iterativo</th>
      <th>Recursivo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Usa loops (<code>for</code>/<code>while</code>)</td>
      <td>Usa chamadas de função (recursão)</td>
    </tr>
    <tr>
      <td>Menos consumo de memória (sem pilha de chamadas)</td>
      <td>Mais consumo de memória (pilha de chamadas recursivas)</td>
    </tr>
    <tr>
      <td>Geralmente mais performático</td>
      <td>Pode ser mais fácil de entender, dependendo do caso</td>
    </tr>
    <tr>
      <td>Exemplo: <code>busca_binaria_iterativa</code></td>
      <td>Exemplo: <code>busca_binaria_recursiva</code></td>
    </tr>
  </tbody>
</table>


<h3>O(log n) iterativo</h3>

Utilizamos o mesmo exemplo porém fazendo de forma iteratica, teremos 2.2.2=8= 2³ e se podemos multiplicar 2 3 vezes para chegar a oito, se fizermos o caminho inverso se dividirmos 8 por dois três vezes chegamos a 1.
Para saber o n em o O(log n) precisamos olhar a quantidade de iterações necessárias para  chegar a menor quantidade possível.

<h3>Busca binária & O(log n)</h3>

Se você não avança (+1) ou não recua (-1), você não elimina nada.
Você vai sempre cair no mesmo valor de meio e vai repetir a chamada infinita.

<h3>O(n log n)</h3>
O(n log n ) é nada mais que O(n * log n)
Então nós temos um loop maior que tem O(log n) e dentro deste temos um loop O(n) e multiplacando os dois nós temos a quantidade de vezes que o bloco de código no loop interno será executado. No caso do exemplo temos n= 4 então O(n)= O(4) e O(log n) = O(2) que 4 * 2= 8.

<h4>Análise do código no arquivo 10</h4>
Como funciona o tempo de execução do MergeSort?
O mergeSort tem duas partes principais:
Dividir a lista no meio (recursão)
Mesclar (merge) as listas ordenadas
A complexidade total vem dessas duas etapas combinadas.

1️⃣ Divisão: Quantas vezes a lista é dividida?
Cada vez que você divide a lista, você parte ela no meio.
Isso acontece até sobrar uma lista de 1 elemento.
Se a lista tem n elementos, quantas vezes dá para dividir por 2?
➡ log n vezes! (base 2, porque é sempre metade)

Então, o número de níveis de divisão da árvore recursiva é log n.

2️⃣ Mesclagem (merge): Quanto tempo demora em cada nível?
Em cada nível, você percorre todos os n elementos para combinar (merge) as listas ordenadas.
Mesmo com várias listas pequenas, a soma dos tamanhos delas sempre dá n elementos no nível atual.

➡ Ou seja, cada nível da árvore custa O(n) para fazer o merge.

3️⃣ Multiplica as duas coisas:
log n níveis de recursão
Em cada nível, o custo é O(n)

De onde vem o log n?
Vem da profundidade da árvore de chamadas recursivas (quantas vezes a lista é dividida).
De onde vem o n?
Vem da quantidade de elementos processados em cada merge (passa pela lista inteira a cada nível).


<h3>O(2^n)</h3>
<h4>Fibonacci & Complexidade exponencial</h4>
Em cada nível o número de chamadas para a função Finonacci aumenta exponencialmente

No caso do algoritmo no arquivo 11 temos O(2^n-1) porém como ignoramos constantes no Big O temos O(2^n)

É quando o número de operações dobra toda vez que você aumenta a entrada em 1.

👉 Se você tem n = 1, são 2¹ = 2 operações
👉 Se n = 2, são 2² = 4 operações
👉 Se n = 3, são 2³ = 8 operações
👉 Se n = 10, são 2¹⁰ = 1024 operações!

O crescimento é exponencial, ou seja, explode muito rápido.

Por isso, O(2ⁿ) é considerado muito custoso em termos de tempo de execução.

<h4>Exemplo do dia a dia</h4>
Imagina uma árvore de decisões, como:

Você está jogando um jogo de perguntas, onde:
<ol>
  <li>Cada pergunta tem 2 respostas possíveis: sim ou não.</li>
  <li>E cada resposta leva a outra pergunta, que tem 2 novas respostas… e assim vai.</li>  
</ol>

Se você tem 1 pergunta inicial, só tem 2 opções.

Mas se você tem n perguntas em sequência, o número de caminhos possíveis será 2ⁿ.

<ul>
  <li>1 pergunta → 2 possibilidades</li>
  <li>2 perguntas → 4 possibilidades</li>
  <li>3 perguntas → 8 possibilidades</li>
  <li>10 perguntas → 1024 possibilidades </li>
</ul>

A quantidade de trabalho dobra a cada novo nível!

<h4>Como saber que é O(2ⁿ)?</h4>
<ol>
  <li>A cada etapa, o número de operações dobra.</li>
  <li>Não é linear (O(n)) e nem quadrático (O(n²)) porque o crescimento é muito mais rápido.</li>
  <li>
    Geralmente aparece em:
    <ul>
        <li>Algoritmos de recursão sem otimização.</li>
        <li>Árvores binárias que exploram todos os caminhos possíveis.</li>
        <li>Problemas de combinações ou subconjuntos (subset problems).</li>
        <li>Alguns algoritmos de backtracking, força bruta e DFS em árvores.</li>
    </ul>
  </li>
</ol>








<h3>O(n!)</h3>
<h4>Fatorial</h4>

O que significa O(n!)?
👉 O(n!), ou fatorial de n, representa um crescimento extremamente rápido, até mais rápido que O(2ⁿ).
👉 Quando você vê O(n!), está lidando com problemas que precisam explorar todas as possíveis ordens, sequências ou combinações de n elementos, sem atalhos.

Exemplo do dia a dia (sem código!)
🎲 Organizando pessoas ou objetos
Imagina que você vai organizar 5 livros diferentes em uma prateleira.

Quantas ordens diferentes você pode organizar esses livros?
A resposta é 5! = 120 ordens possíveis.

Exemplo em algoritmos (O(n!) aparece onde?)

Permutação de elementos:
Exemplo: gerar todas as ordens possíveis de n itens diferentes.

Problemas de força bruta:
Quando você testa cada sequência possível sem atalhos ou regras de corte.

Problemas clássicos:

Caixeiro Viajante (TSP): encontrar a menor rota que passa por várias cidades e volta ao ponto inicial (modo força bruta testa n! rotas).

Permutação de senhas, combinando diferentes elementos.


<h2>Big O para múltiplas entradas</h2>
Quando você tem mais de uma entrada em uma função e precisa analisar a complexidade de tempo (Big O) dela, o valor de 
𝑛 geralmente se refere ao número de entradas ou ao tamanho das entradas que dominam o comportamento da função.

1.Várias entradas independentes: Se a função recebe várias entradas independentes, como por exemplo, 𝑛 e 𝑚, onde 𝑛 é o tamanho de uma lista e 𝑚 é o tamanho de outra, o Big O da função geralmente depende de como essas entradas afetam o desempenho da função. O tempo de execução é expresso em termos de 𝑛 e m, e você pode representar o Big O como uma combinação das duas variáveis. Por exemplo:
<ul>
  <li>Se o tempo de execução é diretamente proporcional a 𝑛 e 𝑚, a complexidade seria 𝑂(𝑛⋅𝑚).</li>
  <li>Se uma das variáveis é muito maior que a outra, você pode simplificar para a maior delas. Por exemplo, se 𝑛 é muito maior que 𝑚, o tempo de execução seria aproximadamente O(n).</li>
</ul>

2.Entradas relacionadas (como vetores ou matrizes): Se as entradas forem vetores ou matrizes, o tamanho 𝑛 pode ser interpretado de formas diferentes dependendo de como você define as dimensões.
<ul>
  <li>Para uma matriz de tamanho 𝑛 × 𝑚, o Big O geralmente é 𝑂(𝑛 ⋅ 𝑚), pois o algoritmo pode precisar percorrer todos os elementos da matriz.</li>
  <li>Se você tiver um vetor de vetores, o Big O pode depender do número de elementos e do número de vetores.</li>
</ul>
Vamos analisar diferentes cenários e como calcular o Big O em cada um deles:

Suponha que você tenha:

n: O número de vetores (o número de listas dentro da lista principal).
m: O número máximo de elementos em qualquer um dos vetores internos. É importante notar que os vetores internos podem ter tamanhos diferentes.
Cenários Comuns e seus Big O:

Acessar um elemento específico:

Para acessar um elemento em uma posição específica (por exemplo, o elemento na linha i e coluna j), você precisa realizar um acesso ao vetor externo (índice i) e depois um acesso ao vetor interno (índice j). Ambas as operações levam tempo constante, O(1).
Big O: O(1)
Iterar por todos os elementos:

Para visitar cada elemento em todos os vetores internos, você precisará de um loop externo para percorrer os n vetores e um loop interno para percorrer os elementos de cada vetor.
No pior caso, cada vetor interno terá m elementos.
Big O: O(n * m)
Encontrar um elemento específico (sem saber a posição):

Você precisará percorrer todos os vetores e, dentro de cada vetor, verificar cada elemento até encontrar o desejado (ou percorrer todos sem encontrar).
No pior caso, você terá que verificar todos os n * m elementos.
Big O: O(n * m)
Adicionar um elemento ao final de um vetor interno específico:

Se você souber qual vetor interno adicionar o elemento, a operação de adicionar ao final de um vetor (geralmente usando append ou similar) geralmente leva tempo constante, O(1) em média (devido à alocação dinâmica de memória).
Big O: O(1) (em média)
Inserir um elemento no meio de um vetor interno específico:

Inserir um elemento no meio de um vetor interno requer deslocar todos os elementos subsequentes para abrir espaço. No pior caso (inserir no início), isso levará um tempo proporcional ao número de elementos restantes no vetor interno.
Big O: O(m) (no pior caso, para um vetor interno)
Ordenar cada vetor interno:

Se você precisar ordenar cada um dos n vetores internos, e cada vetor tem no máximo m elementos, usando um algoritmo de ordenação eficiente como o mergesort ou o quicksort, a complexidade para ordenar um único vetor será O(m log m).
Como você faz isso para n vetores, a complexidade total será:
Big O: O(n * m log m)
Considerações Importantes:

Relação entre n e m: O Big O final dependerá da relação entre n e m.

Se o número de vetores for constante e o tamanho dos vetores internos variar, o Big O pode ser expresso em termos de m.
Se o tamanho dos vetores internos for limitado por uma constante e o número de vetores aumentar, o Big O pode ser expresso em termos de n.
Em muitos casos, ambos n e m podem variar, então a complexidade será expressa em função de ambos.
Operação específica: O Big O sempre se refere a uma operação específica que você está realizando no vetor de vetores. Diferentes operações terão complexidades diferentes.

Melhor Caso, Pior Caso e Caso Médio: Assim como para estruturas de dados unidimensionais, as operações em vetores de vetores também podem ter diferentes complexidades dependendo do melhor, pior e caso médio. As análises acima geralmente focam no pior caso, que é o mais comum para descrever a limitação superior do desempenho.

