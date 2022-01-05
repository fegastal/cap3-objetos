'''
Elabore um programa que receba três valores reais, A, B e C, e calcule as raízes dessa
equaçã de segundo grau. Para isso, deve usar obrigatoriamente uma função chamada bhaskara,
escrita por você, que recebe os coeficientes como parâmetro. Além disso, a função deve calcular
e retornar as duas raízes, reais ou complexas, dependendo dos coeficientes. O módulo
utilizado deve ser chamado de m e deve existir apenas no escopo da função.
'''

def bhaskara(a,b,c):
    delta = b**2-4*a*c
    if delta < 0:
        import cmath as m
    else:
        import math as m
    r1 = -b+m.sqrt(delta)/(2*a)
    r2 = -b-m.sqrt(delta)/(2*a)
    return r1, r2

a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))
r1, r2 = bhaskara(a,b,c)
print(f"As raízes são: {r1} e {r2}.")