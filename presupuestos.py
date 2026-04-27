from excepciones import ImporteInvalidoError, PresupuestoExcedidoError


class Presupuesto:
    def __init__(self, categoria, cantidad_limite, mes, año):
        # Inicializa los datos básicos y el contador de gasto en cero
        self.categoria = categoria
        self.cantidad_limite = cantidad_limite
        self.mes = mes
        self.año = año
        self._gasto_acumulado = 0.0

    def añadir_gasto(self, cantidad):
        # Valida que el gasto sea positivo antes de sumarlo al total
        if cantidad < 0:
            raise ImporteInvalidoError(cantidad)

        self._gasto_acumulado += cantidad
        self.verificar_estado()

    def verificar_estado(self):
        # Lanza una excepción si el gasto actual supera el límite permitido
        if self._gasto_acumulado > self.cantidad_limite:
            raise PresupuestoExcedidoError(self.categoria.nombre, self.cantidad_limite)

    def obtener_progreso(self):
        # Calcula el porcentaje del presupuesto consumido
        if self.cantidad_limite == 0:
            return 0.0

        return (self._gasto_acumulado / self.cantidad_limite) * 100

    def __str__(self):
        # Muestra el resumen del gasto frente al límite establecido
        return f"Presupuesto {self.categoria.nombre}: {self._gasto_acumulado}/{self.cantidad_limite}€"