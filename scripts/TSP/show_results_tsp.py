import os
import pandas as pd
import folium
import webbrowser

def create_map(ruta_ids):
    folder = '../../files'
    path = f'{folder}/dataset_ciudades_mexico.csv'
    filename_html = 'mapa_ciudades_mexico.html'
    html_fullpath = f'{folder}/{filename_html}'
    
    start = ruta_ids[0]
    end = ruta_ids[-1]

    # load the data from the CSV file
    data = pd.read_csv(path)

    # create a map centered in Mexico using the latitude and longitude of the first city
    mapa_mexico = folium.Map(location=[23.6345, -102.5528], zoom_start=5, tiles="Cartodb Positron")

    # add a marker for each city
    for index, row in data.iterrows():          
        # search the position of the city in the route
        position = ruta_ids.index(index) + 1 if index in ruta_ids else None
        # define the text for the popup                
        popup_text = f"{row['ciudad']}, {row['estado']}<br>Latitud: {row['latitud']}<br>Longitud: {row['longitud']}"
        if position:
            # add the position in the route to the popup text
            popup_text += f"<br>Posición en ruta: {position}"
        if index == start:
            popup_text += "<br>Inicio"
        elif index == end:
            popup_text += "<br>Fin"
        
        # define the color of the icon
        icon_color = 'green' if index == start else 'red' if index == end else 'blue'
        # define the icon for the marker depending on the city position
        icon = 'home' if index == start else 'flag' if index == end else 'map-marker'
        
        # add the marker to the map
        folium.Marker(
            location=[row['latitud'], row['longitud']],
            popup=popup_text,
            icon=folium.Icon(color=icon_color, icon=icon, prefix='fa')
        ).add_to(mapa_mexico)

    # create and add the polyline to the map
    coords_ruta = [[data.loc[idx, 'latitud'], data.loc[idx, 'longitud']] for idx in ruta_ids if 0 <= idx < len(data)]
    folium.PolyLine(coords_ruta, color='green', weight=5, opacity=0.8, popup="Ruta de Ciudades").add_to(mapa_mexico)
    folium.PolyLine([coords_ruta[0], coords_ruta[-1]], color='red', weight=5, opacity=0.8, popup="Ruta de Inicio a Fin").add_to(mapa_mexico)

    # save the map to an HTML file
    mapa_mexico.save(html_fullpath)
    
    # open the HTML file in the web browser
    full_html_path = os.path.abspath(html_fullpath)
    webbrowser.open(f'file://{full_html_path}', new=2)
    
    return html_fullpath 

