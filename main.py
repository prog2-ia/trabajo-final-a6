from categorias import Categoria
from cuentas import CuentaPrincipal, CuentaAhorro
from gestor import GestorFinanzas
from transacciones import Transaccion


def iniciar_programa():
    gestor = GestorFinanzas()

    print("--- Configurando Categorías ---")
    cat_gastos = Categoria("Gastos Generales")
    cat_hogar = Categoria("Hogar", cat_gastos)
    cat_ocio = Categoria("Ocio", cat_gastos)
    print(cat_hogar.obtener_ruta())

    print("\n--- Creando Cuentas ---")
    cuenta_diaria = CuentaPrincipal("Mi Cuenta Corriente", 1000.0)
    cuenta_viaje = CuentaAhorro("Ahorros para Japón", 200.0, 3000.0)

    # Añadimos las cuentas al gestor
    gestor.añadir_cuenta(cuenta_diaria)
    gestor.añadir_cuenta(cuenta_viaje)

    print("\n--- Registrando Movimientos ---")

    # Simulamos un ingreso
    gestor.registrar_movimiento("Mi Cuenta Corriente", "Nómina de marzo", 1500.0)

    # Simulamos gastos (uno de ellos muy grande para forzar saldo negativo y ver la alerta)
    gestor.registrar_movimiento("Mi Cuenta Corriente", "Compra supermercado", -150.0)
    gestor.registrar_movimiento("Mi Cuenta Corriente", "Coche nuevo", -3000.0)

    # Transferencia entre cuentas
    print("\n--- Probando Transferencias ---")
    # Nota: la transferencia fallará por saldo insuficiente debido a la compra del coche
    cuenta_diaria.transferir(500.0, cuenta_viaje)

    # Exportación de archivos
    print("\n--- Generando Informes y Alertas ---")

    # Esto creará el archivo 'alertas.log' porque la cuenta corriente está en negativo
    alertas = gestor.verificar_alertas()
    if len(alertas) > 0:
        print(f"Se han encontrado {len(alertas)} alertas de saldo. Revisa alertas.log")

    # Esto creará el archivo 'informe_2026_3.txt'
    gestor.generar_informe_mensual(3, 2026)
    print("Proceso finalizado. Revisa los archivos generados en tu carpeta.")


# Bloque de ejecución principal
if __name__ == "__main__":
    iniciar_programa()