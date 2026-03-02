class Categoria:
    def __init__(self,nombre, categoria_padre: none, descripcion):
        self.nombre = nombre
        self.categoria_padre = categoria_padre
        self.descripcion = descripcion
        self.subcategorias = []

        if self.categoria_padre is not None:
            self.categoria_padre.agregar_subcategoria(self)

    def agregar_subcategoria(self, subcategoria):
        if subcategoria not in self.subcategorias:
            self.subcategorias.append(subcategoria)

    def obtener_ruta(self):
        if self.categoria_padre is None:
            return self.nombre
        else:
            return f"{self.categoria_padre.obtener_ruta()} > {self.nombre}"

    def __str__(self):
        return f"Categoría: {self.nombre} (Hijos: {len(self.subcategorias)})"

    def es_raiz(self) -> bool:
        return self.categoria_padre is None

