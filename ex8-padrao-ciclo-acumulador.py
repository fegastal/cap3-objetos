def encripta(texto_normal):
    '''Encriptação por separação dos caracteres nas posições pares e nas posições ímpares.'''
    comp = len(texto_normal)
    car_pares = ""
    car_impares = ""

    for car in range(comp):
        if indice %2 == 0:
            car_pares = car_pares + texto_normal[indice]
        else:
            car_impares = car_impares + texto_normal[indice]
    texto_encriptado = car_impares + car_pares
    return texto_encriptado