class Transaccion:
    def __init__(self, descripcion, cantidad, categoria=None):
        # Atributos protegidos para asegurar el encapsulamiento
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._categoria = categoria

    def obtener_descripcion(self):
        # Metodo de acceso seguro a la descripción
        return self._descripcion

    def obtener_cantidad(self):
        # Metodo de acceso seguro al importe
        return self._cantidad

    def obtener_categoria(self):
        # Devuelve el objeto Categoria asociado, si existe
        return self._categoria

    def __str__(self):
        # Muestra la transacción con su categoría si está asignada
        if self._categoria is not None:
            return f"{self._descripcion} ({self._categoria.nombre}) : {self._cantidad}€"

        # Formato estándar si no hay categoría
        return f"{self._descripcion} : {self._cantidad}€"