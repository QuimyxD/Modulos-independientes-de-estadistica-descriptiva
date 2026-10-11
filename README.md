# Generador y Analizador Estadístico de Datos en Python (Datos Agrupados)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-orange.svg)

**Generador y Analizador Estadístico de Datos** es una librería y suite de software modular en Python (`estadisitica_analitica_lib`) orientada al procesamiento, agrupación en intervalos de clase y análisis estocástico/descriptivo de series cuantitativas (discretas y continuas) de datos[cite: 1].

El sistema fue diseñado bajo el patrón de software de **doble contexto** (`if __name__ == "__main__":`), permitiendo que cada componente funcione indistintamente como un paquete reutilizable para aplicaciones externas o como un módulo autónomo de auditoría analítica[cite: 1, 3]. Desarrollado como parte de las actividades académicas en la **Universidad de Guanajuato** (División de Ingenierías, Campus Irapuato - Salamanca)[cite: 1].

---

## Tabla de Contenidos

- [Descripción General y Objetivos](#-descripción-general-y-objetivos)
- [Características Principales](#-características-principales)
- [Arquitectura del Software y Estructura del Proyecto](#-arquitectura-del-software-y-estructura-del-proyecto)
- [Fundamentos Matemáticos y Módulos](#-fundamentos-matemáticos-y-módulos)
  - [1. Distribución de Frecuencias (`Frecuencias.py`)](#1-distribución-de-frecuencias-frecuenciaspy)
  - [2. Medidas de Tendencia Central y Posición (`Tendencias.py`)](#2-medidas-de-tendencia-central-y-posición-tendenciaspy)
  - [3. Medidas de Dispersión y Variabilidad (`Dispersion.py`)](#3-medidas-de-dispersión-y-variabilidad-dispersionpy)
  - [4. Análisis de Forma y Geometría (`Forma.py`)](#4-análisis-de-forma-y-geometría-formapy)
- [Modos de Interfaz y Salida Tabular](#-modos-de-interfaz-y-salida-tabular)
- [Instrucciones de Uso y Ejecución](#-instrucciones-de-uso-y-ejecución)
  - [Requisitos Previos](#requisitos-previos)
  - [Ejecución del Script Principal](#ejecución-del-script-principal)
  - [Auditorías Autónomas por Submódulo](#auditorías-autónomas-por-submódulo)
- [Validación Numérica y Resultados](#-validación-numérica-y-resultados)
- [Autor y Créditos](#-autor-y-créditos)

---

## Descripción General y Objetivos

En la estadística descriptiva para grandes volúmenes de datos, el agrupamiento en distribuciones de frecuencias resulta esencial para condensar la información e identificar patrones geométricos, de centralización y de variabilidad[cite: 1]. Este proyecto implementa algoritmos de interpolación lineal y momentos estadísticos utilizando estrictamente **sintaxis nativa de Python** (sin librerías de terceros para los cálculos numéricos).

### Objetivos Clave:
1. **Diseño Modular Jerárquico**: Estructurar una librería en Python (`estadisitica_analitica_lib`) dividida en submódulos especializados[cite: 1].
2. **Independencia de Ejecución**: Implementar el patrón de doble contexto para auditorías unitarias independientes de código[cite: 1, 3].
3. **Agrupamiento Automático**: Determinar clases, límites reales y marcas de clase aplicando la Regla de Sturges[cite: 1, 3].
4. **Análisis Estadístico Profundo**: Calcular métricas de tendencia central, dispersión, posición, momentos crudos/centrales, sesgo de Fisher-Pearson y exceso de curtosis[cite: 1].

---

## Características Principales

- **Patrón de Doble Contexto**: Permite la importación limpia de funciones o la prueba unitaria por terminal[cite: 1, 3].
- **Cero Dependencias Externas**: Algoritmos de búsqueda, ordenamiento e interpolación lineal desarrollados con estructuras de control nativas (`for`, `while`, condicionales y listas).
- **Soporte para Tipos de Datos Duales**: Procesamiento de variables continuas (flotantes) y discretas (enteras)[cite: 1].
- **Generación Sintética de Pruebas**: Inclusión de vectores de prueba/auditoría aleatorios[cite: 1, 5].
- **Formateo de Salida Avanzado**: Despliegue dinámico de tablas resumen en consola utilizando *f-strings* y caracteres de caja[cite: 1, 4].

---

## Arquitectura del Software y Estructura del Proyecto

El código aplica una separación estricta de responsabilidades (*Separation of Concerns*) mediante un paquete ejecutable[cite: 1, 3]:

```text
.
├── Modulos_estadistica_datos_agrupados/
│   ├── main.py                          # Script cliente principal e interfaz de usuario
│   └── estadisitica_analitica_lib/       # Paquete principal de Python
│       ├── __init__.py                  # Inicializador del paquete importable
│       ├── Frecuencias.py               # Agrupamiento, regla de Sturges y marcas de clase
│       ├── Tendencias.py                # Promedios (μ, G, H, RCM) y posición interpolada
│       ├── Dispersion.py                # Rangos, varianza, desviación y coef. variación
│       └── Forma.py                     # Momentos, sesgo de Fisher y curtosis
├── Modulos independientes _estadistica descriptiva_Cecil Quimey Azuara Yañez.pdf  # Reporte técnico en PDF
└── README.md                            # Documentación principal del repositorio

´´´ 
---

## Modos de interfaz y salida modular

El script cliente main.py integra los datos procesados en un diccionario consolidado e imprime un reporte formateado en consola mediante f-strings:

+-----------------------------------------------------------------------+
| Concepto                                  |                     Valor |
+-----------------------------------------------------------------------+
| INFORMACIÓN GENERAL (CONTINUOS)                                       |
+-----------------------------------------------------------------------+
| Total de Datos (N)                        |                       100 |
| Número de Clases (k)                      |                         8 |
| Amplitud de Clase (c)                     |                   12.3750 |
| Rango Total                               |                   99.0000 |
+-----------------------------------------------------------------------+
| MEDIDAS DE TENDENCIA CENTRAL                                          |
+-----------------------------------------------------------------------+
| Media Aritmética                          |                   50.0000 |
| Media Geométrica                          |                   38.5731 |
| Media Armónica                            |                   25.3062 |
| Mediana                                   |                   50.0000 |
| Moda                                      |                   11.9911 |
| Raíz Cuadrada Media (RCM)                 |                   57.5868 |
+-----------------------------------------------------------------------+
| MOMENTOS Y FORMA                                                      |
+-----------------------------------------------------------------------+
| Sesgo Fisher-Pearson                      |                    0.0000 |
| Diagnóstico de Sesgo                      |            Asimetría leve |
| Exceso de Curtosis                        |                   -1.2498 |
| Tipo de Curtosis                          |               Platicúrtica|
+-----------------------------------------------------------------------+


---

## Instrucciones de uso y ejecución

Requisitos Previos
Tener instalado Python 3.8 o superior (no requiere la instalación de librerías externas mediante pip).

---

## Ejecución del Script Principal

Para ejecutar el programa interactivo completo con el menú de selección de datos:
python Modulos_estadistica_datos_agrupados/main.py

Al iniciar, el sistema desplegará un menú dinámico para elegir el conjunto de pruebas sintéticas:   Datos Continuos: Muestra de 100 valores en punto flotante (float).   Datos Discretos: Muestra de 100 valores enteros (int)[cite: 1, 5].Auditorías Autónomas por SubmóduloGracias al patrón de doble contexto (if __name__ == "__main__":), puedes probar la lógica matemática de cada archivo de manera independiente directamente desde la consola:

# Probar el generador de frecuencias y regla de Sturges
python Modulos_estadistica_datos_agrupados/estadisitica_analitica_lib/Frecuencias.py

# Auditar promedios y medidas de posición interpoladas
python Modulos_estadistica_datos_agrupados/estadisitica_analitica_lib/Tendencias.py

# Auditar cálculo de varianza y desviación estándar
python Modulos_estadistica_datos_agrupados/estadisitica_analitica_lib/Dispersion.py

# Auditar momentos, sesgo y exceso de curtosis
python Modulos_estadistica_datos_agrupados/estadisitica_analitica_lib/Forma.py


---

## Validación Numérica y Resultados

Durante las pruebas de auditoría, el sistema demostró estricta concordancia con los principios teóricos de la estadística analítica:   Jerarquía Matemática de Promedios: Se verificó experimentalmente el cumplimiento de la desigualdad fundamental:

   $$H \le G \le \mu \le RCM \quad (25.3062 \le 38.5731 \le 50.0000 \le 57.5868)$$

Consistencia de Momentos: Se validó que el primer momento crudo ($m_1'$) coincide exactamente con la media aritmética ($\mu = 50.0000$) y que el segundo momento central ($m_2$) concuerda con la varianza ($\sigma^2 = 816.2395$).

Clasificación Geométrica: Las funciones de diagnóstico identificaron correctamente distribuciones simétricas ($\gamma_1 = 0.0000$) y de perfil platicúrtico ($\kappa = -1.2498$).

---

## Autor y Créditos

Cecil Quimey Azuara Yáñez[cite: 1]
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial (LIDIA)
Institución: Universidad de Guanajuato – División de Ingenierías (Campus Irapuato - Salamanca)[cite: 1]
Asignatura: Fundamentos del Análisis de Datos
