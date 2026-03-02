class Coche:
    km_totales_por_marca = {}

    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0


        if self.marca not in Coche.km_totales_por_marca:
            Coche.km_totales_por_marca[self.marca] = 0



    @classmethod
    def obtener_km_por_marca(cls, marca):

        return cls.km_totales_por_marca.get(marca, 0)



class CocheCombustion(Coche):
    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)
        self.gasolina = 0
        self.consumo = 0.05

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
        super().obtener_km_por_marca()

    def repostar(self, litros):
        self.gasolina += litros
        print(f'Has repostado {litros} litros de gasolina')



class CocheElectricto(Coche):
    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)
        self.consumo = 0.02
        self.bateria = 0

    def avanzar(self, km):
        if self.bateria > 0:
            if self.bateria > (self.consumo * km):
                self.kilometros_recorridos += km
                Coche.km_totales_por_marca[self.marca] += km
                self.bateria -= km * self.consumo

            else:
                print(f'No tienes batería suficiente para recorrer {km} km')
        else:
            print("El coche no tiene batería...")


    def recargar(self, kw):
        self.bateria += kw
        print(f'Has recargado {kw} kw'<)
