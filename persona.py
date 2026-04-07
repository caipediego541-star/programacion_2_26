class persona:  #clase padre
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


#clases HIJAS:
class cliente(persona):
    def __init__(self,nombre,dni,telefono):
        super().__init__(nombre,dni,telefono)
        self.tipo_usuario="Cliente"
    def mostrar_cliente(self):
        return f"{self.mostrar_datos()}, tipo de usuario: {self.tipo_usuario}"

c=cliente("ana","26756304","2615473928")
print(c.mostrar_cliente())
print(c.identificarse()) #herencia de persona

class propietario(persona):
    def __init__(self, nombre, dni, telefono):
        super().__init__(nombre, dni, telefono)
        self.tipo_usuario="Propietario"
    def mostrar_propietario(self):
        return f"{self.mostrar_datos()}, tipo de usuario: {self.tipo_usuario}"

p=propietario("juan roman","26343234","2614453267")
print(p.mostrar_propietario()) #metodo de propietario
print(p.identificarse()) #herencia de persona(metodo)