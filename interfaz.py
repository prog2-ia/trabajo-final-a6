from excepciones import SaldoInsuficienteError, ImporteInvalidoError
from cuentas import CuentaPrincipal, CuentaAhorro


def mostrar_menu():
    # Muestra las opciones disponibles en consola
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

                cuenta_existe = False
                for c in gestor:
                    if c.nombre == nombre:
                        cuenta_existe = True
                        if monto < 0 and c.saldo < abs(monto):
                            raise SaldoInsuficienteError(c.saldo, abs(monto))
                        break
                    if cuenta_existe:
                        cat_input = input("Categoría del movimiinto (opcional, pulse Enter para ninguna): ").strip()
                        nombre_categoria = cat_input if cat_input != "" else None
                        gestor.registrar_movimiento(nombre, desc, monto)
                        print("Movimiento registrado correctamente.")

                    else:
                        print(f'Error: no se encontro la cuenta "{nombre}".')

            except ValueError:
                print("Error: El monto debe ser un número.")
            except SaldoInsuficienteError as e:

                print(f"Movimiento fallido: {e}")

        elif opcion == "3":
            try:
                origen_nom = input("Nombre cuenta origen: ")
                destino_nom = input("Nombre cuenta destino: ")
                monto = float(input("Cantidad a transferir: "))

                # Buscamos los objetos cuenta (sin usar break)
                origen = None
                destino = None
                for c in gestor:
                    if c.nombre == origen_nom:
                        origen = c
                    if c.nombre == destino_nom:
                        destino = c

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
            print("\n--- AÑADIR NUEVA CUENTA ---")
            print("1. Cuenta Principal (Corriente)")
            print("2. Cuenta de Ahorro")
            tipo = input("Seleccione el tipo de cuenta: ")

            if tipo not in ["1", "2"]:
                print("Opción no válida. Volviendo al menú.")
                continue

            nombre = input("Nombre de la cuenta: ")

            # Evitamos duplicados de nombres de cuenta
            existe = False
            for c in gestor:
                if c.nombre.lower() == nombre.lower():
                    existe = True
                    break
            if existe:
                print("Error: Ya existe una cuenta con ese nombre.")
                continue

            try:
                saldo_inicial = float(input("Saldo inicial (ej: 0.0): "))
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


        elif opcion == "6":
            print("Saliendo del sistema...")
            continuar = False
        else:
            print("Opción no válida.")