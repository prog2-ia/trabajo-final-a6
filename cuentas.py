class Cuenta:
    def __init__(self, nombre, saldo_inicial = 0):
        self.nombre = nombre
        self.saldo_actual = saldo_inicial
        self.historial_transacciones = []

    def registrar_transaccion(self, descripcion, cantidad):

        self.saldo_actual += cantidad
        self.historial_transacciones.append(f'{descripcion} : {cantidad}')

    def transferir(self, cantidad, cuenta_destino):
        if self.saldo_actual >= cantidad:

            self.registrar_transaccion(f"Transferencia enviada a {cuenta_destino.nombre}", -cantidad)

            cuenta_destino.registrar_transaccion(f"Transferencia recibida de {self.nombre}", cantidad)
            print(f"Transferencia de {cantidad}€ realizada con éxito.")
        else:
            print("Saldo insuficiente para realizar la transferencia.")



class CuentaAhorro(Cuenta):
    def __init__(self, nombre, saldo_inicial, objetivo_ahorro):
        super().__init__(nombre, saldo_inicial)
        self.objetivo_ahorro = objetivo_ahorro

class CuentaPrincipal(Cuenta):
    def __init__(self, nombre, saldo_inicial):
        super().__init__(nombre, saldo_inicial)

