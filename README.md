[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)

# Gestor de Finanzas Personales 

* **Gestión Multi-cuenta:** Soporte para Cuentas Principales (Corrientes) y Cuentas de Ahorro con objetivos específicos y dinámicos.
* **Categorización Jerárquica:** Sistema recursivo de categorías (Estructura Padre-Hijo) para un rastreo minucioso del origen de los gastos o ingresos.
* **Control de Presupuestos Activo:** Alertas inmediatas en consola y volcados automáticos en ficheros log si un gasto supera el presupuesto mensual asignado.
* **Transferencias Seguras:** Mecanismo de validación e intercambio de fondos entre cuentas con control estricto de saldo e importes negativos.
* **Persistencia de Datos:** Guardado automático del estado completo del gestor mediante serialización con `pickle` al salir de la aplicación, y autorecuperación al iniciar.
* **Generación de Informes:** Exportación de estados financieros mensuales estructurados en formato de texto plano (`.txt`).

---

## Arquitectura y Principios POO Aplicados

El diseño del software aplica de forma estricta los pilares de la **Programación Orientada a Objetos (POO)**:

### 1. Encapsulamiento y Propiedades
Se protegen los estados internos críticos mediante atributos privados (`__cuentas`) y protegidos (`_saldo_actual`, `_subcategorias`). El acceso y la lectura segura se gestionan a través de decoradores `@property` y métodos accesores dedicados, impidiendo la manipulación externa descontrolada del saldo o historiales.

### 2. Abstracción y Polimorfismo
La clase base `Cuenta` (en `cuentas.py`) se define como una **Clase Abstracta** utilizando el módulo `abc`. Obliga a sus clases hijas (`CuentaPrincipal` y `CuentaAhorro`) a implementar su propio método `obtener_tipo()`, permitiendo tratar de forma polimórfica cualquier cuenta dentro de las colecciones del gestor.

### 3. Gestión Avanzada de Excepciones
El sistema cuenta con una jerarquía propia de errores robusta basada en una clase madre (`ErrorFinanzas`):
* `ImporteInvalidoError`: Captura montos negativos o nulos.
* `SaldoInsuficienteError`: Evita descubiertos no autorizados calculando la diferencia exacta faltante.
* `FechaInvalidaError` & `PresupuestoExcedidoError`: Controlan desajustes temporales y topes de gasto.

### 4. Sobrecarga de Operadores (Dunder Methods)
La clase `GestorFinanzas` implementa métodos mágicos como `__getitem__` y `__len__`, permitiendo iterar e interactuar directamente sobre el gestor en la capa de interfaz (`for cuenta in gestor`) como si fuera una colección nativa de Python.

---

## Estructura del Proyecto

```text
├── categorias.py       # Modelo de categorías jerárquicas y rutas recursivas.
├── cuentas.py          # Clase abstracta Cuenta y subtipos (Ahorro/Principal).
├── excepciones.py      # Definición de la jerarquía de excepciones personalizadas.
├── gestor.py           # Motor lógico (control de flujos, reportes y alertas).
├── interfaz.py         # Orquestador del menú interactivo por consola.
├── main.py             # Punto de entrada (Carga de sesión o datos semilla).
├── presupuestos.py     # Lógica de asignación y cálculo de progreso de presupuestos.
├── transacciones.py    # Modelo contenedor de operaciones individuales.
├── README.md           # Documentación del proyecto.
└── requirements.txt    # Registro de dependencias (Entorno virtual listo).
