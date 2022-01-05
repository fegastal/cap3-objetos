''''
Uma rampa plana, de 36 m de comprimento, faz ângulo de 30º com o plano horizontal.
Uma pessoa que sobe a rampa inteira eleva-se verticalmente quantos metros?
'''

import math
angulo = math.radians(30)
H = math.sin(angulo) * 36
print("A altura é %.2f metros."%(H))
