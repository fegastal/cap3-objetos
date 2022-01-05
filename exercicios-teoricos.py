""""Exercícios Teóricos | Capítulo 03

1) O que entende por programação descendente?

Construção do topo para a base: decompõe-se um dado problema em subproblemas, cada um dos quais é resolvido
usando a mesma abordagem reducionista, até chegarmos a problemas que se podem resolver de modo direto
com as construções da linguagem.

2) O que são objetos imutáveis?

Tuplos, por exemplo, são objetos imutáveis (não somente eles, mas também números, cadeias de caracteres, range) e não é
possível alterar o seu valor sem alterar a sua identidade, criando, assim, um novo objeto. A solução para esse
problema seria criar uma nova cadeia e associar o objeto resultante ao mesmo nome.

4) O que é range?

range() é uma função interna do Python. É usado quando um usuário precisa executar uma ação por um determinado
número de vezes. É comumente usado em looping. O uso mais comum é iterar o tipo de sequência (Lista, string etc.)
com o loop for e while.

Permite ao usuário gerar uma série de números dentro de um determinado intervalo. Dependendo de quantos
argumentos o usuário está passando para a função, o usuário pode decidir onde essa série de números começará
e terminará, bem como quão grande será a diferença entre um número e o próximo.
range()leva principalmente três argumentos.


5) Qual é a diferença entre a função range (ALCANCE) com um argumento, dois argumentos ou três argumentos?

START: inteiro a partir do qual a sequência de inteiros deve ser retornada

STOP: inteiro antes do qual a seqüência de inteiros deve ser retornada.
O intervalo de inteiros termina na parada - 1.

ETAPA / STEP: valor inteiro que determina o incremento entre cada inteiro na sequência

range(stop) leva um argumento.
range(start, stop) leva dois argumentos.
range(start, stop, step) leva três argumentos.

a) UM ARGUMENTO:
Quando o usuário chama range() com um argumento, o usuário obtém uma série de números que começa em 0
e inclui todos os números inteiros até, mas não incluindo, o número que o usuário forneceu como parada.
Obs: o número de parada não conta.

ex:

for i in range(6):
    print(i, end =" ")
1, 2, 3, 4, 5

b) DOIS ARGUMENTOS:

Quando o usuário chama range() com dois argumentos, o usuário pode decidir não apenas onde a série
de números termina, mas também onde começa, de forma que o usuário não precise começar do zero o tempo todo.
O usuário pode usar range()para gerar uma série de números de X a Y usando um intervalo (X, Y).

exemplo: python range (0, 6): 1, 2, 3, 4, 5

c) TRÊS ARGUMENTOS:

Quando o usuário chama range()com três argumentos, o usuário pode escolher não apenas onde
a série de números começará e terminará, mas também quão grande será a diferença entre um número e o
próximo. Se o usuário não fornecer uma etapa, range() se comportará automaticamente como se a etapa fosse 1.

Neste exemplo, estamos imprimindo um número par entre 0 a 10, então escolhemos nosso ponto de
partida de 0 (início = 0) e paramos a série em 10 (parada = 10). Para imprimir um número par,
a diferença entre um número e o próximo deve ser 2 (etapa = 2). Após fornecer uma etapa, obtemos
a seguinte saída (0, 2, 4, 8).


6) O que é uma variável com o papel de contador?

Uma variável com papel de contadora tem o papel de contar
as repetições executadas por um laço, sendo ela a responsável
pela parada do mesmo na maioria das vezes, uma vez que a mesma é
incrementada a cada loop até o momento que torna a condição de execução do lado falsa.

Vale lembrar que a codificação ruim das instruções envolvendo a variável contadora
podem ocasionar o que chamamos de LOOP INFINITO, que é quando a condição de execução do laçode
repetição nunca se torna falsa.


7) O que é uma variável com o papel de acumulador?

Imagine uma calculadora simples, dispondo de apenas um mostrador e apenas 4 operações (somar, subtrair, multiplicar e dividir).
Se desejamos computar o gasto mensal com a padaria, devemos digitar sequencialmente os valores gastos,
um a um, seguido do operador de soma +, sendo que ao final teclamos =. Vamos supor que os valores dos
gastos foram 5, 2, 3, 5 e 3. Mas como foi possível obter a soma de todos os valores? Isso só foi possível
por existir um "acumulador" (AC) para armazenar o primeiro valor digitado e depois disso, esse mesmo "acumulador"
teve um novo valor a ele adicionado (ou acumulado): AC := 5, depois AC := 5+2 = 7. depois AC := 7+3 = 10. depois
AC := 10+5 = 15 e por último AC := 15+3 = 18.

Podemos pensar que calculadora está fazendo o papel da Unidade Lógico Aritmética (Arithmetic logic unit (ALU) em Inglês)
de um computador. O recurso da calculadora que armazena os valores computados (que denotamos por AC) seria o
equivalente a um registrador ou a uma posição de memória em um computador. Para se ter uma noção da diferença,
deve-se notar que um computador moderno dispõe de vários registradores e o que tem sido denominado memória,
ordens de grandeza maiores que os registradores, hoje compra-se computadores com ao menos 4 Gb de memória
RAM (Gb = giga bytes = 1 bilhão de bytes)

Deve-se destacar que o valor armazenado em um registrador ou na memória pode ser alterado, podendo-se
dizer que esses valores variam, vindo dai seu nome de variável.

Para nomear as variáveis, pode-se usar qualquer combinação de letras e números (iniciando por uma letra).

Existe a necessidade de declarar qual é o tipo da variável, em uma linguagem de programação como C
isso deve ser feito de modo explicito. Por outro lado, a linguagem Python não dispõe de um mecanismo para
indicar o tipo de variável explicitamente, pois a primeira atribuição usando um nome funciona como declaração.


8) Como se pode modificar uma cadeia de caracteres obtendo uma nova?

É necessáro construir uma nova cadeia de caracteres e associar o objeto resultante ao mesmo nome, uma vez
que tuplos, números, cadeias de caracteres e os range são imutáveis.


9) O que significa fatiamento?

É uma forma de obter elementos contíguos da cadeia ou a sequência de elementos espaçados regularmente. Usamos agora
a notação [inf:sup], no primeiro caso, e [inf:sup:step], no segundo caso.
ex: cadeia = 'Homem Aranha'
cadeia [1:4]
'ome'
cadeia [-6;-2]
'Aran'
cadeia[:5]
'Homem'
cadeia[1:7:2]
'oe '
cadeia[::-1] = situação inversa
'ahnarA memoH'


10) Qual é o construtor do tipo cadeia de caracteres?

É o recurso à plicas, que podem ser simples, duplas ou triplas. As últimas permitem escrever longas cadeias
de caracteres, que se propagam por mais do que uma linha, sendo, por isso, muito usadas para comentar o código.
Cadeias são sensíveis ao caso. "alma" e "Alma" são objetos diferentes.


9) Que diferenças existem entre os métodos find e index?

Em Python, encontrar o índice de uma substring em uma string pode ser localizado pela função embutida do python
usando find() ou index(). Ambos retornam o índice inicial da substring em uma string, se ela existir.

a) O método index() retorna o índice de uma substring ou char dentro da string (se encontrado). Se a substring
ou char não for encontrado, ele gerará uma exceção.
string.index (<substring>)

Retorna uma exceção se a substring não for encontrada
Não deve ser usado se você não tiver certeza sobre a presença da substring
Isso pode ser aplicado a strings, listas e tuplas
Não pode ser usado com declaração condicional


b) O método find() retorna o índice da primeira ocorrência da substring ou char (se encontrado).
Se não for encontrado, retorna -1.
string.find (<substring>)

Retorna -1 se substring não for encontrada
É a função correta a ser usada quando você não tem certeza sobre a presença de uma substring
Isso só pode ser aplicado a strings
Pode ser usado com uma instrução condicional para executar uma instrução se uma substring for encontrada também se não for

"""