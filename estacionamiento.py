from datetime import datetime

class Estacionamiento:
    def __init__(self):
        self.capacidad = 50
        self.tarjetas = {}
        self.registro = {} 
        self.tarifa = {"moto": 1500, "auto": 2000, "camioneta": 3000}

    def asignar_lugar(self, id_tarjeta, tipo_vehiculo):
        if len(self.tarjetas) < self.capacidad:
             
            if tipo_vehiculo in self.tarifa:
                self.tarjetas[id_tarjeta]=tipo_vehiculo
                self.registro[id_tarjeta] = datetime.now()
                print(f"Vehículo con tarjeta {id_tarjeta} ingresado.")
            else: 
                print("Tipo de vehículo no aceptable.")
        else:
            print("Estacionamiento lleno.")

                 
            
      
    def liberar_lugar(self, id_tarjeta):
        if id_tarjeta in self.tarjetas:
            hora_ingreso = self.registro[id_tarjeta]
            hora_salida = datetime.now()

            # calcular horas aproximadas
            horas = (hora_salida - hora_ingreso).total_seconds()/3600
            if horas < 1:
                horas = 1
            else:
                horas = round(horas)
            tipo_vehiculo=self.tarjetas[id_tarjeta]
            tarifa_total = self.tarifa[tipo_vehiculo] * horas

            # eliminar del registro y lista
            del self.tarjetas[id_tarjeta]
            del self.registro[id_tarjeta]

            print(f"Vehículo con tarjeta {id_tarjeta} retirado.")
            print(f"Tarifa total: {tarifa_total} $  | cantidad de horas: {horas}")
        else:
            print(f"No se encontró vehículo con tarjeta:{id_tarjeta}")

    def mostrar_vehiculos(self):
        if not self.tarjetas:
            print("No hay vehículos en el estacionamiento.")
        else:
            print(f"Tarjetas dentro del estacionamiento:{self.tarjetas}")