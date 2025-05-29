class Registro:
    def __init__(self):
        self.entradas = {}

    def registrar_entrada(self, vehiculo):
        self.entradas[vehiculo.placa] = vehiculo

    def registrar_salida(self, placa):
        return self.entradas.pop(placa, None)

    def obtener_vehiculo(self, placa):
        return self.entradas.get(placa)