import cmath

def poli_2(a,b,c):

    """Calcula as raizes de um polinomio de segundo grau.
    Obs: cmath disponibiliza operações """

    delta = cmath.sqrt(b**2 - 4 * a * c)
    raiz_1 = (-b + delta) / (2 * a)
    raiz_2 = (-b - delta) / (2*a)
    return raiz_1, raiz_2

