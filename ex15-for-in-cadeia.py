'''
Desenvolva uma função que receba como parâmetro uma cadeia de DNA e retorne uma cadeia complementar. A entrada e saída
de dados do programa deve ser feita no código principal.

1) Começamos o programa definindo a função cadeiaComplementar. Ela recebe como parâmetro uma cadeia de DNA e divide
uma das bases nitrogenadas presentes nela em uma lista listaQuimica, através da função split (dividir).

2) Utilizamos o comando for para percorrermos listaQuimica adicionando em fita2 a base nitrogenada correspondente
ao elemento obtido. Por exemplo, se o primeiro elemento de listaQuimica for "A", o primeiro elemento de fita2 deve ser
"I" e assim por diante.

3) Por fim, basta retornarmos fita 2 ao código principal.

4) Com a função cadeiaComplementar definida, podemos codificar o código principal, que consiste basicamentte em obter
a primeira sequência de bases nitrogenadas e passá-las como parâmetro para a função cadeiaComplementar. Em seguida,
o programa irá através de um comando for imprimir o conteúdo da lista fita2 (cadeia complementar de bases nitrogenadas)
obtida no retorno da função.

'''

def cadeiaComplementar(cadeia):

    fita1 = input()
    fita2 = cadeiaComplementar(fita1)

    for i in fita2:
        print(i,end = ' ')
