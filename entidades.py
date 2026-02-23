class Coche:
    # Atributo de clase: Diccionario para acumular km por marca
    km_totales_por_marca = {}

    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0
        self.gasolina = 0
        self.consumo = 0.05

        # Si la marca no existe en el registro global, la inicializamos a 0
        if self.marca not in Coche.km_totales_por_marca:
            Coche.km_totales_por_marca[self.marca] = 0

    def avanzar(self, km):
        if self.gasolina > 0:
            if self.gasolina > (self.consumo * km):
                self.kilometros_recorridos += km
                Coche.km_totales_por_marca[self.marca] += km
                self.gasolina -= km * self.consumo

            else:
                print(f'No tienes gasolina suficiente para recorrer {km} km')
        else:
            print("El coche no tiene gasolina...")

    @classmethod
    def obtener_km_por_marca(cls, marca):

        return cls.km_totales_por_marca.get(marca, 0)

    def repostar(self, litros):
        self.gasolina += litros
        print(f'Has repostado {litros} litros de gasolina')


class Persona:
    def __init__(self, dni, nombre, apellido, coche=None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        # El atributo coche es opcional; si no se pasa, es None (sin coche)
        self.coche = coche

    def vender_coche(self, a_persona):
        if self.coche is not None and a_persona.coche is None:
            a_persona.coche = self.coche
            self.coche = None

        else:
            print(f'Error en la venta: Verifica que {self.nombre} tenga coche y que {a_persona.nombre} no tenga uno ya.')