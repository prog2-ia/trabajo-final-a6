from excepciones import SaldoInsuficienteError, ImporteInvalidoError


def mostrar_menu():
    # Muestra las opciones disponibles en consola
    print("\n" + "=" * 30)
    print("   GESTOR DE FINANZAS")
    print("=" * 30)
    print("1. Ver saldo de todas las cuentas")
    print("2. Registrar nuevo movimiento")
    print("3. Realizar transferencia")
    print("4. Generar informe mensual")
    print("5. Salir")
    return input("Seleccione una opción: ")


def ejecutar_interfaz(gestor):
    # Bucle principal de la interfaz de usuario
    continuar = True
    while continuar:
        opcion = mostrar_menu()

        if opcion == "1":
            print("\n--- ESTADO DE LAS CUENTAS ---")
            # Usamos el protocolo de secuencia (__getitem__) para iterar
            for cuenta in gestor:
                print(f"{cuenta.nombre}: {cuenta.saldo}€")

        elif opcion == "2":
            try:
                nombre = input("Nombre de la cuenta: ")
                desc = input("Descripción del movimiento: ")
                monto = float(input("Cantidad (positivo ingreso, negativo gasto): "))
                gestor.registrar_movimiento(nombre, desc, monto)
            except ValueError:
                print("Error: El monto debe ser un número.")
            except ImporteInvalidoError as e:
                print(e)

        elif opcion == "3":
            try:
                origen_nom = input("Nombre cuenta origen: ")
                destino_nom = input("Nombre cuenta destino: ")
                monto = float(input("Cantidad a transferir: "))

                # Buscamos los objetos cuenta (sin usar break)
                origen = None
                destino = None
                for c in gestor:
                    if c.nombre == origen_nom: origen = c
                    if c.nombre == destino_nom: destino = c

                if origen and destino:
                    origen.transferir(monto, destino)
                else:
                    print("Error: Una o ambas cuentas no existen.")
            except ValueError:
                print("Error: El monto debe ser un número.")
            except (SaldoInsuficienteError, ImporteInvalidoError) as e:
                print(f"Transferencia fallida: {e}")

        elif opcion == "4":
            # Genera los archivos de texto
            gestor.verificar_alertas()
            gestor.generar_informe_mensual(4, 2024)
            print("Informes generados (alertas.log e informe_2024_4.txt).")

        elif opcion == "5":
            print("Saliendo del sistema...")
            continuar = False
        else:
            print("Opción no válida.")