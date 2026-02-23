class ErrorFinanzas(Exception):
    pass
class ImporteInvalidoError(ErrorFinanzas):
    pass
class FechaInvalidaError(ErrorFinanzas):
    pass
class SaldoInsuficienteError(ErrorFinanzas):
    pass
class PresupuestoExcedidoError(ErrorFinanzas):
    pass
