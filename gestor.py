from typing import List
from cuentas import Cuenta
from presupuestos import Presupuesto

class GestorFinanzas:
    def __init__(self) -> None:
        # Listas privadas para el almacenamiento de datos
        self.__cuentas : List[Cuenta] = []
        self.__presupuestos: List[Presupuesto] = []

    def añadir_cuenta(self, cuenta: Cuenta):
        # Agrega una nueva cuenta a la lista del gestor
        self.__cuentas.append(cuenta)

    def añadir_presupuesto(self, presupuesto: Presupuesto)-> None:
        self.__presupuestos.append(presupuesto)

    def __getitem__(self, index):
        # Permite acceder a las cuentas por índice o usarlas en un bucle 'for'
        return self.__cuentas[index]

    def __len__(self) -> int:
        # Devuelve la cantidad total de cuentas registradas
        return len(self.__cuentas)

    def registrar_movimiento(self, nombre_cuenta: str, transaccion_desc: str, cantidad: float) -> None:
        for cuenta in self.__cuentas:
            if cuenta.nombre == nombre_cuenta:
                cuenta.registrar_transaccion(cantidad, transaccion_desc)
                return
        print(f'Error: no se encontro la cuenta "{nombre_cuenta}".')

    def verificar_alertas(self):
        try:
            with open("alertas.log", "w", encoding="utf-8") as file:
                for pres in self.__presupuestos:
                    try:
                        pres.verificar_estado()
                    except Exception as e:
                        file.write(f"ALERTA: {e}\n")
                file.write("Verificación de alertas completada.\n")
        except Exception as e:
            print(f"Error procesando alertas: {e}")

    def generar_informe_mensual(self, mes, año):
        nombre_archivo = f"informe_{año}_{mes}.txt"
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as file:
                file.write(f"--- INFORME MENSUAL {mes}/{año} ---\n\n")
                for cuenta in self.__cuentas:
                    file.write(f"Cuenta: {cuenta.nombre} | Tipo: {cuenta.obtener_tipo()} | Saldo: {cuenta.saldo}€\n")
        except Exception as e:
            print(f"Error al generar el informe: {e}")



