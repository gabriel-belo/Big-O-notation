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

Um logaritmo é a potência à qual um número precisa ser elevado para obter outro número
Em ciência da computação, a menos que especificado de outra forma, podemos sempre assumir que o número que queremos elevar à potência da soma é dois.
Exemplo: 
?^?= 8 de acordo com a afirmação acima temos 2^?=8
Em outra forma isto é Log2 8=?
o dois é a base

No exemplo em arquivo5 iniciamos chamando a função com logFunc(8) depois a chamamos novamente com logFunc(4) e depois a chamamos novamente com logFunc(2) e então a chamamos novamente com logFunc(1) e depois temos o caso base, temos então três niveis neste caso: nível 1 de logFunc(8) para logFunc(4), nível 2 logFunc(4) para logFunc(2) e nível 3 logFunc(2) para logFunc(1).

Então como multiplicação é o inverso da divisão podemos ver o resultado da potência 2³ fazendo 1x2x2x2=8


