'''
Desenvolva uma função que receba uma frase como parâmetro e retorne uma nova frase onde todos os espaços originalmente
presentes sejam substituídos por "#". As entradas e saídas de dados devem ser realizadas no código principal.

1) definir a função substituiEspaco, que é responsável por pegar a frase recebida como parâmetro e utilizar o método
replace passando para o mesmo o que será substituído (espaço em branco) pelo o que será substituído (hashtag). Por fim,
a função simplesmente retorna a substituição realizada.

2) Com a função substituiEspaco definida, basta codificarmos o código principal, que consiste basicamente em requisitar
a entrada da frase, passar a mesma como parâmetro para a função substituiEspaco e imprimir a nova frase (em que os espaços
são substituídos por hashtags) obtida através do retorno da função.
'''

def substituiEspaco(frase):
    substituicao = frase.replace(' ', '#')
    return substituicao

frase = input()
novaFrase = substituiEspaco(frase)

print(novaFrase)