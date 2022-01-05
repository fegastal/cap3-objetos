num_1 = 1
num_2 = 3

mensagem_1 = "A soma de " + str(num_1) + " com " + str(num_2) + " dá " + str(num_1 + num_2)
mensagem_2 = "A soma de %d com %d dá %d" % (num_1, num_2, num_1 + num_2)

print(mensagem_2)