#CLASE PADRE:
class vehiculo:
    def __init__(self,patente,marca,modelo,color):
        self.patente=patente
        self.marca=marca
        self.modelo=modelo
        self.color=color  
        self.encendido=False

    def encender(self):
        self.encendido=True
        return f"vehiculo {self.patente} encendido"
    
    def apagar(self):
        self.encendido=False
        return f"vehiculo {self.patente} apagado"
    
    def mostrar_datos(self):
        return f"patente: {self.patente},marca: {self.marca}, modelo: {self.modelo}, color: {self.color}"
    
    #clases hijas:
class moto(vehiculo):
    def __init__(self, patente, marca, modelo, color, cilindrada, tipomoto):
        super().__init__(patente, marca, modelo, color)
        self.cilindrada = cilindrada
        self.tipomoto = tipomoto
    def mostrar_moto(self):
        return f"{self.mostrar_datos()}, Cilindrada: {self.cilindrada}, Tipo de moto: {self.tipomoto}"


class auto(vehiculo):
    def __init__(self, patente, marca, modelo, color, cantpuertas, tipocarroceria):
        super().__init__(patente, marca, modelo, color)
        self.cantpuertas = cantpuertas
        self.tipocarroceria = tipocarroceria
    
    def mostrar_auto(self):
        return f"{self.mostrar_datos()}, Puertas: {self.cantpuertas}, Tipo carrocería: {self.tipocarroceria}"
    
class camioneta(vehiculo):
        def __init__(self, patente, marca, modelo, color, capacidad, tipotraccion):
            super().__init__(patente, marca, modelo, color)
            self.capacidad = capacidad
            self.tipotraccion = tipotraccion
        def mostrar_camioneta(self):
            return f"{self.mostrar_datos()}, Capacidad: {self.capacidad}kg, Tracción: {self.tipotraccion}"
        

m1 = moto("MOTO123", "Honda", "CB500", "Rojo", 500, "Deportiva")
print(m1.mostrar_moto())
print(m1.encender())
print(m1.apagar())
print()

a1 = auto("AUTO456", "Toyota", "Corolla", "Azul", 4, "Sedán")
print(a1.mostrar_auto())
print(a1.encender())
print(a1.apagar())
print()

c1 = camioneta("CAM789", "Ford", "Ranger", "Negro", 1200, "4x4")
print(c1.mostrar_camioneta())
print(c1.encender())
print(c1.apagar())

