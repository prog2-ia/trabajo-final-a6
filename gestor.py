class GestorFinanzas:
    def __init__(self):
        self.cuentas = []
        self.presupuestos = []
        self.categorias = []

    def registrar_movimiento(self, nombre_cuenta, transaccion):
        cuenta_encontrada = None
        encontrada = False
        while encontrada == False:
            for c in self.cuentas:
                if c.nombre == nombre_cuenta:
                    cuenta_encontrada = c
                    encontrada = True


        if cuenta_encontrada:
            cuenta_encontrada.registrar_transaccion(transaccion)
            print(f"Movimiento registrado con éxito en {nombre_cuenta}.")
        else:
            print(f"Error: No se encontró la cuenta '{nombre_cuenta}'.")

    def verificar_alertas(self):
        alertas = []

        for c in self.cuentas:
            if c.saldo_actual < 0:
                alertas.append(f"¡Ojo! La cuenta {c.nombre} no tiene dinero.")

        if alertas is not None:
            texto_para_guardar = "\n".join(alertas)
            self.exportar_a_texto("alertas.log", texto_para_guardar)

        return alertas

    def generar_informe_mensual(self, mes: int, año: int):
        resumen = f"--- INFORME MENSUAL {mes}/{año} ---\n"
        total_ingresos = 0
        total_gastos = 0

        for cuenta in self.cuentas:
            resumen += f"Cuenta: {cuenta.nombre} | Saldo: {cuenta.saldo_actual}€\n"

        nombre_archivo = f"informe_{año}_{mes}.txt"
        self.exportar_a_texto(nombre_archivo, resumen)
        return resumen

    def exportar_a_texto(self, nombre_archivo, datos):
        archivo = open(nombre_archivo, "w")
        archivo.write(datos)
        archivo.close()
        print("Archivo guardado.")


