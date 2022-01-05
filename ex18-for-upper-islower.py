'''
Faça um programa que receba como entrada uma frase e imprima essa frase substituindo os caracteres maiúsculos por minúsculos
e vice-versa.

1) Ele é praticamente todo feito dentro de uma estrutura FOR.

2) Saber usar os métodos de string islower (verifica se todos os caracteres são minúsculos), lower (cria uma cópia de
uma string com todos os caracteres minúsculos) e upper (cria uma cópia de uma string com todos os caracteres maiúsuculos).

3) Percorre cada caractere da string frase utilizando o método ISLOWER para verificar se o carac é minúsculo. Caso seja,
utilizamos o MÉTODO UPPER. Senão, o MÉTODO LOWER para realizarmos a impressão desse caractere em minúsculo.
'''

frase = input()

for char in frase:
    if char.islower():
        print(char.upper(), end='')
    else:
        print(char.lower(), end='')
