def max_elem_3(elementos, funcao):
    '''Qual é o elemento de maior valor de acordo com a função?'''
    valores = (funcao(elem) for elem in elementos)
    return elementos [valores.index(max(valores))]