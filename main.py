import os
import pickle
from categorias import Categoria
from cuentas import CuentaPrincipal, CuentaAhorro
from gestor import GestorFinanzas
from interfaz import ejecutar_interfaz


def iniciar_programa() -> None:
    # Inicializa la aplicación cargando datos guardados o creando un entorno limpio
    print("--- Configurando Sistema ---")

    # Define la ruta donde se almacena el estado de la aplicación
    ruta_datos = "datos/estado_gestor.pkl"

    # Comprueba si existe un archivo de guardado previo
    if os.path.exists(ruta_datos):
        print("Cargando datos previos...")
        try:
            # Abre el archivo binario en modo lectura y carga el objeto
            with open(ruta_datos, "rb") as f:
                gestor = pickle.load(f)
            print(f"Sistema restaurado correctamente con {len(gestor)} cuentas.")
        except Exception as e:
            # Si hay un error al leer el archivo, inicializa los datos por defecto
            print(f"Error al cargar los datos ({e}). Iniciando sistema limpio.")
            gestor = inicializar_datos_defecto()
    else:
        # Si no hay archivo de guardado, inicializa los datos por defecto
        print("No se encontraron datos previos. Iniciando sistema limpio.")
        gestor = inicializar_datos_defecto()

    # Lanza el bucle principal de la interfaz de usuario
    ejecutar_interfaz(gestor)


def inicializar_datos_defecto() -> GestorFinanzas:
    # Crea y configura un gestor con categorías y cuentas iniciales de ejemplo
    gestor = GestorFinanzas()

    cat_gastos = Categoria("Gastos")
    Categoria("Hogar", cat_gastos)
    Categoria("Ocio", cat_gastos)

    cuenta_diaria = CuentaPrincipal("Corriente", 1000.0)
    cuenta_viaje = CuentaAhorro("Ahorro", 200.0, 3000.0)

    gestor.añadir_cuenta(cuenta_diaria)
    gestor.añadir_cuenta(cuenta_viaje)

    return gestor


if __name__ == "__main__":
    # Punto de entrada principal del script
    iniciar_programa()