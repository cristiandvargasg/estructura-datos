class nodo:
    dato = None
    apuntador = None
    def __init__(self,dato,apuntador):
        self.dato = dato
        self.apuntador = apuntador
    def __str__(self):
        return f"{self.dato}"

        
print ("-"*30)
print ("Verificacion por nodo de un numero")
print ("_"*30)
obj1 = nodo(20,None)
obj2 = nodo(20,None)
print (obj1)
print (obj2)
print ("_"*30)
print (obj1 == obj2)
print ("-"*30)