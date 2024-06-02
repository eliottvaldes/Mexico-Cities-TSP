clc;
clear;
close all;

% Add the folder with the Shapefile files
addpath("../mexico_boundary");

% read the data from the Shapefile for cities and show the structure
mexicoE = readgeotable("México_Estados.shp");
mexicoC = readgeotable("México_Ciudades.shp");

% Create a figure and define the map projection
figure;
worldmap('Mexico'); % initiates a map with the boundaries centered in Mexico
setm(gca, 'MLabelLocation', 5, 'PLabelLocation', 5, 'MLineLocation', 5, 'PLineLocation', 5);

% show the boundaries of the states
geoshow(mexicoE);

% Show the cities with a marker
geoshow(mexicoC, 'DisplayType', 'point', 'Marker', '.', 'Color', 'red', 'MarkerSize', 8);

% add text annotations for each city
for i = 1:height(mexicoC)
    lat = mexicoC.Shape(i).Latitude;
    lon = mexicoC.Shape(i).Longitude;
    city = mexicoC.CIUDAD(i);
    state = mexicoC.ESTADO(i);
    text = sprintf('%s, %s\n(%0.2f, %0.2f)', city, state, lat, lon);
    textm(lat, lon, text, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right', 'FontSize', 8, 'Color', 'blue');
end
