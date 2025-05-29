from vehiculo import Vehiculo
from registro import Registro
from utilidades import calcular_tarifa, TARIFAS_POR_MINUTO # Importamos también TARIFAS_POR_MINUTO

class Parqueadero:
    def __init__(self, filas=10, columnas=10): 
        self.filas = filas
        self.columnas = columnas
        self.mapa = [['#' for _ in range(columnas)] for _ in range(filas)] 
        self.registro = Registro()
        self._configurar_mapa()
        self.vehiculos_en_espacios = {} 

    def _configurar_mapa(self):
        # Generar bordes del parqueadero
        for i in range(self.filas):
            for j in range(self.columnas):
                if i == 0 or i == self.filas - 1 or j == 0 or j == self.columnas - 1:
                    self.mapa[i][j] = '#' # Borde

        # Definir una vía principal en el centro
        for i in range(1, self.filas - 1):
            self.mapa[i][self.columnas // 2] = 'V' # Vía central vertical

        # Definir entrada y salida
        self.mapa[1][self.columnas // 2] = 'E' # Entrada en la vía
        self.mapa[self.filas - 2][self.columnas // 2] = 'S' # Salida en la vía

        # Asignar espacios de parqueo a ambos lados de la vía principal
        espacios_count = 0
        for i in range(2, self.filas - 2): # Evitar entrada y salida y los bordes
            # Lado izquierdo de la vía
            if self.columnas // 2 - 1 > 0 and self.mapa[i][self.columnas // 2 - 1] == '#': 
                self.mapa[i][self.columnas // 2 - 1] = 'P'
                espacios_count += 1
            # Lado derecho de la vía
            if self.columnas // 2 + 1 < self.columnas -1 and self.mapa[i][self.columnas // 2 + 1] == '#': 
                self.mapa[i][self.columnas // 2 + 1] = 'P'
                espacios_count += 1
        
        print(f"Mapa configurado con {espacios_count} espacios de parqueo.")


    def mostrar_mapa(self):
        print("\n--- Mapa del Parqueadero ---")
        for i, fila in enumerate(self.mapa):
            row_str = []
            for j, celda in enumerate(fila):
                if celda == 'P': # Espacio libre
                    row_str.append(f'\033[92m{celda}\033[0m') # Verde
                elif celda == 'O': # Espacio ocupado
                    row_str.append(f'\033[91m{celda}\033[0m') # Rojo
                elif celda == 'E': # Entrada
                    row_str.append(f'\033[94m{celda}\033[0m') # Azul
                elif celda == 'S': # Salida
                    row_str.append(f'\033[93m{celda}\033[0m') # Amarillo
                elif celda == 'V': # Vía
                    row_str.append(f'\033[97m{celda}\033[0m') # Blanco (vía)
                else: # Pared/Obstáculo
                    row_str.append(f'\033[90m{celda}\033[0m') # Gris
            print(' '.join(row_str))

        libres = 0
        ocupados = 0
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.mapa[i][j] == 'P':
                    libres += 1
                elif self.mapa[i][j] == 'O':
                    ocupados += 1
        
        print(f"Disponibilidad: Libres: {libres}, Ocupados: {ocupados}, Total: {libres + ocupados}")
        print("---------------------------\n")

    def ingresar_vehiculo(self, placa, tipo_vehiculo): # Agregamos 'tipo_vehiculo'
        if self.registro.obtener_vehiculo(placa):
            print(f"El vehículo con placa {placa} ya se encuentra en el parqueadero.")
            return

        # Validar el tipo de vehículo
        if tipo_vehiculo.lower() not in TARIFAS_POR_MINUTO:
            print(f"Tipo de vehículo '{tipo_vehiculo}' no válido. Tipos permitidos: {', '.join(TARIFAS_POR_MINUTO.keys())}")
            return

        for r in range(self.filas):
            for c in range(self.columnas):
                if self.mapa[r][c] == 'P': # Encontramos un espacio de parqueo libre
                    vehiculo = Vehiculo(placa, tipo_vehiculo.lower()) # Pasar el tipo de vehículo
                    vehiculo.espacio_asignado = (r, c)
                    self.mapa[r][c] = 'O'
                    self.registro.registrar_entrada(vehiculo)
                    self.vehiculos_en_espacios[placa] = (r, c)
                    print(f"Vehículo {tipo_vehiculo} con placa {placa} ingresó al parqueadero en ({r},{c})")
                    return
        print("No hay espacios disponibles.")

    def retirar_vehiculo(self, placa):
        vehiculo = self.registro.registrar_salida(placa)
        if not vehiculo:
            print("Vehículo no encontrado.")
            return

        # Recuperar las coordenadas donde estaba el vehículo
        if placa in self.vehiculos_en_espacios:
            r, c = self.vehiculos_en_espacios[placa]
            self.mapa[r][c] = 'P' # Liberar el espacio en el mapa
            del self.vehiculos_en_espacios[placa]
        else:
            print(f"Error: No se encontró la ubicación del vehículo {placa} en el mapa. Pero el registro de salida se completó.")
            # Aunque el vehículo salió del registro, su posición en el mapa no se actualizó correctamente.

        minutos = vehiculo.obtener_tiempo_estacionado()
        tarifa = calcular_tarifa(minutos, vehiculo.tipo) # Pasar el tipo de vehículo al cálculo de tarifa
        print(f"Vehículo con placa {placa} ({vehiculo.tipo}) salió. Tiempo: {minutos:.2f} minutos. Tarifa: ${tarifa:,.2f}")