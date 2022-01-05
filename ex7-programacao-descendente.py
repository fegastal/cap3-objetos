def encripta(texto_normal):
    '''Encriptação por separação dos caracteres nas posições pares e nas posições ímpares.'''
    car_pares = ""
    car_impares = ""
    car_conta = 0
    
    for car in texto_normal:
        if car_conta %2 == 0:
            car_pares = car_pares + car
        else:
            car_impares = car_impares + car
        car_conta = car_conta + 1
    texto_encriptado = car_impares + car_pares
    return texto_encriptado