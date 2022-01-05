def declive(x1, y1, x2, y2):
    """Usa a forma habitual para calcular o declive, dados dois pontos. Obs: Prever o caso de os pontos
    terem a mesma abscissa, isto é, estarmos na presença de uma reta perpendicular ao eixo dos x.
    Obs 2: Inf é uma constante que simboliza o infinito"""
    if x1 != x2:
        return (y2 - y1) / (x2 - x1)
    else:
        return float ('Inf')