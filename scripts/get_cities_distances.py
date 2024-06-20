import pandas as pd
from geopy.distance import geodesic
import io


folder = '../files'
filename = 'dataset_aeropuertos_mexico.csv'

# read the data from a CSV file
df = pd.read_csv(f'{folder}/{filename}')

# initialize the dictionary of distances
distances = {i: {} for i in df.index}

# initialize the dictionary of city names
city_names = {i: name for i, name in enumerate(df['ciudad'])}

# calculate the distances between each pair of cities
for i in df.index:
    for j in df.index:
        if i == j:
            distances[i][j] = 0
        else:
            coord1 = (df.at[i, 'latitud'], df.at[i, 'longitud'])
            coord2 = (df.at[j, 'latitud'], df.at[j, 'longitud'])
            distance = geodesic(coord1, coord2).kilometers
            # round to 6 decimal places
            distances[i][j] = round(distance, 6)



# write the distances and city names to a Python file
with open("TSP/data_aeropuertos.py", "w") as file:
    file.write("distances = {\n")
    for i in distances:
        file.write(f"    {i}: {distances[i]},\n")
    file.write("}\n\n")
    file.write("city_names = {\n")
    for i in city_names:
        file.write(f"    {i}: '{city_names[i]}',\n")
    file.write("}")
