TARIFAS_POR_MINUTO = {
    'carro': 100,      # $100 por minuto
    'camioneta': 150,  # $150 por minuto
    'moto': 70         # $70 por minuto
}

def calcular_tarifa(minutos, tipo_vehiculo): # La función ahora recibe el tipo de vehículo
    # Obtener la tarifa por minuto para el tipo de vehículo
    tarifa_por_minuto_especifica = TARIFAS_POR_MINUTO.get(tipo_vehiculo.lower(), 0) # .lower() para ser flexible

    if tarifa_por_minuto_especifica == 0:
        print(f"Advertencia: Tipo de vehículo '{tipo_vehiculo}' no reconocido. Tarifa por defecto de $0.")
        return 0


    valor_a_pagar = minutos * tarifa_por_minuto_especifica
    return valor_a_pagar
