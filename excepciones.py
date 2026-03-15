class ErrorFinanzas():
    #Esta es la clase base de la que heredaran los errores del sistema
    pass
class ImporteInvalidoError(ErrorFinanzas):
    def __init__(self, importe_erroneo):
        self.importe_erroneo = importe_erroneo
        #Recibira el importe invalido que provoco el fallo.

    def __str__(self):
        # Nos hará una representación del error y nos indicará que importe falló

        pass


class FechaInvalidaError(ErrorFinanzas):
    def __init__(self, fecha_erronea):
        # Guardará la fecha erronea para mostrarla
        pass
    def sugerir_formato(self):
        #Sugerira un formato correcto.
        pass

    def __str__(self):
        # Devolverá el mensaje de error
        pass

class SaldoInsuficienteError(ErrorFinanzas):
    def __init__(self, saldo_actual, cantidad_intentada):
        # Almacenará cuánto dinero había en la cuenta y cuánto se intentó sacar o transferir.
        pass

    def calcular_diferencia(self):
        # Calculará cuánto dinero faltaba para poder hacer la operación.
        pass

    def __str__(self):
        # Mensaje de error diciendo el saldo actual y el intento fallido.
        pass

class PresupuestoExcedidoError(ErrorFinanzas):
    def __init__(self, categoria, limite_sobrepasado):
        # Guardará la categoría del presupuesto y el límite que ha saltado.
        pass

    def __str__(self):
        # Mensaje de error avisando de que se ha roto el presupuesto de la categoría.
        pass

