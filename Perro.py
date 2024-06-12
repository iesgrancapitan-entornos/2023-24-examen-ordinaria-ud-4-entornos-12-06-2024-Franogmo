"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:
    """
    Clase perro. Hace cosas de perro
    """

    def __init__(self):
        """
        Constructor del perro

        :param: ladra = str
        """
        self.ladra = 'Guau'

    def ladrar(self):
        """
        Imprime un ladrido (variable de instancia de perro) por la pantalla
        """
        print(self.ladra);

p = Perro();
p.ladrar();
