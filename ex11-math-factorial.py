'''
Possuo 4 bolas amarelas, 3 bolas vermelhas, 2 bolas azuis e 1 bola verde. Pretendo colocá-las em um
tubo acrílico translúcido e incolor, onde elas ficarão umas sobre as outras na vertical. De quantas maneiras distintas
podemos formar essa coluna de bolas?

1) importar o módulo
2) criar uma variável e calcular o total de combinações. chamar a variável de C só para economizar espaço.
Lembre-se que o total de bolinhas e a quantidade de cada uma são dados no enunciado.


'''

import math
total = 4+3+2+1
n = math.factorial(total)
q1 = math.factorial(4)
q2 = math.factorial(3)
q3 = math.factorial(2)
q4 = math.factorial(1)
C = n/(q1*q2*q3*q4)
print(f"O total de combinações é {n}.")