import os  # Imports necesarios
from typing import List
from cuentas import Cuenta
from presupuestos import Presupuesto
from excepciones import PresupuestoExcedidoError


class GestorFinanzas:
    def __init__(self) -> None:
        # Listas privadas para el almacenamiento de datos
        self.__cuentas: List[Cuenta] = []
        self.__presupuestos: List[Presupuesto] = []

    def añadir_cuenta(self, cuenta: Cuenta):
        self.__cuentas.append(cuenta)

    def añadir_presupuesto(self, presupuesto: Presupuesto) -> None:
        self.__presupuestos.append(presupuesto)

    def __getitem__(self, index):
        return self.__cuentas[index]

    def __len__(self) -> int:
        return len(self.__cuentas)

    def registrar_movimiento(self, nombre_cuenta: str, transaccion_desc: str, cantidad: float,
                             nombre_categoria: str = None) -> None:
        categoria_obj = None

        if nombre_categoria:
            for pres in self.__presupuestos:
                if pres.categoria.nombre.lower() == nombre_categoria.lower():
                    categoria_obj = pres.categoria
                    if cantidad < 0:
                        try:
                            pres.añadir_gasto(abs(cantidad))
                        except PresupuestoExcedidoError as e:
                            print(f"\n  ¡ALERTA DE PRESUPUESTO! {e}")
                        break

        for cuenta in self.__cuentas:
            if cuenta.nombre == nombre_cuenta:
                cuenta.registrar_transaccion(cantidad, transaccion_desc, categoria_obj)
                return
        print(f'Error: no se encontro la cuenta "{nombre_cuenta}".')

    def verificar_alertas(self):
        try:
            # os.makedirs crea la carpeta 'logs'. exist_ok=True evita que dé error si la carpeta ya existe.
            os.makedirs("logs", exist_ok=True)

            # Guardamos el archivo dentro de la carpeta creada usando 'w' (escritura de texto)
            with open("logs/alertas.log", "w", encoding="utf-8") as file:
                for pres in self.__presupuestos:
                    try:
                        pres.verificar_estado()
                    except Exception as e:
                        file.write(f"ALERTA: {e}\n")
                file.write("Verificación de alertas completada.\n")
        except Exception as e:
            print(f"Error procesando alertas: {e}")

    def generar_informe_mensual(self, mes, año):
   #Uso de rutas coherentes y directorios
        os.makedirs("informes", exist_ok=True)
        nombre_archivo = f"informes/informe_{año}_{mes}.txt"
        try:
            # Escribimos el informe dentro de la subcarpeta 'informes'
            with open(nombre_archivo, "w", encoding="utf-8") as file:
                file.write(f"--- INFORME MENSUAL {mes}/{año} ---\n\n")
                for cuenta in self.__cuentas:
                    file.write(f"Cuenta: {cuenta.nombre} | Tipo: {cuenta.obtener_tipo()} | Saldo: {cuenta.saldo}€\n")
        except Exception as e:
            print(f"Error al generar el informe: {e}")



