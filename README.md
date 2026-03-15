[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)

# Gestor de Finanzas Personales 💰

## 1. Propósito del Proyecto
Este proyecto es una aplicación desarrollada en Python para la gestión integral de finanzas personales. Permite administrar diferentes tipos de cuentas bancarias, categorizar gastos e ingresos mediante una estructura jerárquica (padre-hijo), registrar transacciones y generar informes automatizados. 

El diseño del código aplica estrictamente los principios de la **Programación Orientada a Objetos (POO)** requeridos, incluyendo:
* **Encapsulamiento:** Uso de atributos privados/protegidos (ej. `_subcategorias`, `__cuentas`).
* **Herencia y Polimorfismo:** Implementación de distintos tipos de cuentas (`CuentaPrincipal`, `CuentaAhorro`) que heredan de una clase base.
* **Clases Abstractas:** Uso del módulo `abc` para definir la estructura base de las cuentas.

## 2. Instalación y Configuración
Para ejecutar este proyecto de forma segura y cumplir con las buenas prácticas, se recomienda el uso de un entorno virtual:

1. Clona este repositorio en tu máquina local.
2. Abre una terminal en el directorio raíz del proyecto.
3. Crea un entorno virtual ejecutando:
   `python -m venv venv`
4. Activa el entorno virtual:
   - **Windows:** `venv\Scripts\activate`
   - **Mac/Linux:** `source venv/bin/activate`
5. (Opcional) Verifica las dependencias: `pip install -r requirements.txt`

## 3. Uso y Ejemplos
El punto de entrada de la aplicación es el archivo `main.py`. Para probar el funcionamiento del proyecto, simplemente ejecuta:

```bash
python main.py
