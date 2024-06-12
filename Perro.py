"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:

    def __init__(self):
        self.ladra = 'Guau'

    def ladrar(self):
        print(self.ladra);

p = Perro();
p.ladrar();
