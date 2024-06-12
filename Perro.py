"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:

    def __init__(self):
        self.guau = 'Guau'

    def ladrar(self):
        print(self.guau);

p = Perro();
p.ladrar();
