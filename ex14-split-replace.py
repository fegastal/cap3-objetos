'''
Escreva uma função que receba uma frase e uma palavra. A função deve ser capaz de retornar a frase original,
mas com a última palavra da frase substituída pela palavra nova. As entradas e saídas do programa devem ser realizadas
no código principal.

1) Começamos o programa definindo a função responsável por realizar a troca da última
palavra da frase recebida como parâmetro pela nova palavra (também recebida como parâmetro):
Temos, basicamente, a função de substituir que recebe f(frase) e p(nova palavra) como parâmetros.

2) Atribuímos a uma variável aux uma lista com a separação de cada palavra da frase f (pode ser feito pelo método split).

3) Atribuímos a variável ultimaPalavra o último elemento da lista armazenada em aux, que nada mais é do que a última
palavra da frase original.

4) Utilizamos o método replace para substituir ultimaPalavra (última palavra da frase original) por p (nova palavra
recebida como parâmetro) e retornamos isso ao programa principal.

5) Com a função substituir definida, pode-se codificar o programa principal. Basicamente, requisita ao usuário a entrada
da frase e da nova palavra, atribui a novaFrase o retorno obtid na chamada da função substituir passando como parâmetros
frase e palavra substituída pela nova palavra).

'''

def substituir(f, p):
    aux = f.split()
    ultimaPalavra = aux[-1]
    return f.replace(ultimaPalavra, p)

frase = input("Frase: ")
palavra = input("Palavra: ")

novaFrase = substituir(frase, palavra)

print(novaFrase)
