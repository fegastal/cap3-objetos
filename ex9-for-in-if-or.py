def max_elem_1(elementos, funcao):
    '''Qual é o elemento de maior valor de acordo com a função?'''
    melhor_valor = None
    melhor_elem = None

    for elem in elementos:
        valor = funcao(elem)
        if melhor_valor == None or valor > melhor_valor:
            melhor_valor = valor
            melhor_elem = elem
        return melhor_elem

