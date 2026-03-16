from abc import ABC, abstractmethod

class Coche(ABC):
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

    def __str__(self):
        return f"Coche {self.marca} (Matrícula: {self.matricula})"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.matricula}', '{self.marca}')"


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


    def repostar(self, litros):
        self.gasolina += litros
        print(f'Has repostado {litros} litros de gasolina')



class CocheElectrico(Coche):
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
        print(f'Has recargado {kw} kw')

class CocheHibrido(CocheElectrico, CocheCombustion):
    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)

        self.consumo_electrico = 0.02
        self.consumo_gasolina = 0.05
        self.kilometros_recorridos = 0

    def avanzar(self, km):

        self.km_posibles_elec = self.bateria / self.consumo_electrico
        self.km_posibles_gas = self.gasolina / self.consumo_gasolina


        if km > (self.km_posibles_elec + self.km_posibles_gas):
            print('No puede realizarse el trayecto debido a que no tenemos suficiente autonomía total.')
            return


        if self.bateria >= (self.consumo_electrico * km):

            self.kilometros_recorridos += km
            Coche.km_totales_por_marca[self.marca] += km
            self.bateria -= km * self.consumo_electrico

        else:

            self.km_restantes = km - self.km_posibles_elec


            self.bateria = 0
            self.gasolina -= self.km_restantes * self.consumo_gasolina
            self.kilometros_recorridos += km
            Coche.km_totales_por_marca[self.marca] += km

            print(f'Has recorrido {km} km en total: {self.km_posibles_elec:.2f} en modo ELÉCTRICO y {self.km_restantes:.2f} en COMBUSTIÓN.')






