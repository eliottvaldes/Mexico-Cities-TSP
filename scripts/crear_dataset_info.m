clc;
clear;
close all;

% Leer los datos del archivo Shapefile para ciudades
mexicoC = readgeotable("mexico_boundary/México_Ciudades.shp");

% Extraer los datos necesarios
id = (1:height(mexicoC))'; % Generar un ID para cada ciudad
estado = mexicoC.ESTADO;
ciudad = mexicoC.CIUDAD;
latitud = zeros(height(mexicoC), 1);
longitud = zeros(height(mexicoC), 1);

% Extraer latitud y longitud de cada punto
for i = 1:height(mexicoC)
    latitud(i) = mexicoC.Shape(i).Latitude;
    longitud(i) = mexicoC.Shape(i).Longitude;
end

% Crear una tabla con los datos
datosCiudades = table(id, estado, ciudad, latitud, longitud);

% Especificar el nombre del archivo CSV
nombreArchivoCSV = '../files/dataset_ciudades_mexico.csv';

% Escribir los datos en un archivo CSV
writetable(datosCiudades, nombreArchivoCSV);

disp(['Archivo CSV creado: ', nombreArchivoCSV]);
