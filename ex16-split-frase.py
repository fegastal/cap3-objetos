'''
Desenvolva uma função que receba como parâmetro uma frase e seja capaz de retornar o número de palavras que ela contém.
As entradas e saídas de dados do programa devem ser feitas no código principal (main).

1) Definir a função countPalavras, que basicamente utiliza o método split (dividir) para separar cada uma das
palavras da frase recebida como parâmetro em uma lista aux. Após isso, utiliza outro método, chamado len, para retornar
ao código principal a quantidade de elementos da lista (quantidade de palavras da frase).

2) Com a função countPalavras definida, podemos codificar o código principal, que basicamente consiste em ler a frase
digitada pelo usuário, passar a mesma como parâmetro para a função countPalavras e imprimir na tela o retorno obtido
(número de palavras da frase).

'''

def countPalavras(frase):
    i = 0
    aux = frase.split()

    return len(aux)

frase = input()
qtdPalavras = countPalavras(frase)
print(qtdPalavras)