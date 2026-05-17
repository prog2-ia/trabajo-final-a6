import os
import pickle
from excepciones import SaldoInsuficienteError, ImporteInvalidoError
from cuentas import CuentaPrincipal, CuentaAhorro


def mostrar_menu():
    # Muestra el menú principal en consola y devuelve la opción seleccionada
    print("\n" + "=" * 30)
    print("   GESTOR DE FINANZAS")
    print("=" * 30)
    print("1. Ver saldo de todas las cuentas")
    print("2. Registrar nuevo movimiento")
    print("3. Realizar transferencia")
    print("4. Generar informe mensual")
    print("5. Añadir nueva cuenta")
    print("6. Salir")
    return input("Seleccione una opción: ")


def ejecutar_interfaz(gestor):
    # Bucle principal que mantiene la aplicación en ejecución
    continuar = True
    while continuar:
        opcion = mostrar_menu()

        if opcion == "1":
            # Muestra el saldo actual de todas las cuentas registradas
            print("\n--- ESTADO DE LAS CUENTAS ---")
            for cuenta in gestor:
                print(f"{cuenta.nombre}: {cuenta.saldo}€")

        elif opcion == "2":
            # Inicia el proceso para registrar un nuevo ingreso o gasto
            try:
                nombre = input("Nombre de la cuenta: ")
                desc = input("Descripción del movimiento: ")
                monto = float(input("Cantidad (positivo ingreso, negativo gasto): "))

                cuenta_existe = False

                # Busca la cuenta indicada por el usuario
                for c in gestor:
                    if c.nombre == nombre:
                        cuenta_existe = True
                        # Verifica si hay fondos suficientes para realizar un gasto
                        if monto < 0 and c.saldo < abs(monto):
                            raise SaldoInsuficienteError(c.saldo, abs(monto))
                        break

                if cuenta_existe:
                    # Solicita la categoría opcional y registra el movimiento
                    cat_input = input("Categoría del movimiento (opcional, pulse Enter para ninguna): ").strip()
                    nombre_categoria = cat_input if cat_input != "" else None

                    gestor.registrar_movimiento(nombre, desc, monto, nombre_categoria)
                    print("Movimiento registrado correctamente.")
                else:
                    print(f'Error: no se encontro la cuenta "{nombre}".')

            except ValueError:
                print("Error: El monto debe ser un número.")
            except SaldoInsuficienteError as e:
                print(f"Movimiento fallido: {e}")

        elif opcion == "3":
            # Inicia el proceso para transferir dinero entre dos cuentas
            try:
                origen_nom = input("Nombre cuenta origen: ")
                destino_nom = input("Nombre cuenta destino: ")
                monto = float(input("Cantidad a transferir: "))

                origen = None
                destino = None

                # Busca las instancias de las cuentas de origen y destino
                for c in gestor:
                    if c.nombre == origen_nom:
                        origen = c
                    if c.nombre == destino_nom:
                        destino = c

                if origen and destino:
                    # Ejecuta la transferencia si ambas cuentas existen
                    origen.transferir(monto, destino)
                else:
                    print("Error: Una o ambas cuentas no existen.")

            except ValueError:
                print("Error: El monto debe ser un número.")
            except (SaldoInsuficienteError, ImporteInvalidoError) as e:
                print(f"Transferencia fallida: {e}")

        elif opcion == "4":
            # Genera los archivos de registro y el informe mensual
            gestor.verificar_alertas()
            gestor.generar_informe_mensual(4, 2024)
            print("Informes generados en sus carpetas ('logs/alertas.log' e 'informes/informe_2024_4.txt').")

        elif opcion == "5":
            # Inicia el proceso para crear y registrar una nueva cuenta bancaria
            print("\n--- AÑADIR NUEVA CUENTA ---")
            print("1. Cuenta Principal (Corriente)")
            print("2. Cuenta de Ahorro")
            tipo = input("Seleccione el tipo de cuenta: ")

            if tipo in ["1", "2"]:
                nombre = input("Nombre de la cuenta: ")

                existe = False
                # Comprueba que no exista ya una cuenta con el mismo nombre
                for c in gestor:
                    if c.nombre.lower() == nombre.lower():
                        existe = True
                        break

                if not existe:
                    try:
                        saldo_inicial = float(input("Saldo inicial (ej: 0.0): "))

                        # Crea la cuenta correspondiente según la elección del usuario
                        if tipo == "1":
                            nueva_cuenta = CuentaPrincipal(nombre, saldo_inicial)
                            gestor.añadir_cuenta(nueva_cuenta)
                            print(f"Cuenta Principal '{nombre}' añadida correctamente.")
                        elif tipo == "2":
                            objetivo = float(input("Objetivo de ahorro: "))
                            nueva_cuenta = CuentaAhorro(nombre, saldo_inicial, objetivo)
                            gestor.añadir_cuenta(nueva_cuenta)
                            print(f"Cuenta de Ahorro '{nombre}' añadida correctamente.")
                    except ValueError:
                        print("Error: Los valores de saldo u objetivo deben ser numéricos.")
                else:
                    print("Error: Ya existe una cuenta con ese nombre.")
            else:
                print("Opción no válida. Volviendo al menú.")

        elif opcion == "6":
            # Guarda el estado de la aplicación en un fichero y finaliza la ejecución
            print("Guardando el estado del sistema...")
            try:
                # Crea el directorio de destino si no existe
                os.makedirs("datos", exist_ok=True)

                # Escribe el objeto gestor en un archivo binario
                with open("datos/estado_gestor.pkl", "wb") as f:
                    pickle.dump(gestor, f)
                print("Datos guardados correctamente en 'datos/estado_gestor.pkl'.")

            except Exception as e:
                print(f"Error al guardar los datos: {e}")

            print("Saliendo del sistema...")
            continuar = False

        else:
            print("Opción no válida. Por favor, introduzca un número del 1 al 6.")