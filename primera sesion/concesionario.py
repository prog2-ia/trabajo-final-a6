class Concesionario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coches = []
        self.clientes = []

    def agregar_coche(self, coche):
        self.coches.append(coche)

    def agregar_cliente(self, persona):
        self.clientes.append(persona)

    def __getitem__(self, indice):
        return self.coches[indice]

    def __len__(self):
        return len(self.coches)

    def __bool__(self):
        return len(self.coches) > 0

    def __str__(self):
        return f"Concesionario '{self.nombre}' | Stock: {len(self.coches)} coches | Clientes: {len(self.clientes)}"

    def __repr__(self):
        return f"Concesionario('{self.nombre}', coches={repr(self.coches)})"