from datetime import datetime

class Vehiculo:
    def __init__(self, placa, tipo): # Agregamos 'tipo' al constructor
        self.placa = placa
        self.tipo = tipo # Guardamos el tipo de vehículo (ej. 'carro', 'camioneta', 'moto')
        self.hora_entrada = datetime.now()
        self.espacio_asignado = None

    def obtener_tiempo_estacionado(self):
        tiempo_salida = datetime.now()
        return (tiempo_salida - self.hora_entrada).total_seconds() / 60  # en minutos

    def __str__(self):
        return f"Placa: {self.placa}, Tipo: {self.tipo}, Entrada: {self.hora_entrada.strftime('%Y-%m-%d %H:%M:%S')}"