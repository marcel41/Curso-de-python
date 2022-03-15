from abc import ABC, abstractmethod
class Vehiculo(ABC):
    def __init__(self,color, marca, num_pasajeros, tipo_gas):
        self.color = color
        self.marca = marca
        self.num_pasajeros = num_pasajeros
        self.tipo_gas = tipo_gas

    def conducir(self):
        print("Conduciendo un " + self.marca)

    @abstractmethod
    def __str__(self):
        msg = "Vehiculo marca " + self.marca + ", color " + self.color + " de " + str(self.num_pasajeros) + " pasajeros " + "que funciona a gasolina " + self.tipo_gas
        return msg
