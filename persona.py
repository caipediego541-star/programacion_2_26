class persona:
    #atributos
    def __init__(self,nombre,dni,telefono):
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono
    #metodos
    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Tel: {self.telefono}"
    def identificarse(self):
        return f"Soy {self.nombre} con DNI: {self.dni}"



p=persona("Diego","45873451","2617127020")
print(p.mostrar_datos())
print(p.identificarse())