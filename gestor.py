class GestorFinanzas:
    def __init__(self):
        # Listas privadas para el almacenamiento de datos del sistema
        self.__cuentas = []
        self.__presupuestos = []
        self.__categorias = []

    def registrar_movimiento(self, nombre_cuenta, transaccion_desc, cantidad):
        # Busca una cuenta por su nombre y añade una transacción
        cuenta_encontrada = None
        indice = 0

        # Búsqueda mediante condición lógica de control
        while indice < len(self.__cuentas) and cuenta_encontrada is None:
            if self.__cuentas[indice].nombre == nombre_cuenta:
                cuenta_encontrada = self.__cuentas[indice]
            indice += 1

        if cuenta_encontrada:
            cuenta_encontrada.registrar_transaccion(transaccion_desc, cantidad)
            print(f"Movimiento registrado con éxito en {nombre_cuenta}.")
        else:
            print(f"Error: No se encontró la cuenta '{nombre_cuenta}'.")

    def verificar_alertas(self):
        # Identifica cuentas con saldo negativo y genera un registro de errores
        alertas = []

        for c in self.__cuentas:
            # Validación de balance disponible
            if c.saldo < 0:
                alertas.append(f"¡Alerta! La cuenta '{c.nombre}' tiene saldo negativo: {c.saldo}€")

        if len(alertas) > 0:
            texto_para_guardar = "\n".join(alertas)
            self.exportar_a_texto("alertas.log", texto_para_guardar)

        return alertas

    def generar_informe_mensual(self, mes, año):
        # Compila el estado de todas las cuentas en un documento de texto externo
        resumen = f"--- INFORME MENSUAL {mes}/{año} ---\n"

        for cuenta in self.__cuentas:
            # Concatenación de detalles de cuenta y saldo actual
            resumen += f"Cuenta: {cuenta.nombre} ({cuenta.obtener_tipo()}) | Saldo: {cuenta.saldo}€\n"

        nombre_archivo = f"informe_{año}_{mes}.txt"
        self.exportar_a_texto(nombre_archivo, resumen)
        return resumen

    def exportar_a_texto(self, nombre_archivo, datos):
        # Realiza la escritura física de datos en disco (para la realización de este metodo hemos utilizado la ayuda de gemini)
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        archivo.write(datos)
        archivo.close()

        print(f"Archivo '{nombre_archivo}' guardado correctamente.")

    def añadir_cuenta(self, cuenta):
        # Permite la inserción de objetos cuenta en el registro privado
        self.__cuentas.append(cuenta)

