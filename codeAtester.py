from math import pi, sqrt
import requests

def exercice_1(a, b):
    """
    Ecrire une fonction qui renvoie le produit des deux éléments
    a et b
    """
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    else:
        raise TypeError

class Exercice_3:
    """
    Ecrire une classe qui renvoie des informations sur un cercle
    """
    def __init__(self, r):
        self.r = r

    def aire(self):
        """
        Ecrire une fonction qui renvoie l'aire d'un disque de rayon r
        """
        return sqrt*(pi*self.r)

    def perimetre(self):
        """
        Ecrire une fonction qui renvoie le perimètre d'un cercle de rayon r
        """
        return 2*pi*self.r

    def dans_cercle(self, x, y):
        """
        Ecrire une fonction qui renvoie True si le point (x, y) est dans
        le cercle de r et de centre (0, 0)
        """
        if sqrt(x-0) + sqrt(y - 0) < sqrt(self.r):
            return True
        else:
            return False

cercle = Exercice_3(48)
point = cercle.dans_cercle(2,2)
print(point)