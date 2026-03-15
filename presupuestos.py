class Presupuesto:
    def __init__(self, categoria, cantidad_limite, mes, año):
        # Inicialización de los límites mensuales por categoría
        self.categoria = categoria
        self.cantidad_limite = cantidad_limite
        self.mes = mes
        self.año = año
        # Atributo privado para el seguimiento del gasto actual
        self._gasto_acumulado = 0.0

    def añadir_gasto(self, cantidad):
        # Metodo para sumar gastos al presupuesto actual
        # Aquí irá el manejo de excepciones (ej. si la cantidad es negativa)
        pass

    def verificar_estado(self):
        # Comprueba si el gasto acumulado supera el límite establecido
        pass

    def obtener_progreso(self):
        # Devuelve el porcentaje de presupuesto consumido
        pass

    def __str__(self):
        # Representación textual del presupuesto y su límite
        return f"Presupuesto {self.categoria.nombre}: {self.cantidad_limite}€"