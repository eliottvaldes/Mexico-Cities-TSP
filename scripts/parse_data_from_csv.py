import csv
import os

def read_csv_to_dict(folder, filename):
    # Construye la ruta completa al archivo CSV
    filepath = os.path.join(folder, filename)
    
    # Lista para almacenar los diccionarios de cada fila del CSV
    data_list = []
    
    # Abrir el archivo CSV y leer los datos
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            # Crea un diccionario con la estructura especificada y lo añade a la lista
            data_dict = {
                'id': i,  # Usamos i para el ID, comenzando en 0
                'estado': row['estado'],
                'ciudad': row['ciudad'],
                'nombre_recinto': row['nombre_recinto'] if 'nombre_recinto' in row else row['ciudad'],
                'latitud': row['latitud'],
                'longitud': row['longitud']
            }
            data_list.append(data_dict)
    
    # Guarda el diccionario en un archivo Python
    save_dict_to_file(data_list, folder)

def save_dict_to_file(data, folder):
    # Construye la ruta al archivo de salida
    output_filepath = os.path.join(folder, 'data.py')
    
    # Escribe el diccionario en el archivo con formato adecuado
    with open(output_filepath, 'w', encoding='utf-8') as file:
        # crea un salto de linea entre cada objeto antes de escribirlo
        file.write('data = [\n')
        for obj in data:
            file.write(f'{obj},\n')
        file.write(']')        
        

# Define la ruta al folder y el nombre del archivo CSV
folder = '../files'
filename = 'dataset_autobuses_mexico.csv'

# Llama a la función principal
read_csv_to_dict(folder, filename)
