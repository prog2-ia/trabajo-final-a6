from categorias import Categoria
from cuentas import CuentaPrincipal, CuentaAhorro
from gestor import GestorFinanzas
from interfaz import ejecutar_interfaz


def iniciar_programa() -> None:
    # 1. Inicializamos el gestor central
    gestor = GestorFinanzas()

    print("--- Configurando Sistema ---")

    # 2. Creamos categorías de ejemplo
    cat_gastos = Categoria("Gastos")
    cat_hogar = Categoria("Hogar", cat_gastos)
    cat_ocio = Categoria("Ocio", cat_gastos)

    # 3. Creamos cuentas iniciales
    cuenta_diaria = CuentaPrincipal("Corriente", 1000.0)
    cuenta_viaje = CuentaAhorro("Ahorro", 200.0, 3000.0)

    # 4. Añadimos las cuentas al gestor
    gestor.añadir_cuenta(cuenta_diaria)
    gestor.añadir_cuenta(cuenta_viaje)

    print(f"Sistema listo con {len(gestor)} cuentas.")

    # 5. Lanzamos la interfaz interactiva
    ejecutar_interfaz(gestor)


if __name__ == "__main__":
    # Punto de entrada principal
    iniciar_programa()