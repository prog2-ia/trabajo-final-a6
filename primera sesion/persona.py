class Persona:
    def __init__(self, dni, nombre, apellido, coche=None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.coche = coche

    def vender_coche(self, a_persona):
        if self.coche is not None and a_persona.coche is None:
            a_persona.coche = self.coche
            self.coche = None
        else:
            print(f'Error en la venta: Verifica que {self.nombre} tenga coche y que {a_persona.nombre} no tenga uno ya.')

        def __str__(self):
            if self.coche is not None:
                tiene_coche = f"posee un {self.coche.marca}"
            else:
                tiene_coche = "no tiene coche"

            return f"{self.nombre} {self.apellido} ({tiene_coche})"

        def __repr__(self):
            return f"Persona('{self.dni}', '{self.nombre}', '{self.apellido}', coche={repr(self.coche)})"