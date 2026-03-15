from abc import ABC, abstractmethod

class Cuenta (ABC):
    def __init__(self, nombre, saldo_inicial: float = 0.0):
        self.nombre = nombre
        self._saldo_actual = saldo_inicial
        self._historial_transacciones = []

    @property
    def saldo(self):
        return self._saldo_actual

    @abstractmethod
    def obtener_tipo(self):

        pass

    def registrar_transaccion(self,cantidad: float, descripcion: str = ""):

        self._saldo_actual += cantidad
        self._historial_transacciones.append(f'{descripcion} : {cantidad}')

    def transferir(self, cantidad, cuenta_destino):
        if self._saldo_actual >= cantidad:

            self.registrar_transaccion(f"Transferencia enviada a {cuenta_destino.nombre}", -cantidad)
            cuenta_destino.registrar_transaccion(f"Transferencia recibida de {self.nombre}", cantidad)
            print(f"Transferencia de {cantidad}€ realizada con éxito.")
        else:
            print("Saldo insuficiente para realizar la transferencia.")



class CuentaAhorro(Cuenta):
    def __init__(self, nombre: str, saldo_inicial: float, objetivo_ahorro: float):
        super().__init__(nombre, saldo_inicial)
        self.objetivo_ahorro = objetivo_ahorro

    def obtener_tipo(self):
        return "Cuenta Ahorro"

class CuentaPrincipal(Cuenta):
    def __init__(self, nombre: str, saldo_inicial: float):
        super().__init__(nombre, saldo_inicial)

    def obtener_tipo(self):
        return "Cuenta Principal"

