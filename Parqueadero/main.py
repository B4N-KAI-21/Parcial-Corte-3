from parqueadero import Parqueadero

def menu():
    parqueadero = Parqueadero(filas=10, columnas=10) 
    while True:
        print("\n--- Menú Parqueadero ---")
        print("1. Mostrar Mapa y Disponibilidad")
        print("2. Ingresar Vehículo")
        print("3. Retirar Vehículo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            parqueadero.mostrar_mapa()
        elif opcion == '2':
            placa = input("Ingrese la placa del vehículo: ")
            # Ofrecer opciones de tipo de vehículo al usuario
            print("Seleccione el tipo de vehículo:")
            print("  1. Carro ($100/min)")
            print("  2. Camioneta ($150/min)")
            print("  3. Moto ($70/min)")
            tipo_opcion = input("Ingrese el número correspondiente al tipo: ")
            
            tipo_vehiculo = ""
            if tipo_opcion == '1':
                tipo_vehiculo = 'carro'
            elif tipo_opcion == '2':
                tipo_vehiculo = 'camioneta'
            elif tipo_opcion == '3':
                tipo_vehiculo = 'moto'
            else:
                print("Opción de tipo de vehículo inválida. Se asignará 'carro' por defecto.")
                tipo_vehiculo = 'carro' # O manejarlo como un error y no permitir el ingreso

            parqueadero.ingresar_vehiculo(placa, tipo_vehiculo) # Pasar el tipo de vehículo
        elif opcion == '3':
            placa = input("Ingrese la placa del vehículo: ")
            parqueadero.retirar_vehiculo(placa)
        elif opcion == '4':
            print("Saliendo del sistema de parqueadero. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    menu()
    