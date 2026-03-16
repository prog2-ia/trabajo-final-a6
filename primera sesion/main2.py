from coche import Coche, CocheCombustion, CocheElectrico, CocheHibrido
from persona import Persona
from concesionario import Concesionario

# Crear dos coches
coche_juan = CocheCombustion("1234-ABC", "Toyota")

coche_pedro = CocheElectrico("6978-ART", "Tesla")

coche_dunsqui = CocheHibrido("8377-LBK", "Ferrari")



# Simular que el coche de Juan recorre algunos km
coche_juan.avanzar(150)
coche_pedro.avanzar(100)
coche_dunsqui.avanzar(100)


coche_juan.repostar(100)
coche_juan.avanzar(150)
coche_pedro.recargar(70)
coche_pedro.avanzar(100)
coche_dunsqui.recargar(3)
coche_dunsqui.repostar(20)
coche_dunsqui.avanzar(100)

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
print(f"km totales Ferrari en la flota: {Coche.km_totales_por_marca['Ferrari']} km")

print()
# 1. Pruebas de __str__ y __repr__ en Coches y Personas
print("Salida legible (__str__) del coche de Pedro:", str(coche_pedro))
print("Salida técnica (__repr__) del coche de Pedro:", repr(coche_pedro))
print("Salida legible (__str__) de la persona 3:", str(persona3))

# 2. Creación del concesionario
mi_conce = Concesionario("Coches UA")
mi_conce.agregar_coche(coche_juan)
mi_conce.agregar_coche(coche_pedro)
mi_conce.agregar_coche(coche_dunsqui)

mi_conce.agregar_cliente(persona1)
mi_conce.agregar_cliente(persona2)

# 3. Pruebas en el concesionario
print("\nSalida legible del concesionario:", str(mi_conce))

print(f"\nUso de len(): El concesionario tiene {len(mi_conce)} coches.")

# 4. Prueba de __bool__ con if/else sencillo
print("\nPrueba de evaluación booleana:")
if mi_conce:
    print("El concesionario tiene stock disponible.")
else:
    print("El concesionario está vacío.")

# 5. Prueba de acceso por índice con [] (__getitem__)
print("\nPrueba de acceso por índice:")
print("Coche en la posición 0:", mi_conce[0].marca)
print("Coche en la posición 1:", mi_conce[1].marca)
print("Coche en la posición 2:", mi_conce[2].marca)

