from entidades import Coche, Persona

# Crear dos coches
coche_juan = Coche("1234-ABC", "Toyota")
coche_ana = Coche("5678-XYZ", "Honda")

# Simular que el coche de Juan recorre algunos km
coche_juan.avanzar(150)
coche_ana.avanzar(100)

coche_juan.repostar(100)
coche_juan.avanzar(150)

persona1 = Persona("11223344A", "Juan", "Pérez", coche_juan)


persona2 = Persona("55667788B", "Marta", "García", coche_ana)


print(f"Persona 1: {persona1.nombre}, Coche: {persona1.coche.marca if persona1.coche else 'Sin coche'}")
print(f"Persona 2: {persona2.nombre}, Coche: {persona2.coche.marca if persona2.coche else 'Sin coche'}")
print(f"Km totales Toyota en la flota: {Coche.km_totales_por_marca['Toyota']} km")
print(f"Km totales Honda en la flota: {Coche.km_totales_por_marca['Honda']} km")