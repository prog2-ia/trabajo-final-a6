class Categoria:
    def __init__(self, nombre, categoria_padre=None, descripcion=""):
        # Definición de los atributos principales de la categoría
        self.nombre = nombre
        self.categoria_padre = categoria_padre
        self.descripcion = descripcion

        # Atributo protegido para el manejo interno de subcategorías
        self._subcategorias = []

        # Si se indica un padre, esta categoría se añade automáticamente a su lista de hijos
        if self.categoria_padre is not None:
            self.categoria_padre.agregar_subcategoria(self)

    def agregar_subcategoria(self, subcategoria):
        # Inserta una subcategoría en la lista comprobando que no esté ya presente
        if subcategoria not in self._subcategorias:
            self._subcategorias.append(subcategoria)

    def obtener_ruta(self):
        # Construye la jerarquía completa de nombres de forma recursiva
        if self.categoria_padre is None:
            return self.nombre
        else:
            return f"{self.categoria_padre.obtener_ruta()} > {self.nombre}"

    def es_raiz(self):
        # Verifica si la categoría es de nivel superior (no tiene padre)
        return self.categoria_padre is None

    def obtener_subcategorias(self):
        # Metodo para acceder a la lista protegida de subcategorías
        return self._subcategorias

    def __str__(self):
        # Retorna la representación visual simple de la categoría y sus hijos
        return f"Categoría: {self.nombre} (Hijos: {len(self._subcategorias)})"



