class Transaccion:
    def __init__(self, descripcion: str, cantidad: float, categoria: Categoria | None = None) -> None:
        # Atributos protegidos para asegurar el encapsulamiento
        self._descripcion: str = descripcion
        self._cantidad: float = cantidad
        self._categoria: Categoria | None = categoria

    def obtener_descripcion(self)-> str:
        # Metodo de acceso seguro a la descripción
        return self._descripcion

    def obtener_cantidad(self)-> float:
        # Metodo de acceso seguro al importe
        return self._cantidad

    def obtener_categoria(self)-> Categoria | None:
        # Devuelve el objeto Categoria asociado, si existe
        return self._categoria

    def __str__(self)-> str:
        # Muestra la transacción con su categoría si está asignada
        if self._categoria is not None:
            return f"{self._descripcion} ({self._categoria.nombre}) : {self._cantidad}€"

        # Formato estándar si no hay categoría
        return f"{self._descripcion} : {self._cantidad}€"