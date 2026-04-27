class ErrorFinanzas(Exception):
    # Clase base para todas las excepciones del sistema
    pass

class ImporteInvalidoError(ErrorFinanzas):
    def __init__(self, importe_erroneo):
        # Almacena el valor incorrecto que causó el error
        self.importe_erroneo = importe_erroneo

    def __str__(self):
        # Devuelve el mensaje de error para importes negativos o nulos
        return f"ImporteInvalidoError: El valor {self.importe_erroneo}€ no es válido (debe ser > 0)."

class FechaInvalidaError(ErrorFinanzas):
    def __init__(self, fecha_erronea):
        # Guarda la fecha con formato incorrecto
        self.fecha_erronea = fecha_erronea

    def sugerir_formato(self):
        # Indica el formato de fecha esperado por el sistema
        return "Formato sugerido: MM/AAAA o DD/MM/AAAA."

    def __str__(self):
        # Muestra el error de fecha junto con la sugerencia de formato
        return f"FechaInvalidaError: '{self.fecha_erronea}' no es válida. {self.sugerir_formato()}"

class SaldoInsuficienteError(ErrorFinanzas):
    def __init__(self, saldo_actual, cantidad_intentada):
        # Registra el estado de la cuenta y el importe fallido
        self.saldo_actual = saldo_actual
        self.cantidad_intentada = cantidad_intentada

    def calcular_diferencia(self):
        # Calcula el dinero restante necesario para la operación
        return self.cantidad_intentada - self.saldo_actual

    def __str__(self):
        # Detalla la falta de fondos y la diferencia calculada
        return (f"SaldoInsuficienteError: Intento de {self.cantidad_intentada}€ "
                f"en cuenta con solo {self.saldo_actual}€. Faltan {self.calcular_diferencia()}€.")

class PresupuestoExcedidoError(ErrorFinanzas):
    def __init__(self, categoria, limite_sobrepasado):
        # Identifica la categoría y el límite que se ha sobrepasado
        self.categoria = categoria
        self.limite_sobrepasado = limite_sobrepasado

    def __str__(self):
        # Notifica que se ha superado el tope de gasto establecido
        return f"PresupuestoExcedidoError: La categoría '{self.categoria}' superó su límite de {self.limite_sobrepasado}€."

