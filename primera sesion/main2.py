from coche import Coche, CocheCombustion, CocheElectrico
from persona import Persona

# Crear dos coches
coche_juan = CocheCombustion("1234-ABC", "Toyota")

coche_pedro = CocheElectrico("6978-ART", "Tesla")


# Simular que el coche de Juan recorre algunos km
coche_juan.avanzar(150)
coche_pedro.avanzar(100)


coche_juan.repostar(100)
coche_juan.avanzar(150)
coche_pedro.recargar(70)
coche_pedro.avanzar(100)

persona1 = Persona("11223344A", "Juan", "Pérez", coche_juan)

persona2 = Persona("78242856R", "Eusebio", "Franco")

persona3 = Persona("55667788B", "Pedro", "Barbu", coche_pedro)

#Pruebas de venta
persona1.vender_coche(persona2)

print("\n ESTADO TRAS LA VENTA")
print(f'Persona 1: {persona1.nombre}, Coche: {persona1.coche.marca if persona1.coche else "Sin coche"}')
print(f'Persona 2: {persona2.nombre}, Coche: {persona2.coche.marca if persona2.coche else "Sin coche"}')

print("\n FORZANDO ERROR DE VENTA")
persona1.vender_coche(persona2)


print(f"Km totales Toyota en la flota: {Coche.km_totales_por_marca['Toyota']} km")
print(f"Km totales Tesla en la flota: {Coche.km_totales_por_marca['Tesla']} km")
