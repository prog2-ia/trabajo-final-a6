from abc import ABC, abstractmethod
from excepciones import SaldoInsuficienteError, ImporteInvalidoError

class Cuenta (ABC):
    #Creamos la clase abstracta  "Cuenta", para definir el comportamiento de cualquier cuenta '''
    def __init__(self, nombre: str, saldo_inicial: float = 0.0)->None:
        self.nombre: str = nombre
        #Aquí lo que hacemos es proteger el saldo y el historial haciendolos privados
        self._saldo_actual: float = saldo_inicial
        self._historial_transacciones: list[str] = []

    @property
    def saldo(self)-> float:
        #Aquí podemos mirar el saldo, pero no podremos modificarlo
        return self._saldo_actual

    @abstractmethod
    def obtener_tipo(self)-> str:
        # Utilizando en abstractmethod obligamos a las clases hijas a que implementen este metodo (cada una el suyo propio)
        pass

    def registrar_transaccion(self, cantidad: float, descripcion: str = "") -> None:
        # Actualiza el saldo y guarda el registro en el historial
        self._saldo_actual += cantidad
        self._historial_transacciones.append(f'{descripcion} : {cantidad}')

    def transferir(self, cantidad: float, cuenta_destino: 'Cuenta') -> None:
        # Valida que el importe sea positivo y haya saldo suficiente [cite: 22, 23, 178, 179]
        if cantidad <= 0:
            raise ImporteInvalidoError(cantidad)

        if self._saldo_actual < cantidad:
            raise SaldoInsuficienteError(self._saldo_actual, cantidad)

        # Ejecuta el movimiento de fondos entre ambas cuentas
        self.registrar_transaccion(-cantidad, f"Transferencia a {cuenta_destino.nombre}")
        cuenta_destino.registrar_transaccion(cantidad, f"Transferencia de {self.nombre}")
        print(f"Transferencia de {cantidad}€ realizada con éxito.")



class CuentaAhorro(Cuenta):
    # Creamo sun objeto cuenta ahorro
    def __init__(self, nombre: str, saldo_inicial: float, objetivo_ahorro: float)->None:
        super().__init__(nombre, saldo_inicial)
        self.objetivo_ahorro: float = objetivo_ahorro

    def obtener_tipo(self)->str:
        return "Cuenta Ahorro"

class CuentaPrincipal(Cuenta):
    # Y otro cuenta principal, la cuenta corriente
    def __init__(self, nombre: str, saldo_inicial: float)->None:
        super().__init__(nombre, saldo_inicial)

    def obtener_tipo(self)-> str:
        return "Cuenta Principal"

