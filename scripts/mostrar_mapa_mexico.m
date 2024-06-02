clc;
clear;
close all;

% Agregar la carpeta con los archivos Shapefile
addpath("../mexico_boundary");

% Leer los datos del archivo Shapefile para ciudades y mostrar la estructura
mexicoE = readgeotable("México_Estados.shp");
mexicoC = readgeotable("México_Ciudades.shp");

% Crear una figura y definir la proyección del mapa
figure;
worldmap('Mexico'); % Inicia un mapa con los límites centrados en México
setm(gca, 'MLabelLocation', 5, 'PLabelLocation', 5, 'MLineLocation', 5, 'PLineLocation', 5);

% Mostrar los límites de los estados
geoshow(mexicoE);

% Mostrar las ciudades con un marcador
geoshow(mexicoC, 'DisplayType', 'point', 'Marker', '.', 'Color', 'red', 'MarkerSize', 8);

% Añadir anotaciones de texto para cada ciudad
for i = 1:height(mexicoC)
    lat = mexicoC.Shape(i).Latitude;
    lon = mexicoC.Shape(i).Longitude;
    ciudad = mexicoC.CIUDAD(i);
    estado = mexicoC.ESTADO(i);
    texto = sprintf('%s, %s\n(%0.2f, %0.2f)', ciudad, estado, lat, lon);
    textm(lat, lon, texto, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right', 'FontSize', 8, 'Color', 'blue');
end
