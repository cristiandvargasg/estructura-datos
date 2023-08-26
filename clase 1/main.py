class Vehiculo:

    marca = ""
    combustible = ""

    def encender(self):
        return f"se enciende el vehiculo con combustible {self.combustible}"

    def arrancar(self):
        pass

    def __init__(self, marca, combustible):
        self.combustible = combustible
        self.marca = marca

carro = Vehiculo("mercedes", "diesel")
print(carro.marca)
print("="*10)
print(carro.encender())