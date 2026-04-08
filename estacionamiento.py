from datetime import datetime

class Estacionamiento:
    def __init__(self):
        self.capacidad = 50
        self.tarjetas = []
        self.registro = {} 
        self.tarifa = {"moto": 1500, "auto": 2000, "camioneta": 3000}

    def asignar_lugar(self, id_tarjeta, tipo_vehiculo):
        if len(self.tarjetas) < self.capacidad:
            self.tarjetas.append(id_tarjeta)
            self.registro[id_tarjeta] = datetime.now()
            print("Vehículo con tarjeta", id_tarjeta, "ingresado.")
        else:
            print("Estacionamiento lleno.")

    def liberar_lugar(self, id_tarjeta, tipo_vehiculo):
        if id_tarjeta in self.tarjetas:
            hora_ingreso = self.registro[id_tarjeta]
            hora_salida = datetime.now()

            # calcular horas aproximadas
            horas = (hora_salida.hour + hora_salida.minute/60) - (hora_ingreso.hour + hora_ingreso.minute/60)
            if horas < 1:
                horas = 1
            else:
                horas = round(horas)

            tarifa_total = self.tarifa[tipo_vehiculo] * horas

            # eliminar del registro y lista
            self.tarjetas.remove(id_tarjeta)
            del self.registro[id_tarjeta]

            print("Vehículo con tarjeta", id_tarjeta, "retirado.")
            print("Hora ingreso:", hora_ingreso.hour, "h", hora_ingreso.minute, "min")
            print("Hora salida:", hora_salida.hour, "h", hora_salida.minute, "min")
            print("Tarifa total:", tarifa_total)
        else:
            print("No se encontró vehículo con tarjeta", id_tarjeta)

    def mostrar_vehiculos(self):
        if not self.tarjetas:
            print("No hay vehículos en el estacionamiento.")
        else:
            print("Tarjetas dentro del estacionamiento:", self.tarjetas)