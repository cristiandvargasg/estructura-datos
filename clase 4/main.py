class Nodo:
    dato = None
    apuntador = None
    def __init__(self, dato, apuntador):
        self.dato = dato 
        self.apuntador = apuntador

    def __str__(self):
        return f"{self.dato}"

