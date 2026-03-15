from abc import ABC, abstractmethod

class Cuenta (ABC):
    #Creamos la clase abstracta  "Cuenta", para definir el comportamiento de cualquier cuenta '''
    def __init__(self, nombre, saldo_inicial: float = 0.0):
        self.nombre = nombre
        #Aquí lo que hacemos es proteger el saldo y el historial haciendolos privados
        self._saldo_actual = saldo_inicial
        self._historial_transacciones = []

    @property
    def saldo(self):
        #Aquí podemos mirar el saldo, pero no podremos modificarlo
        return self._saldo_actual

    @abstractmethod
    def obtener_tipo(self):
        # Utilizando en abstractmethod obligamos a las clases hijas a que implementen este metodo (cada una el suyo propio)
        pass

    def registrar_transaccion(self,cantidad: float, descripcion: str = ""):
        #Este metodo suma o resta dinero al saldo protegido y guarda el registro
        self._saldo_actual += cantidad
        self._historial_transacciones.append(f'{descripcion} : {cantidad}')

    def transferir(self, cantidad, cuenta_destino): # Realiza una transferencia a otra cuenta validando el saldo
        if self._saldo_actual >= cantidad:

            self.registrar_transaccion(f"Transferencia enviada a {cuenta_destino.nombre}", -cantidad)
            cuenta_destino.registrar_transaccion(f"Transferencia recibida de {self.nombre}", cantidad)
            print(f"Transferencia de {cantidad}€ realizada con éxito.")
        else:
            print("Saldo insuficiente para realizar la transferencia.")



class CuentaAhorro(Cuenta):
    # Creamo sun objeto cuenta ahorro
    def __init__(self, nombre: str, saldo_inicial: float, objetivo_ahorro: float):
        super().__init__(nombre, saldo_inicial)
        self.objetivo_ahorro = objetivo_ahorro

    def obtener_tipo(self):
        return "Cuenta Ahorro"

class CuentaPrincipal(Cuenta):
    # Y otro cuenta principal, la cuenta corriente
    def __init__(self, nombre: str, saldo_inicial: float):
        super().__init__(nombre, saldo_inicial)

    def obtener_tipo(self):
        return "Cuenta Principal"

