# Proyecto de Mapeo y TSP de Ciudades en México

Este repositorio contiene scripts y datos necesarios para visualizar un mapa de México y realizar un análisis del Problema del Agente Viajero (TSP) con las ciudades principales del país.

## Estructura del Repositorio

Dentro de este repositorio, encontrarás las siguientes carpetas:

- `mexico_boundary`: Contiene archivos utilizados para visualizar el mapa de México en MATLAB, proporcionados y mejorados a partir de los originales del profesor.
- `files`: Incluye los archivos generados por los scripts, como `dataset_ciudades_mexico.csv` para los datos de las ciudades y `mapa_ciudades_mexico.html` para el mapa visual del TSP.
- `scripts`: Contiene los códigos necesarios para ejecutar todo el proceso desde cero, incluyendo los scripts de MATLAB y Python.

## Instrucciones de Uso

Para explorar y utilizar este proyecto, sigue los siguientes pasos:

### Con MATLAB

1. (Opcional) Ejecuta `scripts/show_initial_mexico_map.m` para visualizar el mapa de México. Este script mejora visualmente el mapa original enviado por el profesor.
2. Ejecuta `scripts/create_dataset_mexico_cities.m` para exportar los datos del mapa a un archivo CSV. Puedes encontrar el archivo generado en `files/dataset_ciudades_mexico.csv`.

### Con Python

3. Ejecuta `scripts/get_cities_distances.py` para calcular la distancia en kilómetros entre cada par de ciudades. Al ejecutar este script, se genera automaticamente el archivo `scripts/TSP/data_cities.py` que contiene la matriz de distancias entre las ciudades. Este archivo es necesario para el análisis del TSP.
4. Ejecuta `scripts/TSP/main.py` para realizar el análisis del TSP. Los resultados se mostrarán en la consola y el mapa generado se abrirá automáticamente desde `files/mapa_ciudades_mexico.html`.

### Ejecución Automática

Si deseas ejecutar el análisis del TSP sin realizar los pasos intermedios manualmente, simplemente ejecuta `scripts/TSP/main.py`. Este script automatiza todo el proceso, muestra los resultados en consola y genera un mapa visual en HTML que se abrirá automáticamente.

## Contacto

Si tienes preguntas o necesitas ayuda con el proyecto, no dudes en abrir un issue en este repositorio o contactarme directamente.
