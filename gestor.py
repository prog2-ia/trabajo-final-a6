class GestorFinanzas:
    def __init__(self) -> None:
        # Listas privadas para el almacenamiento de datos
        self.__cuentas = []
        self.__presupuestos = []
        self.__categorias = []

    def añadir_cuenta(self, cuenta):
        # Agrega una nueva cuenta a la lista del gestor
        self.__cuentas.append(cuenta)

    def __getitem__(self, index):
        # Permite acceder a las cuentas por índice o usarlas en un bucle 'for'
        return self.__cuentas[index]

    def __len__(self):
        # Devuelve la cantidad total de cuentas registradas
        return len(self.__cuentas)

    def registrar_movimiento(self, nombre_cuenta, transaccion_desc, cantidad):
        # Busca la cuenta mediante un bucle controlado por índice y condición
        cuenta_encontrada = None
        i = 0
        while i < len(self.__cuentas) and cuenta_encontrada is None:
            if self.__cuentas[i].nombre == nombre_cuenta:
                cuenta_encontrada = self.__cuentas[i]
            i += 1

        # Si se localiza la cuenta, se procede al registro
        if cuenta_encontrada:
            cuenta_encontrada.registrar_transaccion(cantidad, transaccion_desc)
        else:
            print(f"Error: No se encontró la cuenta '{nombre_cuenta}'.")

    def verificar_alertas(self):
        # Identifica cuentas en negativo y genera el log de alertas
        alertas = []
        for c in self.__cuentas:
            if c.saldo < 0:
                alertas.append(f"¡Alerta! La cuenta '{c.nombre}' tiene saldo negativo: {c.saldo}€")

        if alertas:
            self.exportar_a_texto("alertas.log", "\n".join(alertas))
        return alertas

    def generar_informe_mensual(self, mes, año):
        # Crea un resumen de todas las cuentas en un archivo de texto
        resumen = f"--- INFORME MENSUAL {mes}/{año} ---\n"
        for cuenta in self.__cuentas:
            resumen += f"Cuenta: {cuenta.nombre} | Saldo: {cuenta.saldo}€\n"

        self.exportar_a_texto(f"informe_{año}_{mes}.txt", resumen)

    def exportar_a_texto(self, nombre_archivo, datos):
        # Escribe los datos proporcionados en un archivo físico
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(datos)

