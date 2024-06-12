"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class Vehiculo:
    color = 'rojo';
    fabricante = 'seat';
    num_serie = 1;

    def __init__(self):
        self.__num_serie = Vehiculo.num_serie
        self.__color = Vehiculo.color
        self.__fabricante = Vehiculo.fabricante

    @property
    def num_serie(self):
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        self.__num_serie = value

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: int):
        self.__color = value


class Coche(Vehiculo):

    cilindrada = 1000;

    def __init__(self):
        super().__init__()
        self.__cilindrada = Coche.cilindrada

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self.__cilindrada = value
