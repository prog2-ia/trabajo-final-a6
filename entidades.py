class Coche:
    # Atributo de clase: Diccionario para acumular km por marca
    km_totales_por_marca = {}

    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0
        self.gasolina = 0

        # Si la marca no existe en el registro global, la inicializamos a 0
        if self.marca not in Coche.km_totales_por_marca:
            Coche.km_totales_por_marca[self.marca] = 0

    def conducir(self, km):
        self.kilometros_recorridos += km
        Coche.km_totales_por_marca[self.marca] += km


class Persona:
    def __init__(self, dni, nombre, apellido, coche=None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        # El atributo coche es opcional; si no se pasa, es None (sin coche)
        self.coche = coche