# Big-O-notation
Estudando notação Big O com vídeo do freecodecamp

A notação Big O é usada para analisar a eficiência de um algoritmo à medida que sua entrada se aporxima do infinito. Que significa que, à medida que o tamanho da entrada do algoritmo cresce, quão drasticamente os requisitos de espaço ou tempo crescem com ele. 

Utilizando um exemplo: Uma dentista leva 30 minutos para cuidar de um paciente, então sabemos que a fórmula para saber quanto tempo ela irá levar para cuidar de todos os pacientes é 30 * o número de paciente, com isso podemos categorizar sua eficiência como linear, já que não ocorre variação é um valor constante. Na notação Big O dizemos Big O(n) onde n é igual ao número de pacientes. O valor do tempo que a dentista leva para atender cada paciente indifere na questão de aumentar de forma linear o tempo, ou seja, o tempo ser 30 minutos ou 3 horas, não modifica a forma com que o tempo irá aumentat somente será um tempo maior mas ele continuará aumentando de forma linear

No exemplo do arquivo1 temos Big O(1), pois é uma operação constante, multiplicar e imprimir leva sempre o mesmo tempo, independente do tamanho da entrada.

Uma constante é qualquer passo que não é dependente(escalonado) a entrada da função.

Para algoritmos que são constantes e independem 

No Big O temos uma hierarquia de crescimento:


<img src="https://github.com/user-attachments/assets/5e7f4fc0-3fe0-458e-8642-501220e5a8f1" width="300" height="400">


✅ O que Big O não é:
<ul>
  <li>Não te dá o tempo real de execução (tipo: "roda em 1 segundo").</li>
  <li>Ele não mede o tempo no relógio, porque isso depende de hardware, linguagem de programação, compilador, etc.</li>
</ul>



➡️ Ele mede o comportamento assintótico:
Quando o n cresce, como o algoritmo se comporta?
<ul>
  <li>Cresce linearmente (O(n))?</li>
  <li>Cresce quadraticamente (O(n²))?</li>
  <li>Cresce exponencialmente (O(2ⁿ))?</li>
</ul>

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
Quando você tem operações aninhadas, ou seja, uma dentro da outra, a complexidade se multiplica. Como no arquivo3.
Em O(n), para cada item, você faz uma ação só.
Em O(n²), para cada item, você precisa combinar ele com todos os outros itens.

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

<h3>Big O(n²)</h3>
