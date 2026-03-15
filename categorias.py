class Categoria:
    def __init__(self,nombre: str, categoria_padre = None, descripcion: str = ""):
        self.nombre = nombre
        self.categoria_padre = categoria_padre
        self.descripcion = descripcion
        self._subcategorias = []

        if self.categoria_padre is not None:
            self.categoria_padre.agregar_subcategoria(self)

    def agregar_subcategoria(self, subcategoria):
        if subcategoria not in self._subcategorias:
            self._subcategorias.append(subcategoria)

    def obtener_ruta(self):
        if self.categoria_padre is None:
            return self.nombre
        else:
            return f"{self.categoria_padre.obtener_ruta()} > {self.nombre}"

    def es_raiz(self):
        return self.categoria_padre is None

    def obtener_subcategorias(self):
        return self._subcategorias

    def __str__(self):
        return f"Categoría: {self.nombre} (Hijos: {len(self._subcategorias)})"



