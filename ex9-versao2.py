def max_elem_2(elementos, funcao):
    '''Qual é o elemento de maior valor de acordo com a função?'''
    melhor_valor = funcao(melhor_elem)
    melhor_elem = elementos[0]

    for elem in elementos[1:]:
        valor = funcao(elem)
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_elem = elem
        return melhor_elem