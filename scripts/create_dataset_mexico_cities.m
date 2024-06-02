clc;
clear;
close all;

% read the data from the Shapefile for cities
mexicoC = readgeotable("mexico_boundary/México_Ciudades.shp");

% extract the necessary data
id = (1:height(mexicoC))'; % generate an ID for each city
state = mexicoC.ESTADO;
city = mexicoC.CIUDAD;
latitud = zeros(height(mexicoC), 1);
longitud = zeros(height(mexicoC), 1);

% Extract latitude and longitude of each point
for i = 1:height(mexicoC)
    latitud(i) = mexicoC.Shape(i).Latitude;
    longitud(i) = mexicoC.Shape(i).Longitude;
end

% create a table with the data
dataCities = table(id, state, city, latitud, longitud);

% define the name of the CSV file
csvFilename = '../files/dataset_ciudades_mexico.csv';

% write the data to a CSV file
writetable(dataCities, csvFilename);

disp(['Archivo CSV creado: ', csvFilename]);
